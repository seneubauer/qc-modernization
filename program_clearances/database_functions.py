# import dependencies
from sqlalchemy import create_engine, ForeignKey, UniqueConstraint, Column, Integer, Text, Float, Boolean
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine.base import Engine
from os.path import join
import pandas as pd

# instantiate the base
Base = declarative_base()

# define the tables
class Direction_Types(Base):
    __tablename__ = "dir_types"
    uid = Column(Text, nullable = False, unique = True, primary_key = True)

class Fixtures(Base):
    __tablename__ = "fixtures"
    uid = Column(Text, nullable = False, unique = True, primary_key = True)
    anchor_dir = Column(Text, ForeignKey("dir_types.uid"), nullable = False)
    anchor_val = Column(Float, nullable = False)
    py = Column(Float, nullable = False)
    px = Column(Float, nullable = False)
    ny = Column(Float, nullable = False)
    nx = Column(Float, nullable = False)

class Parts(Base):
    __tablename__ = "parts"
    uid = Column(Text, nullable = False, unique = True, primary_key = True)
    py = Column(Float, nullable = False)
    px = Column(Float, nullable = False)
    ny = Column(Float, nullable = False)
    nx = Column(Float, nullable = False)

class Programs(Base):
    __tablename__ = "programs"
    uid = Column(Integer, nullable = False, unique = True, primary_key = True)
    drawing = Column(Text, ForeignKey("parts.uid"), nullable = False)
    revision = Column(Text, nullable = False)
    fixture = Column(Text, ForeignKey("fixtures.uid"), nullable = True)
    py = Column(Float, nullable = False)
    px = Column(Float, nullable = False)
    ny = Column(Float, nullable = False)
    nx = Column(Float, nullable = False)
    requires_attention = Column(Boolean, nullable = False)
    operator_notes = Column(Text)
    developer_notes = Column(Text)
    __tableargs__ = (
        UniqueConstraint(drawing, revision)
    )

# create the database and its tables
def db_create(db_path:str) -> Engine:

    # create the database if it doesn't already exist
    engine = create_engine(f"sqlite:///{db_path}", echo = False)
    if not database_exists(engine.url):
        create_database(engine.url)

    # create the tables
    Base.metadata.create_all(engine)

    # return the database engine
    return engine

# populate the database's tables
def db_populate(data_path:str, engine:Engine):

    # import the cleaned data
    fixture_df = pd.read_csv(join(data_path, "fixture_clearances.csv"))
    part_df = pd.read_csv(join(data_path, "part_clearances.csv"))
    path_df = pd.read_csv(join(data_path, "path_clearances.csv"))

    # relfect the database
    base = automap_base()
    base.prepare(engine, reflect = True)

    # instantiate the database tables
    dir_types = base.classes.dir_types
    fixtures = base.classes.fixtures
    parts = base.classes.parts
    programs = base.classes.programs

    # create the session
    session = Session(engine)

    # add the direction types
    my_query = session.query(dir_types.uid).filter(dir_types.uid == "py").first()
    if my_query is None:
        session.add(dir_types(uid = "py"))
        session.add(dir_types(uid = "px"))
        session.add(dir_types(uid = "ny"))
        session.add(dir_types(uid = "nx"))

    # add data from the fixture dataframe
    for index, row in fixture_df.iterrows():

        my_uid = str(row["id"])
        my_anchor_dir = str(row["anchor_dir"])
        my_anchor_val = float(row["anchor_val"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])
        my_query = session.query(fixtures.uid).filter(fixtures.uid == my_uid).first()

        if my_query is None:
            session.add(fixtures(uid = my_uid, anchor_dir = my_anchor_dir, anchor_val = my_anchor_val, py = my_py, px = my_px, ny = my_ny, nx = my_nx))

    # add data from the part dataframe
    for index, row in part_df.iterrows():

        my_uid = str(row["id"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])
        my_query = session.query(parts.uid).filter(parts.uid == my_uid).first()

        if my_query is None:
            session.add(parts(uid = my_uid, py = my_py, px = my_px, ny = my_ny, nx = my_nx))

    # add data from the paths/program dataframe
    index = 0
    for index, row in path_df.iterrows():

        my_drawing = str(row["drawing"])
        my_revision = str(row["revision"])
        my_fixture = str(row["fixture"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])
        my_query = session.query(*[programs.drawing, programs.revision]).filter(programs.drawing == my_drawing).filter(programs.revision == my_revision).first()

        if my_query is None:
            session.add(programs(uid = index, drawing = my_drawing, revision = my_revision, fixture = my_fixture, py = my_py, px = my_px, ny = my_ny, nx = my_nx, requires_attention = False))

        index += 1
    
    # commit the changes
    session.commit()

    # close the session
    session.close()