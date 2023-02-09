# import dependencies
from os import getcwd
from os.path import join

# import functions
from database_functions import db_connect, db_populate

# import confidential values
from sys import path
path.insert(0, "..")
from config import db_server, db_port, db_name, db_driver

# connect to the mssql server
obj_dict = db_connect(f"mssql+pyodbc://@{db_server}:{db_port}/{db_name}?driver={db_driver}")

engine = obj_dict["engine"]
tables = obj_dict["tables"]

# populate the database
db_populate(join(getcwd(), "data"), engine, tables)