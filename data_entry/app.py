# import dependencies for flask
from flask import Flask, render_template, request

# import dependencies for sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, and_, or_, func

# import general dependencies
import json
import datetime
import pandas as pd
from math import isnan
from os.path import join, isfile, splitext
from os import listdir, remove

# import confidential information
from sys import path
path.insert(0, "..")
from config import pg_key, pg_db, pg_host, pg_port, pg_user, char_schema_destination

# create the sqlalchemy engine
engine = create_engine(f"postgresql://{pg_user}:{pg_key}@{pg_host}:{pg_port}/{pg_db}", pool_pre_ping = True, echo = False)

# reflect the database
base = automap_base()
base.prepare(engine, reflect = True)

# instantiate the database tables
disposition_types = base.classes.disposition_types
location_types = base.classes.location_types
machine_types = base.classes.machine_types
gauge_types = base.classes.gauge_types
characteristic_types = base.classes.characteristic_types
specification_types = base.classes.specification_types
project_types = base.classes.project_types
material_types = base.classes.material_types
frequency_types = base.classes.frequency_types
lot_numbers = base.classes.lot_numbers
suppliers = base.classes.suppliers
job_orders = base.classes.job_orders
purchase_orders = base.classes.purchase_orders
receiver_numbers = base.classes.receiver_numbers
projects = base.classes.projects
departments = base.classes.departments
locations = base.classes.locations
employees = base.classes.employees
machines = base.classes.machines
inspection_reports = base.classes.inspection_reports
parts = base.classes.parts
gauges = base.classes.gauges
checks = base.classes.checks
characteristics = base.classes.characteristics
deviations = base.classes.deviations
employee_projects = base.classes.employee_projects
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
inspection_lot_numbers = base.classes.inspection_lot_numbers

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# --------------------------------------------------

#region page navigation

@app.route("/data_entry/")
def data_entry():
    return render_template("data_entry.html")

#endregion

# --------------------------------------------------

#region get enumerations

@app.route("/get_all_gauges/")
def get_all_gauges():

    # define the requested columns
    columns = [
        gauges.id,
        gauges.name,
        gauges.last_calibrated,
        gauges.gauge_type_id,
        gauges.employee_id,
        gauges.location_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns).order_by(gauges.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name, last_calibrated, gauge_type_id, employee_id, location_id in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "last_calibrated": last_calibrated,
                    "gauge_type_id": gauge_type_id,
                    "employee_id": employee_id,
                    "location_id": location_id
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }

        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'gauges'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_gauge_types/")
def get_all_gauge_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(gauge_types.id, gauge_types.name).order_by(gauge_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'gauge_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_specification_types/")
def get_all_specification_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(specification_types.id, specification_types.name).order_by(specification_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'specification_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_frequency_types/")
def get_all_frequency_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(frequency_types.id, frequency_types.name).order_by(frequency_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'frequency_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_characteristic_types/")
def get_all_characteristic_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(characteristic_types.id, characteristic_types.name).order_by(characteristic_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'characteristic_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_employees/")
def get_all_employees():

    # define the requested columns
    columns = [
        employees.id,
        employees.first_name,
        employees.last_name,
        employees.department_id,
        employees.location_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns).order_by(employees.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, first_name, last_name, department_id, location_id in results:
                output_arr.append({
                    "id": id,
                    "name": f"{last_name}, {first_name}",
                    "department_id": department_id,
                    "location_id": location_id
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'employees'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_disposition_types/")
def get_all_disposition_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(disposition_types.id, disposition_types.name).order_by(disposition_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'disposition_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_parts/")
def get_all_parts():

    # define the requested columns
    columns = [
        parts.id,
        parts.drawing,
        parts.revision,
        parts.item
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns).order_by(parts.drawing.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, drawing, revision, item in results:
                output_arr.append({
                    "id": id,
                    "drawing": drawing,
                    "revision": revision.upper(),
                    "item": item
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_job_orders/")
def get_all_job_orders():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_orders.id, job_orders.name).order_by(job_orders.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'job_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_material_types/")
def get_all_material_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(material_types.id, material_types.name).order_by(material_types.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'material_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_suppliers/")
def get_all_suppliers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(suppliers.id, suppliers.name).order_by(suppliers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'suppliers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_receiver_numbers/")
def get_all_receiver_numbers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(receiver_numbers.id, receiver_numbers.name).order_by(receiver_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no record found in 'receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_purchase_orders/")
def get_all_purchase_orders():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id, purchase_orders.name, purchase_orders.supplier_id).order_by(purchase_orders.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name, supplier_id in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "supplier_id": supplier_id
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/get_all_lot_numbers/")
def get_all_lot_numbers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(lot_numbers.id, lot_numbers.name).order_by(lot_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no records found in 'purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

#endregion

# --------------------------------------------------

#region data entry - inspection reports

@app.route("/data_entry/get_filtered_parts/", methods = ["POST"])
def data_entry_get_filtered_parts():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item_search_term = form_data["item"]
    drawing_search_term = form_data["drawing"]

    try:

        # start the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.item, parts.drawing)\
            .filter(parts.item.ilike(f"%{item_search_term}%"))\
            .filter(parts.drawing.ilike(f"%{drawing_search_term}%"))\
            .order_by(parts.drawing.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, item, drawing in results:
                output_arr.append({
                    "id": id,
                    "item": item,
                    "drawing": drawing
                })
            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no matching parts found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/get_filtered_characteristic_schemas/", methods = ["POST"])
def data_entry_get_filtered_characteristic_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"]).lower()

    try:
        filtered_list = list(filter(lambda item:
                                isfile(join(char_schema_destination, item))
                                and item[-len(".csv"):].lower() == ".csv"
                                and search_term in item.lower(), listdir(char_schema_destination)))
        schema_list = [splitext(x)[0] for x in filtered_list]
        schema_list.sort()
    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

    if len(schema_list) > 0:
        return {
            "status": "ok_func",
            "response": schema_list
        }
    else:
        return {
            "status": "ok_log",
            "response": "no matching schema files found"
        }

@app.route("/data_entry/get_filtered_inspection_reports/", methods = ["POST"])
def data_entry_get_filtered_inspection_reports():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = int(form_data["part_id"])
    job_order_id = int(form_data["job_order_id"])
    started_after = datetime.date(form_data["start_year"], form_data["start_month"], form_data["start_day"])
    finished_before = datetime.date(form_data["finish_year"], form_data["finish_month"], form_data["finish_day"])

    # define the required fields
    columns = [
        inspection_reports.id,
        inspection_reports.full_inspect_interval,
        inspection_reports.released_qty,
        inspection_reports.completed_qty,
        parts.id,
        parts.item,
        parts.drawing,
        parts.revision,
        job_orders.id,
        job_orders.name,
        inspection_reports.disposition_id,
        inspection_reports.material_type_id,
        inspection_reports.employee_id,
        inspection_reports.supplier_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns).distinct(parts.item, parts.drawing, parts.revision)\
            .join(checks, (checks.inspection_id == inspection_reports.id))\
            .join(parts, (checks.part_id == parts.id))\
            .join(job_orders, (inspection_reports.job_order_id == job_orders.id), isouter = True)\
            .filter(checks.datetime_measured >= started_after)\
            .filter(or_(checks.datetime_measured <= finished_before, checks.datetime_measured == None))

        # additional filtering
        if part_id > 0:
            results = results.filter(parts.id == part_id)
        if job_order_id > 0:
            results = results.filter(job_orders.id == job_order_id)

        # convert to list of tuples
        results = results.order_by(parts.drawing.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for inspection_id, full_inspect_interval, released_qty, completed_qty, part_id, item, drawing, revision, job_order_id, job_order, disposition_type_id, material_type_id, employee_id, supplier_id in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "full_inspect_interval": full_inspect_interval,
                    "released_qty": released_qty,
                    "completed_qty": completed_qty,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "revision": revision.upper(),
                    "job_order_id": job_order_id,
                    "job_order": job_order,
                    "disposition_type_id": disposition_type_id,
                    "material_type_id": material_type_id,
                    "employee_id": employee_id,
                    "supplier_id": supplier_id
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no matching records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - characteristic display

@app.route("/data_entry/get_filter_selector_lists/", methods = ["POST"])
def data_entry_get_filter_selector_lists():
    
    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])

    try:

        # open the database session
        session = Session(engine)

        # frequency type list
        frequency_types_query = session.query(frequency_types.id, frequency_types.name)\
            .join(characteristics, (characteristics.frequency_type_id == frequency_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(frequency_types.name.asc()).distinct(frequency_types.name).all()

        # check id list
        check_ids_query = session.query(checks.id)\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(checks.id.asc()).distinct(checks.id).all()

        # revisions list
        revisions_query = session.query(parts.id, parts.revision)\
            .join(checks, (checks.part_id == part_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(parts.revision.asc()).distinct(parts.revision).all()

        # part indices list
        part_indices_query = session.query(checks.part_index)\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(checks.part_index.asc()).distinct(checks.part_index).all()

        # inspectors list
        inspectors_query = session.query(employees.id, employees.first_name, employees.last_name)\
            .join(checks, (checks.employee_id == employees.id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(employees.last_name.asc()).distinct(employees.first_name, employees.last_name).all()

        # gauges list
        gauges_query = session.query(gauges.id, gauges.name)\
            .join(characteristics, (characteristics.gauge_id == gauges.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(gauges.name.asc()).distinct(gauges.name).all()

        # gauges types list
        gauge_types_query = session.query(gauge_types.id, gauge_types.name)\
            .join(gauges, (gauges.gauge_type_id == gauge_types.id))\
            .join(characteristics, (characteristics.gauge_id == gauges.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(gauge_types.name.asc()).distinct(gauge_types.name).all()

        # specification types list
        specification_types_query = session.query(specification_types.id, specification_types.name)\
            .join(characteristics, (characteristics.specification_type_id == specification_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(specification_types.name.asc()).distinct(specification_types.name).all()

        # characteristic types list
        characteristic_types_query = session.query(characteristic_types.id, characteristic_types.name)\
            .join(characteristics, (characteristics.characteristic_type_id == characteristic_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(and_(checks.inspection_id == inspection_id, checks.part_id == part_id))\
            .order_by(characteristic_types.name.asc()).distinct(characteristic_types.name).all()

        # close the database session
        session.close()

        # return the results
        if len(frequency_types_query) > 0 and len(check_ids_query) > 0 and len(revisions_query) > 0 and len(inspectors_query) > 0 and len(gauges_query) > 0 and len(gauge_types_query) > 0 and len(specification_types_query) > 0 and len(characteristic_types_query) > 0:

            frequency_types_list = []
            for id, name in frequency_types_query:
                frequency_types_list.append({
                    "id": id,
                    "name": name
                })

            check_ids_list = []
            for id in check_ids_query:
                check_ids_list.append({
                    "id": id[0],
                    "value": id[0]
                })

            revisions_list = []
            for id, revision in revisions_query:
                revisions_list.append({
                    "id": id,
                    "revision": revision.upper()
                })

            part_indices_list = []
            for id in part_indices_query:
                part_indices_list.append({
                    "id": id[0],
                    "value": id[0]
                })

            inspectors_list = []
            for id, first_name, last_name in inspectors_query:
                inspectors_list.append({
                    "id": id,
                    "name": f"{last_name}, {first_name}"
                })

            gauges_list = []
            for id, name in gauges_query:
                gauges_list.append({
                    "id": id,
                    "name": name
                })

            gauge_types_list = []
            for id, name in gauge_types_query:
                gauge_types_list.append({
                    "id": id,
                    "name": name
                })

            specification_types_list = []
            for id, name in specification_types_query:
                specification_types_list.append({
                    "id": id,
                    "name": name
                })

            characteristic_types_list = []
            for id, name in characteristic_types_query:
                characteristic_types_list.append({
                    "id": id,
                    "name": name
                })

            # return the data object
            return {
                "status": "ok_func",
                "response": {
                    "frequency_types": frequency_types_list,
                    "check_ids": check_ids_list,
                    "revisions": revisions_list,
                    "part_indices": part_indices_list,
                    "inspectors": inspectors_list,
                    "gauges": gauges_list,
                    "gauge_types": gauge_types_list,
                    "specification_types": specification_types_list,
                    "characteristic_types": characteristic_types_list
                }
            }
        else:
            return {
                "status": "ok_log",
                "response": "queries returned null values"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/get_filtered_inspection_report_part_characteristics/", methods = ["POST"])
def data_entry_get_filtered_inspection_report_part_characteristics():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["identity"]["inspection_id"])
    part_id = int(form_data["identity"]["part_id"])
    check_id = int(form_data["content"]["check_id"])
    frequency_type_id = int(form_data["content"]["frequency_type_id"])
    revision = form_data["content"]["revision"]
    name = form_data["content"]["name"]
    has_deviations = int(form_data["content"]["has_deviations"])
    inspector_id = int(form_data["content"]["inspector_id"])
    gauge_id = int(form_data["content"]["gauge_id"])
    gauge_type_id = int(form_data["content"]["gauge_type_id"])
    specification_type_id = int(form_data["content"]["specification_type_id"])
    characteristic_type_id = int(form_data["content"]["characteristic_type_id"])

    # define the columns
    columns = [
        checks.id,
        checks.part_index,
        parts.revision,
        characteristics.name,
        characteristics.nominal,
        characteristics.usl,
        characteristics.lsl,
        characteristics.measured,
        characteristics.precision,
        checks.employee_id,
        gauges.id,
        gauge_types.name,
        specification_types.name,
        characteristic_types.name,
        frequency_types.name,
        characteristics.id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(gauges, (characteristics.gauge_id == gauges.id))\
            .join(gauge_types, (gauges.gauge_type_id == gauge_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .join(inspection_reports, (checks.inspection_id == inspection_reports.id))\
            .join(specification_types, (characteristics.specification_type_id == specification_types.id))\
            .join(characteristic_types, (characteristics.characteristic_type_id == characteristic_types.id))\
            .join(frequency_types, (characteristics.frequency_type_id == frequency_types.id))\
            .filter(and_(inspection_reports.id == inspection_id, parts.id == part_id))\
            .filter(characteristics.name.ilike(f"%{name}%"))\
            .filter(parts.revision.ilike(f"%{revision}%"))

        if check_id > 0:
            results = results.filter(checks.id == check_id)
        if frequency_type_id > 0:
            results = results.filter(characteristics.frequency_type_id == frequency_type_id)
        if has_deviations > 0:
            results = results.filter(characteristics.id.in_(session.query(deviations.characteristic_id)))
        if inspector_id > 0:
            results = results.filter(checks.employee_id == inspector_id)
        if gauge_id > 0:
            results = results.filter(characteristics.gauge_id == gauge_id)
        if gauge_type_id > 0:
            results = results.filter(gauges.gauge_type_id == gauge_type_id)
        if specification_type_id > 0:
            results = results.filter(characteristics.specification_type_id == specification_type_id)
        if characteristic_type_id > 0:
            results = results.filter(characteristics.characteristic_type_id == characteristic_type_id)

        # convert to a list
        characteristic_list = results\
            .order_by(checks.id.asc(), checks.part_id.asc(), parts.revision.asc(), characteristics.id.asc(), characteristics.name.asc()).all()

        # get the list of characteristics that have deviations
        deviations_list = []
        for id in session.query(deviations.characteristic_id).all():
            deviations_list.append(id[0])

        # get the list of inspectors
        inspectors_list = session.query(employees.id, employees.first_name, employees.last_name).order_by(employees.last_name.asc()).all()

        # get the list of gauges
        gauges_list = session.query(gauges.id, gauges.name).order_by(gauges.name.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(characteristic_list) > 0 and len(inspectors_list) > 0 and len(gauges_list) > 0:

            # assemble characteristics output
            output_characteristics_list = []
            for check_id, part_index, revision, name, nominal, usl, lsl, measured, precision, employee_id, gauge_id, gauge_type, specification_type, characteristic_type, frequency_type, characteristic_id in characteristic_list:

                # parse to floats
                nominal_flt = round(float(nominal), precision)
                usl_flt = round(float(usl), precision)
                lsl_flt = round(float(lsl), precision)

                # evaluate measurements
                state = "n/a"
                measured_flt = 0
                if measured is None:
                    measured_flt = None
                else:
                    measured_flt = round(float(measured), precision)
                    if usl_flt >= measured_flt and lsl_flt <= measured_flt:
                        state = "pass"
                    else:
                        state = "fail"

                output_characteristics_list.append({
                    "has_deviations": characteristic_id in deviations_list,
                    "check_id": check_id,
                    "part_index": part_index,
                    "revision": revision.upper(),
                    "name": name,
                    "nominal": nominal_flt,
                    "usl": usl_flt,
                    "lsl": lsl_flt,
                    "measured": measured_flt,
                    "precision": precision,
                    "employee_id": employee_id,
                    "gauge_id": gauge_id,
                    "gauge_type": gauge_type,
                    "specification_type": specification_type,
                    "characteristic_type": characteristic_type,
                    "frequency_type": frequency_type,
                    "state": state
                })

            # assemble inspectors output
            output_inspectors_list = []
            for id, first_name, last_name in inspectors_list:
                output_inspectors_list.append({
                    "id": id,
                    "name": f"{last_name}, {first_name}"
                })

            # assemble gauges output
            output_gauges_list = []
            for id, name in gauges_list:
                output_gauges_list.append({
                    "id": id,
                    "name": name
                })

            # return the data object
            return {
                "status": "ok_func",
                "response": {
                    "characteristics": output_characteristics_list,
                    "inspectors": output_inspectors_list,
                    "gauges": output_gauges_list
                }
            }
        else:
            return {
                "status": "ok_log",
                "response": "no matching characteristics found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/commit_characteristic_data/<int:report_id>/", methods = ["POST"])
def data_entry_commit_characteristic_data(report_id:int):

    # handle a null report id
    if report_id == -1:
        return {
            "status": "ok_alert",
            "response": "report id is null"
        }

    # store raw incoming data into new list
    char_data = {}
    for k, v in request.form.items():

        key_split = k.split("-")
        char_id = int(key_split[0])
        field = str(key_split[1])

        if char_id in char_data:
            char_data[char_id].append({
                field: v
            })
        else:
            char_data[char_id] = [{
                field: v
            }]

    # proceed if the dictionary has contents
    if len(char_data) > 0:
        try:

            # open the session
            session = Session(engine)

            affected_count = 0
            for k, v in char_data.items():

                # get the part id
                part_id = session.query(inspection_reports.part_id)\
                    .join(parts, (parts.id == inspection_reports.part_id))\
                    .filter(inspection_reports.id == report_id).first()[0]

                if part_id is not None:
                    results = session.query(characteristics)\
                        .filter(characteristics.id == k)\
                        .filter(characteristics.part_id == part_id)

                    row_affected = 0
                    for d in v:
                        key = list(d.keys())[0]
                        value = d[key]
                        row_affected = results.update({ key: value })
                    if row_affected > 0:
                        affected_count += 1
                else:
                    return {
                        "status": "ok_alert",
                        "response": "no part id found"
                    }

            # commit the changes
            session.commit()

            # close the session
            session.close()

            # return the result
            if affected_count > 0:
                return {
                    "status": "ok",
                    "response": {
                        "rows_affected": affected_count
                    }
                }
            else:
                return {
                    "status": "ok_alert",
                    "response": "no rows affected"
                }

        except SQLAlchemyError as e:
            error_msg = str(e.__dict__["orig"])
            return {
                "status": "err_log",
                "response": error_msg
            }

    else:
        return {
            "status": "ok_alert",
            "response": "no data passed to flask server"
        }

#endregion

#region data entry - metadata

@app.route("/data_entry/save_metadata/", methods = ["POST"])
def data_entry_save_metadata():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = form_data["identity"]["part_id"]
    inspection_id = form_data["identity"]["inspection_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the report/part combination exists
        results = session.query(inspection_reports.id).distinct(inspection_reports.id)\
            .join(checks, (checks.inspection_id == inspection_reports.id))\
            .filter(and_(checks.part_id == part_id, checks.inspection_id == inspection_id)).all()
        if len(results) == 0:
            return {
                "status": "ok_log",
                "response": "no matching inspection report and part found"
            }

        # define the changes
        results = session.query(inspection_reports).filter(inspection_reports.id == inspection_id)
        is_affected = 0
        for k, v in form_data["content"].items():
            is_affected = results.update({ k: v })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the response
        if is_affected > 0:
            return {
                "status": "ok_func",
                "response": "table 'inspection_reports' successfully updated"
            }
        else:
            return {
                "status": "ok_alert",
                "response": "no records in 'inspection_reports' updated"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

#endregion

#region data entry - receiver numbers

@app.route("/data_entry/get_filtered_receiver_numbers/", methods = ["POST"])
def data_entry_get_filtered_receiver_numbers():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(receiver_numbers.id, receiver_numbers.name)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(receiver_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(receiver_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/assign_receiver_number_association/", methods = ["POST"])
def data_entry_assign_receiver_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]
    inspection_id = form_data["inspection_id"]
    receiver_number_id = form_data["receiver_number_id"]

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        results = session.query(inspection_receiver_numbers.inspection_id)\
            .filter(and_(inspection_receiver_numbers.inspection_id == inspection_id, inspection_receiver_numbers.receiver_number_id == receiver_number_id)).all()

        # logic gate
        if len(results) > 0:
            return {
                "status": "ok_alert",
                "response": "this receiver number association already exists"
            }

        # add the new association
        session.add(inspection_receiver_numbers(inspection_id = inspection_id, receiver_number_id = receiver_number_id))
        session.commit()

        # get the new list
        results = session.query(receiver_numbers.id, receiver_numbers.name)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(receiver_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(receiver_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/remove_receiver_number_association/", methods = ["POST"])
def data_entry_remove_receiver_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    receiver_number_id = form_data["receiver_number_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        results = session.query(inspection_receiver_numbers)\
            .filter(and_(inspection_receiver_numbers.inspection_id == inspection_id, inspection_receiver_numbers.receiver_number_id == receiver_number_id))\
            .delete()

        # logic gate
        if results == 0:
            return {
                "status": "ok_alert",
                "response": "no records deleted; none matched the provided criteria"
            }
        else:
            session.commit()

        # get the new list
        results = session.query(receiver_numbers.id, receiver_numbers.name)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(receiver_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(receiver_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

#endregion

#region data entry - purchase orders

@app.route("/data_entry/get_filtered_purchase_orders/", methods = ["POST"])
def data_entry_get_filtered_purchase_orders():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id, purchase_orders.name)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(purchase_orders.name.ilike(f"%{search_term}%"))\
            .order_by(purchase_orders.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/assign_purchase_order_association/", methods = ["POST"])
def data_entry_assign_assign_purchase_order_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]
    inspection_id = form_data["inspection_id"]
    purchase_order_id = form_data["purchase_order_id"]

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        results = session.query(inspection_purchase_orders.inspection_id)\
            .filter(and_(inspection_purchase_orders.inspection_id == inspection_id, inspection_purchase_orders.purchase_order_id == purchase_order_id)).all()

        # logic gate
        if len(results) > 0:
            return {
                "status": "ok_alert",
                "response": "this purchase order association already exists"
            }

        # add the new association
        session.add(inspection_purchase_orders(inspection_id = inspection_id, purchase_order_id = purchase_order_id))
        session.commit()

        # get the new list
        results = session.query(purchase_orders.id, purchase_orders.name)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(purchase_orders.name.ilike(f"%{search_term}%"))\
            .order_by(purchase_orders.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/remove_purchase_order_association/", methods = ["POST"])
def data_entry_remove_remove_purchase_order_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    purchase_order_id = form_data["purchase_order_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        results = session.query(inspection_purchase_orders)\
            .filter(and_(inspection_purchase_orders.inspection_id == inspection_id, inspection_purchase_orders.purchase_order_id == purchase_order_id))\
            .delete()

        # logic gate
        if results == 0:
            return {
                "status": "ok_alert",
                "response": "no records deleted; none matched the provided criteria"
            }
        else:
            session.commit()

        # get the new list
        results = session.query(purchase_orders.id, purchase_orders.name)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(purchase_orders.name.ilike(f"%{search_term}%"))\
            .order_by(purchase_orders.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

#endregion

#region data entry - lot numbers

@app.route("/data_entry/get_filtered_lot_numbers/", methods = ["POST"])
def data_entry_get_filtered_lot_numbers():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(lot_numbers.id, lot_numbers.name)\
            .join(inspection_lot_numbers, (lot_numbers.id == inspection_lot_numbers.lot_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_lot_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(lot_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(lot_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'lot_numbers', and 'inspection_lot_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/assign_lot_number_association/", methods = ["POST"])
def data_entry_assign_lot_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]
    inspection_id = form_data["inspection_id"]
    lot_number_id = form_data["lot_number_id"]

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        results = session.query(inspection_lot_numbers.inspection_id)\
            .filter(and_(inspection_lot_numbers.inspection_id == inspection_id, inspection_lot_numbers.lot_number_id == lot_number_id)).all()

        # logic gate
        if len(results) > 0:
            return {
                "status": "ok_alert",
                "response": "this lot number association already exists"
            }

        # add the new association
        session.add(inspection_lot_numbers(inspection_id = inspection_id, lot_number_id = lot_number_id))
        session.commit()

        # get the new list
        results = session.query(lot_numbers.id, lot_numbers.name)\
            .join(inspection_lot_numbers, (lot_numbers.id == inspection_lot_numbers.lot_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_lot_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(lot_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(lot_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'lot_numbers', and 'inspection_lot_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/data_entry/remove_lot_number_association/", methods = ["POST"])
def data_entry_remove_lot_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    lot_number_id = form_data["lot_number_id"]
    search_term = form_data["search_term"]

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        results = session.query(inspection_lot_numbers)\
            .filter(and_(inspection_lot_numbers.inspection_id == inspection_id, inspection_lot_numbers.lot_number_id == lot_number_id))\
            .delete()

        # logic gate
        if results == 0:
            return {
                "status": "ok_alert",
                "response": "no records deleted; none matched the provided criteria"
            }
        else:
            session.commit()

        # get the new list
        results = session.query(lot_numbers.id, lot_numbers.name)\
            .join(inspection_lot_numbers, (lot_numbers.id == inspection_lot_numbers.lot_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_lot_numbers.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(lot_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(lot_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok_func",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "no connection found between 'inspection_reports', 'lot_numbers', and 'inspection_lot_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

#endregion

# --------------------------------------------------















#region data entry - report controls

@app.route("/data_entry/create_new_inspection_report/", methods = ["POST"])
def data_entry_create_new_inspection_report():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item = form_data["item"]
    drawing = form_data["drawing"]
    revision = form_data["revision"]

    # handle null values
    if revision == "":
        return {
            "status": "ok_alert",
            "response": "revision must be defined"
        }

    try:

        # open the database session
        session = Session(engine)

        # make sure the inputs exist in the database
        results = session.query(parts.id)\
            .filter(func.lower(parts.item) == item)\
            .filter(func.lower(parts.drawing) == drawing)\
            .filter(func.lower(parts.revision) == revision).first()

        if results is None:
            return {
                "status": "ok_alt",
                "response": f"referenced part ({item}, {drawing}, {revision}) does not exist in the database"
            }

        # define the associated part id
        part_id = results[0]

        # check if this part is already associated with an inspection report
        results = session.query(inspection_reports.id)\
            .filter(inspection_reports.part_id == part_id).first()
        if results is not None:
            return {
                "status": "ok_alt",
                "response": f"referenced part ({item}, {drawing}, {revision}) is already associated with an inspection report"
            }

        # define the new inspection report id
        new_id = len(session.query(inspection_reports.id).order_by(inspection_reports.id.asc()).all())

        # get today's date
        dt_now = datetime.datetime.now()
        today = datetime.date(dt_now.year, dt_now.month, dt_now.day)

        # add the record
        session.add(inspection_reports(
            id = new_id,
            day_started = today,
            full_inspect_qty = 0,
            full_inspect_qty_type = "custom",
            released_qty = 0,
            released_qty_type = "custom",
            completed_qty = 0,
            completed_qty_type = "custom",
            material_type_id = "aluminum",
            disposition = "incomplete",
            part_id = part_id))

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        return {
            "status": "ok",
            "response": f"new inspection report (ID: {new_id}) added"
        }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/save_inspection_report_metadata/", methods = ["POST"])
def data_entry_save_inspection_report_metadata():

    # interpret the form data
    form_data = json.loads(request.data)

    # get the ids
    part_id = form_data["ident"]["part_id"]
    report_id = form_data["ident"]["report_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the report/part combination exists
        results = session.query(inspection_reports.id)\
            .join(parts, (inspection_reports.part_id == parts.id))\
            .filter(inspection_reports.id == report_id)\
            .filter(parts.id == part_id).all()
        if (len(results)) == 0:
            return {
                "status": "ok_alt",
                "response": "no matching inspection report and part"
            }

        results = session.query(inspection_reports).filter(inspection_reports.id == report_id)

        is_affected = 0
        for k, v in form_data["info"].items():
            is_affected = results.update({ k: v })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        if is_affected > 0:
            return {
                "status": "ok",
                "response": "table 'inspection_reports' successfully updated"
            }
        else:
            return {
                "status": "ok",
                "response": "no records updated in 'inspection_reports'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - existing reports

@app.route("/data_entry/get_filtered_inspection_reports_old/", methods = ["POST"])
def data_entry_get_filtered_inspection_reports_old():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item_number = form_data["item"]
    drawing = form_data["drawing"]
    job_order = form_data["job_order"]
    started_after = datetime.date(form_data["start_year"], form_data["start_month"], form_data["start_day"])
    finished_before = datetime.date(form_data["finish_year"], form_data["finish_month"], form_data["finish_day"])

    # define the required fields
    columns = [
        parts.id,
        parts.item,
        parts.drawing,
        parts.revision,
        inspection_reports.id,
        inspection_reports.job_order_id,
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(inspection_reports, (inspection_reports.part_id == parts.id))\
            .join(characteristics, (characteristics.part_id == parts.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .filter(checks.date_measured >= started_after)\
            .filter(or_(checks.date_measured <= finished_before, checks.date_measured == None))\
            .filter(parts.item.ilike(f"%{item_number}%"))\
            .filter(parts.drawing.ilike(f"%{drawing}%"))\
            .filter(inspection_reports.job_order_id.ilike(f"%{job_order}%"))\
            .order_by(parts.drawing.asc()).all()

        # close the database session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

    # return the results
    if len(results) > 0:
        output_arr = []
        for part_id, item, drawing, revision, report_id, job_order_id in results:
            output_arr.append({
                "report_id": report_id,
                "part_id": part_id,
                "item": item,
                "drawing": drawing,
                "revision": revision.upper(),
                "job_order_id": job_order_id
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "ok_alt",
            "response": "no matching inspection reports found"
        }

#endregion

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)