# import dependencies
from os import getcwd
from os.path import join

# import functions
from database_functions import db_create, db_populate

# import confidential values
from sys import path
path.insert(0, "..")
from config import db_path

# create the engine
engine = db_create(db_path)

# populate the databse
db_populate(join(getcwd(), "data"), engine)