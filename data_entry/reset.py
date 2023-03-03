# import dependencies for sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text

# import general dependencies
import pandas as pd
from os.path import join

# import confidential information
from sys import path
path.insert(0, "..")
from config import pg_key, pg_db, pg_host, pg_port, pg_user

# create the sqlalchemy engine
engine = create_engine(f"postgresql://{pg_user}:{pg_key}@{pg_host}:{pg_port}/{pg_db}", pool_pre_ping = True, echo = False)

# reset the database
with engine.connect() as con:
    with open("schema.sql") as file:
        query = text(file.read())
        con.execute(query)

# reflect the database
base = automap_base()
base.prepare(engine, reflect = True)

# instantiate the database tables
characteristic_types = base.classes.characteristic_types
departments = base.classes.departments
disposition_types = base.classes.disposition_types
employees = base.classes.employees
gauge_types = base.classes.gauge_types
gauges = base.classes.gauges
inspection_reports = base.classes.inspection_reports
job_orders = base.classes.job_orders
location_types = base.classes.location_types
locations = base.classes.locations
machine_types = base.classes.machine_types
machines = base.classes.machines
parts = base.classes.parts
project_types = base.classes.project_types
projects = base.classes.projects
purchase_orders = base.classes.purchase_orders
receiver_numbers = base.classes.receiver_numbers
specification_types = base.classes.specification_types
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
employee_projects = base.classes.employee_projects

# retrieve type data
characteristic_types_df = pd.read_csv(join("data", "characteristic_types.csv"))
disposition_types_df = pd.read_csv(join("data", "disposition_types.csv"))
gauge_types_df = pd.read_csv(join("data", "gauge_types.csv"))
location_types_df = pd.read_csv(join("data", "location_types.csv"))
machine_types_df = pd.read_csv(join("data", "machine_types.csv"))
project_types_df = pd.read_csv(join("data", "project_types.csv"))
specification_types_df = pd.read_csv(join("data", "specification_types.csv"))

# instantiate the session
session = Session(engine)

# populate type data
for i, r in characteristic_types_df.iterrows():
    session.add(characteristic_types(id = r["id"], is_gdt = r["is_gdt"]))
session.commit()

for i, r in disposition_types_df.iterrows():
    session.add(disposition_types(id = r["id"]))
session.commit()

for i, r in gauge_types_df.iterrows():
    session.add(gauge_types(id = r["id"]))
session.commit()

for i, r in location_types_df.iterrows():
    session.add(location_types(id = r["id"]))
session.commit()

for i, r in machine_types_df.iterrows():
    session.add(machine_types(id = r["id"]))
session.commit()

for i, r in project_types_df.iterrows():
    session.add(project_types(id = r["id"]))
session.commit()

for i, r in specification_types_df.iterrows():
    session.add(specification_types(id = r["id"]))
session.commit()

# retrieve record data
job_orders_df = pd.read_csv(join("data", "job_orders.csv"))
purchase_orders_df = pd.read_csv(join("data", "purchase_orders.csv"))
receiver_numbers_df = pd.read_csv(join("data", "receiver_numbers.csv"))
projects_df = pd.read_csv(join("data", "projects.csv"))
departments_df = pd.read_csv(join("data", "departments.csv"))
locations_df = pd.read_csv(join("data", "locations.csv"))
employees_df = pd.read_csv(join("data", "employees.csv"))
machines_df = pd.read_csv(join("data", "machines.csv"))
parts_df = pd.read_csv(join("data", "parts.csv"))
inspection_reports_df = pd.read_csv(join("data", "inspection_reports.csv"))
gauges_df = pd.read_csv(join("data", "gauges.csv"))

# populate record data
for i, r in job_orders_df.iterrows():
    session.add(job_orders(id = r["id"]))
session.commit()

for i, r in purchase_orders_df.iterrows():
    session.add(purchase_orders(id = r["id"]))
session.commit()

for i, r in receiver_numbers_df.iterrows():
    session.add(receiver_numbers(id = r["id"]))
session.commit()

for i, r in projects_df.iterrows():
    session.add(projects(id = r["id"], description = r["description"], day_started = r["day_started"], day_finished = r["day_finished"], project_type = r["project_type"]))
session.commit()

for i, r in departments_df.iterrows():
    session.add(departments(id = r["id"], description = r["description"]))
session.commit()

for i, r in locations_df.iterrows():
    session.add(locations(id = r["id"], description = r["description"], location_type_id = r["location_type_id"]))
session.commit()

for i, r in employees_df.iterrows():
    session.add(employees(id = r["id"], first_name = r["first_name"], last_name = r["last_name"], department_id = r["department_id"], location_id = r["location_id"]))
session.commit()

for i, r in machines_df.iterrows():
    session.add(machines(id = r["id"], machine_type_id = r["machine_type_id"], machine_location_id = r["machine_location_id"]))
session.commit()

for i, r in parts_df.iterrows():
    session.add(parts(drawing = r["drawing"], revision = r["revision"], item = r["item"]))
session.commit()

for i, r in inspection_reports_df.iterrows():
    session.add(inspection_reports(id = r["id"], day_started = r["day_started"], day_finished = r["day_finished"], job_order_id = r["job_order_id"], disposition = r["disposition"], part_id = r["part_id"]))
session.commit()

for i, r in gauges_df.iterrows():
    eid = ""
    lid = ""
    if r["employee_id"] == "None":
        eid = None
    else:
        eid = r["employee_id"]
    if r["location_id"] == "None":
        lid = None
    else:
        lid = r["location_id"]
    session.add(gauges(id = r["id"], last_calibrated = r["last_calibrated"], gauge_type_id = r["gauge_type_id"], employee_id = eid, location_id = lid))
session.commit()

# retrieve linking data
employee_projects_df = pd.read_csv(join("data", "employee_projects.csv"))
inspection_purchase_orders_df = pd.read_csv(join("data", "inspection_purchase_orders.csv"))
inspection_receiver_numbers_df = pd.read_csv(join("data", "inspection_receiver_numbers.csv"))

# populate linking data
for i, r in employee_projects_df.iterrows():
    session.add(employee_projects(employee_id = r["employee_id"], project_id = r["project_id"]))
session.commit()

for i, r in inspection_purchase_orders_df.iterrows():
    session.add(inspection_purchase_orders(inspection_id = r["inspection_id"], purchase_order_id = r["purchase_order_id"]))
session.commit()

for i, r in inspection_receiver_numbers_df.iterrows():
    session.add(inspection_receiver_numbers(inspection_id = r["inspection_id"], receiver_number_id = r["receiver_number_id"]))
session.commit()

# close the connection
session.close()