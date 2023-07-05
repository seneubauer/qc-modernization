# import dependencies for sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text

# import general dependencies
import pandas as pd
from os.path import join
from math import isnan
import datetime

# register numpy
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
register_adapter(np.int64, AsIs)

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
inspection_records_lot_numbers = base.classes.inspection_records_lot_numbers
inspection_records_purchase_orders = base.classes.inspection_records_purchase_orders
inspections_job_numbers = base.classes.inspections_job_numbers
employee_projects = base.classes.employee_projects
inspection_schema_details = base.classes.inspection_schema_details
inspection_schemas = base.classes.inspection_schemas
deviations = base.classes.deviations
features = base.classes.features
inspections = base.classes.inspections
gauges = base.classes.gauges
parts = base.classes.parts
inspection_records = base.classes.inspection_records
machines = base.classes.machines
employees = base.classes.employees
locations = base.classes.locations
departments = base.classes.departments
projects = base.classes.projects
receiver_numbers = base.classes.receiver_numbers
purchase_orders = base.classes.purchase_orders
job_numbers = base.classes.job_numbers
suppliers = base.classes.suppliers
lot_numbers = base.classes.lot_numbers
dimension_types = base.classes.dimension_types
frequency_types = base.classes.frequency_types
material_types = base.classes.material_types
project_types = base.classes.project_types
specification_types = base.classes.specification_types
inspection_types = base.classes.inspection_types
gauge_types = base.classes.gauge_types
machine_types = base.classes.machine_types
location_types = base.classes.location_types
disposition_types = base.classes.disposition_types
deviation_types = base.classes.deviation_types

# instantiate the session
session = Session(engine)

# retrieve type data
inspection_types_df = pd.read_csv(join("data", "inspection_types.csv"))
frequency_types_df = pd.read_csv(join("data", "frequency_types.csv"))
material_types_df = pd.read_csv(join("data", "material_types.csv"))
project_types_df = pd.read_csv(join("data", "project_types.csv"))
specification_types_df = pd.read_csv(join("data", "specification_types.csv"))
dimension_types_df = pd.read_csv(join("data", "dimension_types.csv"))
gauge_types_df = pd.read_csv(join("data", "gauge_types.csv"))
machine_types_df = pd.read_csv(join("data", "machine_types.csv"))
location_types_df = pd.read_csv(join("data", "location_types.csv"))
disposition_types_df = pd.read_csv(join("data", "disposition_types.csv"))
deviation_types_df = pd.read_csv(join("data", "deviation_types.csv"))

# populate type data
for i, r in inspection_types_df.iterrows():
    session.add(inspection_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in frequency_types_df.iterrows():
    session.add(frequency_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in material_types_df.iterrows():
    session.add(material_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in project_types_df.iterrows():
    session.add(project_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in specification_types_df.iterrows():
    session.add(specification_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in dimension_types_df.iterrows():
    session.add(dimension_types(
        id = r["id"],
        name = r["name"],
        is_gdt = r["is_gdt"]))
session.commit()

for i, r in gauge_types_df.iterrows():
    session.add(gauge_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in machine_types_df.iterrows():
    session.add(machine_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in location_types_df.iterrows():
    session.add(location_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in disposition_types_df.iterrows():
    session.add(disposition_types(
        id = r["id"],
        name = r["name"]))
session.commit()

for i, r in deviation_types_df.iterrows():
    session.add(deviation_types(
        id = r["id"],
        name = r["name"]))
session.commit()

# retrieve record data
lot_numbers_df = pd.read_csv(join("data", "lot_numbers.csv"))
suppliers_df = pd.read_csv(join("data", "suppliers.csv"))
job_numbers_df = pd.read_csv(join("data", "job_numbers.csv"))
purchase_orders_df = pd.read_csv(join("data", "purchase_orders.csv"))
reciever_numbers_df = pd.read_csv(join("data", "receiver_numbers.csv"))
projects_df = pd.read_csv(join("data", "projects.csv"))
departments_df = pd.read_csv(join("data", "departments.csv"))
locations_df = pd.read_csv(join("data", "locations.csv"))
employees_df = pd.read_csv(join("data", "employees.csv"))
machines_df = pd.read_csv(join("data", "machines.csv"))
inspection_records_df = pd.read_csv(join("data", "inspection_records.csv"))
parts_df = pd.read_csv(join("data", "parts.csv"))
gauges_df = pd.read_csv(join("data", "gauges.csv"))
inspections_df = pd.read_csv(join("data", "inspections.csv"))
features_df = pd.read_csv(join("data", "features.csv"))
deviations_df = pd.read_csv(join("data", "deviations.csv"))
inspection_schemas_df = pd.read_csv(join("data", "inspection_schemas.csv"))
inspection_schema_details_df = pd.read_csv(join("data", "inspection_schema_details.csv"))

# populate record data
for i, r in lot_numbers_df.iterrows():
    session.add(lot_numbers(
        name = r["name"]))
session.commit()

for i, r in suppliers_df.iterrows():
    session.add(suppliers(
        name = r["name"]))
session.commit()

for i, r in job_numbers_df.iterrows():
    session.add(job_numbers(
        name = r["name"],
        full_inspect_interval = r["full_inspect_interval"],
        released_qty = r["released_qty"],
        completed_qty = r["completed_qty"]))
session.commit()

for i, r in purchase_orders_df.iterrows():
    session.add(purchase_orders(
        name = r["name"],
        supplier_id = r["supplier_id"]))
session.commit()

for i, r in reciever_numbers_df.iterrows():
    session.add(receiver_numbers(
        name = r["name"],
        received_qty = r["received_qty"],
        purchase_order_id = r["purchase_order_id"]))
session.commit()

for i, r in projects_df.iterrows():
    day_finished_val = r["day_finished"]
    if type(day_finished_val) is not str:
        day_finished_val = None
    session.add(projects(
        name = r["name"],
        description = r["description"],
        day_started = r["day_started"],
        day_finished = day_finished_val,
        project_type_id = r["project_type_id"]))
session.commit()

for i, r in departments_df.iterrows():
    session.add(departments(
        name = r["name"],
        description = r["description"]))
session.commit()

for i, r in locations_df.iterrows():
    session.add(locations(
        name = r["name"],
        description = r["description"],
        location_type_id = r["location_type_id"]))
session.commit()

for i, r in employees_df.iterrows():
    session.add(employees(
        id = r["id"],
        first_name = r["first_name"],
        last_name = r["last_name"],
        department_id = r["department_id"],
        location_id = r["location_id"]))
session.commit()

for i, r in machines_df.iterrows():
    session.add(machines(
        name = r["name"],
        machine_type_id = r["machine_type_id"],
        machine_location_id = r["machine_location_id"]))
session.commit()

for i, r in inspection_records_df.iterrows():
    employee_id_val = r["employee_id"]
    if isnan(employee_id_val):
        employee_id_val = None
    session.add(inspection_records(
        material_type_id = r["material_type_id"],
        employee_id = employee_id_val))
session.commit()

for i, r in parts_df.iterrows():
    session.add(parts(
        drawing = r["drawing"],
        revision = r["revision"],
        item = r["item"],
        ))
session.commit()

for i, r in gauges_df.iterrows():

    employee_id_val = r["employee_id"]
    location_id_val = r["location_id"]

    if isnan(employee_id_val):
        employee_id_val = None
    if isnan(location_id_val):
        location_id_val = None

    session.add(gauges(
        name = r["name"],
        last_calibrated = r["last_calibrated"],
        gauge_type_id = r["gauge_type_id"],
        employee_id = employee_id_val,
        location_id = location_id_val))
session.commit()

for i, r in inspections_df.iterrows():
    session.add(inspections(
        part_index = r["part_index"],
        datetime_measured = r["datetime_measured"],
        inspection_record_id = r["inspection_record_id"],
        part_id = r["part_id"],
        employee_id = r["employee_id"],
        inspection_type_id = r["inspection_type_id"],
        disposition_id = r["disposition_id"]))
session.commit()

for i, r in features_df.iterrows():

    measured_val = r["measured"]
    if isnan(measured_val):
        measured_val = None

    session.add(features(
        name = r["name"],
        nominal = r["nominal"],
        usl = r["usl"],
        lsl = r["lsl"],
        measured = measured_val,
        precision = r["precision"],
        inspection_id = r["inspection_id"],
        specification_type_id = r["specification_type_id"],
        dimension_type_id = r["dimension_type_id"],
        frequency_type_id = r["frequency_type_id"],
        gauge_id = r["gauge_id"]))
session.commit()

for i, r in deviations_df.iterrows():
    notes = ""
    date_implemented = str(r["date_implemented"])
    if not r["notes"] == "":
        notes = str(r["notes"])
    session.add(deviations(
        nominal = r["nominal"],
        usl = r["usl"],
        lsl = r["lsl"],
        precision = r["precision"],
        date_implemented = datetime.datetime.strptime(date_implemented, "%m/%d/%Y").date(),
        notes = notes,
        deviation_type_id = r["deviation_type_id"],
        employee_id = r["employee_id"],
        feature_id = r["feature_id"]))
session.commit()

for i, r in inspection_schemas_df.iterrows():
    session.add(inspection_schemas(
        is_locked = r["is_locked"],
        part_id = r["part_id"]))
session.commit()

for i, r in inspection_schema_details_df.iterrows():
    session.add(inspection_schema_details(
        name = r["name"],
        nominal = r["nominal"],
        usl = r["usl"],
        lsl = r["lsl"],
        precision = r["precision"],
        specification_type_id = r["specification_type_id"],
        dimension_type_id = r["dimension_type_id"],
        frequency_type_id = r["frequency_type_id"],
        gauge_type_id = r["gauge_type_id"],
        schema_id = r["schema_id"]))
session.commit()

# retrieve linking data
employee_projects_df = pd.read_csv(join("data", "employee_projects.csv"))
inspections_job_numbers_df = pd.read_csv(join("data", "inspections_job_numbers.csv"))
inspection_records_purchase_orders_df = pd.read_csv(join("data", "inspection_records_purchase_orders.csv"))
inspection_records_lots_df = pd.read_csv(join("data", "inspection_records_lot_numbers.csv"))

# populate linking data
for i, r in employee_projects_df.iterrows():
    session.add(employee_projects(
        employee_id = r["employee_id"],
        project_id = r["project_id"]))
session.commit()

for i, r in inspections_job_numbers_df.iterrows():
    session.add(inspections_job_numbers(
        inspection_id = r["inspection_id"],
        job_number_id = r["job_number_id"]))
session.commit()

for i, r in inspection_records_purchase_orders_df.iterrows():
    session.add(inspection_records_purchase_orders(
        inspection_record_id = r["inspection_record_id"],
        purchase_order_id = r["purchase_order_id"]))
session.commit()

for i, r in inspection_records_lots_df.iterrows():
    session.add(inspection_records_lot_numbers(
        inspection_record_id = r["inspection_record_id"],
        lot_number_id = r["lot_number_id"]))
session.commit()

# close the connection
session.close()