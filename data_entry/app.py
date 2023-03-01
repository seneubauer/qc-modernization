# import dependencies for flask
from flask import Flask, render_template

# import dependencies for sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# import confidential information
from sys import path
path.insert(0, "..")
from config import pg_key, pg_db, pg_host, pg_port, pg_user

# create the sqlalchemy engine
engine = create_engine(f"postgresql://{pg_user}:{pg_key}@{pg_host}:{pg_port}/{pg_db}", pool_pre_ping = True, echo = False)

# reflect the database
base = automap_base()
base.prepare(engine, reflect = True)

# instantiate the database tables
characteristic_types = base.classes.characteristic_types
departments = base.classes.departments
employees = base.classes.employees
gauge_types = base.classes.gauge_types
gauges = base.classes.gauges
inspection_reports = base.classes.inspection_reports
location_types = base.classes.location_types
locations = base.classes.locations
machine_types = base.classes.machine_types
machines = base.classes.machines
parts = base.classes.parts
project_types = base.classes.project_types
projects = base.classes.projects
specification_types = base.classes.specification_types

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# data entry
@app.route("/data_entry")
def data_entry_route():
    return render_template("data_entry.html")

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)