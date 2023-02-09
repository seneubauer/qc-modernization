# import dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine.base import Engine
from os.path import join
import pandas as pd
import datetime

# instantiate the base
Base = declarative_base()

# connect to the mssql server
def db_connect(conn_str:str) -> dict:

    # create the engine
    engine = create_engine(conn_str, echo = False)

    # reflect the existing database into tables
    Base = automap_base()
    Base.prepare(engine, reflect = True)

    # assign the tables to variables
    dir_types = Base.classes.dir_types
    fixtures = Base.classes.fixtures
    parts = Base.classes.parts
    requests = Base.classes.requests
    programs = Base.classes.programs

    # return the object dictionary
    return {
        "engine": engine,
        "tables": [dir_types, fixtures, parts, requests, programs]
    }

# populate the database's tables
def db_populate(data_path:str, engine:Engine, tables:list):

    # import the cleaned data
    fixture_df = pd.read_csv(join(data_path, "fixture_data.csv"))
    part_df = pd.read_csv(join(data_path, "part_data.csv"))
    path_df = pd.read_csv(join(data_path, "program_data.csv"))

    # instantiate the database tables
    dir_types = tables[0]
    fixtures = tables[1]
    parts = tables[2]
    programs = tables[4]

    # create the session
    session = Session(engine)

    my_query = session.query(*[dir_types.id, dir_types.dir_type]).all()
    dir_dict = {}
    for t in my_query:
        dir_dict[t[1]] = t[0]

    # add data from the fixture dataframe
    for index, row in fixture_df.iterrows():

        my_id = str(row["id"])
        my_anchor_dir = dir_dict[str(row["anchor_dir"])]
        my_anchor_val = float(row["anchor_val"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])

        if session.query(fixtures.id).filter(fixtures.id == my_id).first() is None:
            session.add(fixtures(
                id = my_id,
                anchor_dir = my_anchor_dir,
                anchor_val = my_anchor_val,
                py = my_py,
                px = my_px,
                ny = my_ny,
                nx = my_nx,
                developer_notes = "",
                operator_notes = ""
            ))
        else:
            session.query(fixtures).filter(fixtures.id == my_id).update({
                "anchor_dir": my_anchor_dir,
                "anchor_val": my_anchor_val,
                "py": my_py,
                "px": my_px,
                "ny": my_ny,
                "nx": my_nx
            })

    # add data from the part dataframe
    for index, row in part_df.iterrows():

        my_id = str(row["id"])
        my_revision = str(row["revision"])
        my_item = str(row["item"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])

        if session.query(parts.id).filter(parts.id == my_id).first() is None:
            session.add(parts(
                id = my_id,
                revision = my_revision,
                item = my_item,
                py = my_py,
                px = my_px,
                ny = my_ny,
                nx = my_nx,
                developer_notes = "",
                operator_notes = ""
            ))
        else:
            session.query(parts).filter(parts.id == my_id).update({
                "py": my_py,
                "px": my_px,
                "ny": my_ny,
                "nx": my_nx,
                "revision": my_revision,
                "item": my_item
            })

    # add data from the paths/program dataframe
    index = 0
    for index, row in path_df.iterrows():

        my_name = str(row["name"])
        my_part = str(row["drawing"])
        my_fixture = str(row["fixture"])
        my_py = float(row["py"])
        my_px = float(row["px"])
        my_ny = float(row["ny"])
        my_nx = float(row["nx"])
        my_attn = int(row["requires_attn"])
        my_proof = int(row["requires_proof"])
        my_start = datetime.date(int(row["start_year"]), int(row["start_month"]), int(row["start_day"]))
        my_finish = datetime.date(int(row["finish_year"]), int(row["finish_month"]), int(row["finish_day"]))

        if session.query(*[programs.id, programs.name]).filter(programs.id == index).filter(programs.name == my_name).first() is None:
            session.add(programs(
                id = index,
                py = my_py,
                px = my_px,
                ny = my_ny,
                nx = my_nx,
                name = my_name,
                part = my_part,
                fixture = my_fixture,
                requires_attn = my_attn,
                requires_proof = my_proof,
                start_date = my_start,
                finish_date = my_finish,
                developer_notes = "",
                operator_notes = ""
            ))
        else:
            session.query(programs).filter(programs.id == my_id).update({
                "py": my_py,
                "px": my_px,
                "ny": my_ny,
                "nx": my_nx,
                "name": my_name,
                "part": my_part,
                "fixture": my_fixture,
                "requires_attn": my_attn,
                "requires_proof": my_proof,
                "start_date": my_start,
                "finish_date": my_finish
            })

        index += 1
    
    # commit the changes
    session.commit()

    # close the session
    session.close()