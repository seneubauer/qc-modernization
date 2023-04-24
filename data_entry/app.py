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
deviations = base.classes.deviations
lots = base.classes.lots
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
employee_projects = base.classes.employee_projects
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
inspection_lots = base.classes.inspection_lots

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

#region page navigation

@app.route("/data_entry/")
def data_entry():
    return render_template("data_entry.html")

#endregion

#region data entry - get enumerations

@app.route("/get_all_gauge_ids/")
def get_all_gauge_ids():

    try:
        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(gauges.id).order_by(gauges.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'gauges'"
            }
    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_gauge_type_ids/")
def get_all_gauge_type_ids():

    try:
        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(gauge_types.id).order_by(gauge_types.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'gauge_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_specification_types/")
def get_all_specification_types():

    try:
        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(specification_types.id).order_by(specification_types.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'specification_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_characteristic_types/")
def get_all_characteristic_types():

    try:
        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(characteristic_types.id).order_by(characteristic_types.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'characteristic_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_employee_ids/")
def get_all_employees_ids():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(employees.id).order_by(employees.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'employees'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_disposition_types/")
def get_all_disposition_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(disposition_types.id).order_by(disposition_types.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'disposition_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_item_numbers/")
def get_all_item_numbers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.item).order_by(parts.drawing.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            results = list(set(results))
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_drawings/")
def get_all_drawings():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.drawing).order_by(parts.drawing.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            results = list(set(results))
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_job_order_ids/")
def get_all_job_order_ids():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_orders.id).order_by(job_orders.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'job_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_material_types/")
def get_all_material_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(material_types.id).order_by(material_types.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'material_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_suppliers/")
def get_all_suppliers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(suppliers.id).order_by(suppliers.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'suppliers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_receiver_numbers/")
def get_all_receiver_numbers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(receiver_numbers.id).order_by(receiver_numbers.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no record found in 'receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/get_all_purchase_orders/")
def get_all_purchase_orders():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id).order_by(purchase_orders.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no records found in 'purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - characteristics

@app.route("/data_entry/get_inspection_report_filtered_characteristics/", methods = ["POST"])
def data_entry_get_inspection_report_filtered_characteristics():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    name = form_data["name"]
    gauge_id = form_data["gauge_id"]
    gauge_type = form_data["gauge_type"]
    spec_type = form_data["spec_type"]
    char_type = form_data["char_type"]
    inspector_id = form_data["inspector_id"]
    check_id = form_data["check_id"]

    # define the columns
    columns = [
        characteristics.id,
        characteristics.name,
        characteristics.nominal,
        characteristics.usl,
        characteristics.lsl,
        characteristics.measured,
        characteristics.precision,
        characteristics.gauge_id,
        gauge_types.id,
        characteristics.specification_type_id,
        characteristics.characteristic_type_id,
        characteristics.employee_id,
        parts.revision
    ]

    try:

        # open the session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(employees, (characteristics.employee_id == employees.id))\
            .join(gauges, (func.lower(characteristics.gauge_id) == gauges.id))\
            .join(inspection_reports, (characteristics.part_id == inspection_reports.part_id))\
            .join(parts, (characteristics.part_id == parts.id))\
            .join(gauge_types, (func.lower(gauges.gauge_type_id) == gauge_types.id))\
            .filter(inspection_reports.id == report_id)

        if name != "__null":
            results = results.filter(characteristics.name.ilike(f"%{name}%"))

        if gauge_id != "__null":
            results = results.filter(characteristics.gauge_id.ilike(f"%{gauge_id}%"))

        if gauge_type != "__null":
            results = results.filter(gauge_types.id.ilike(f"%{gauge_type}%"))

        if spec_type != "__null":
            results = results.filter(characteristics.specification_type_id.ilike(f"%{spec_type}%"))

        if char_type != "__null":
            results = results.filter(characteristics.characteristic_type_id.ilike(f"%{char_type}%"))

        if inspector_id != 0:
            results = results.filter(characteristics.employee_id == inspector_id)

        # convert to a list of tuples
        results_all = results.order_by(characteristics.name.asc()).all()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

    list_status = True

    # gauge ids
    gauge_ids = get_all_gauge_ids()
    if gauge_ids["status"] == "ok":
        gauge_ids = gauge_ids["response"]
    else:
        list_status = False

    # inspectors
    inspectors = get_all_employees_ids()
    if inspectors["status"] == "ok":
        inspectors = inspectors["response"]
    else:
        list_status = False

    # return the result
    if len(results_all) > 0 and list_status:
        output_arr = []
        for id, name, nominal, usl, lsl, measured, precision, gauge_id, gauge_type_id, spec_type_id, char_type_id, employee_id in results_all:
            
            nominal_float = round(float(nominal), precision)
            usl_float = round(float(usl), precision)
            lsl_float = round(float(lsl), precision)
            measured_float = float(measured)

            state = "null"
            if isnan(measured_float):
                measured_float = None
            else:
                measured_float = round(measured_float, precision)
                if usl_float >= measured_float and lsl_float <= measured_float:
                    state = "pass"
                else:
                    state = "fail"

            output_arr.append({
                "id": id,
                "name": name,
                "nominal": nominal_float,
                "usl": usl_float,
                "lsl": lsl_float,
                "measured": measured_float,
                "precision": precision,
                "gauge_id": gauge_id,
                "gauge_type_id": gauge_type_id,
                "spec_type_id": spec_type_id,
                "char_type_id": char_type_id,
                "employee_id": employee_id,
                "state": state
            })

        return {
            "status": "ok",
            "response": {
                "data_array": output_arr,
                "gauge_ids": gauge_ids,
                "inspectors": inspectors
            }
        }
    else:
        return {
            "status": "ok_alt",
            "response": "no matching characteristics found"
        }

#endregion

#region data entry - characteristic schemas


#endregion

#region data entry - report controls

@app.route("/data_entry/get_drawing_from_item_number/", methods = ["POST"])
def data_entry_get_drawing_from_item_number():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item_number = form_data["item"].lower()

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.drawing, parts.revision).filter(func.lower(parts.item) == item_number).all()

        # close the session
        session.close()

        # return the result
        if len(results) > 0:
            print(results)
            drawing = results[0][0]
            rev_arr = []
            for drawing, revision in results:
                rev_arr.append(revision.upper())

            return {
                "status": "ok",
                "response": {
                    "drawing": drawing,
                    "revisions": rev_arr
                }
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no matching records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/get_item_number_from_drawing/", methods = ["POST"])
def data_entry_get_item_number_from_drawing():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    drawing = form_data["drawing"].lower()

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.item, parts.revision).filter(func.lower(parts.drawing) == drawing).all()

        # close the session
        session.close()

        # return the result
        if len(results) > 0:
            item = results[0][0]
            rev_arr = []
            for item, revision in results:
                rev_arr.append(revision.upper())

            return {
                "status": "ok",
                "response": {
                    "item_number": item,
                    "revisions": rev_arr
                }
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no matching records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - existing reports

@app.route("/data_entry/get_filtered_inspection_reports/", methods = ["POST"])
def data_entry_get_filtered_inspection_reports():

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

#region data entry - metadata


#endregion

#region data entry - receiver numbers

@app.route("/data_entry/get_filtered_receiver_numbers/", methods = ["POST"])
def data_entry_get_filtered_receiver_numbers():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    search_filter = form_data["search_filter"]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(receiver_numbers.id)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(receiver_numbers.id.ilike(f"%{search_filter}%"))\
            .order_by(receiver_numbers.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/assign_receiver_number_association/", methods = ["POST"])
def data_entry_assign_receiver_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    receiver_number = form_data["receiver_number"]
    search_filter = form_data["search_filter"]

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        results = session.query(inspection_receiver_numbers.inspection_id)\
            .filter(and_(inspection_receiver_numbers.inspection_id == report_id, func.lower(inspection_receiver_numbers.receiver_number_id) == receiver_number)).all()

        # logic gate
        if len(results) > 0:
            return {
                "status": "ok_alt",
                "response": "this receiver number association already exists"
            }

        # add the new association
        session.add(inspection_receiver_numbers(inspection_id = report_id, receiver_number_id = receiver_number))
        session.commit()

        # get the new list
        results = session.query(receiver_numbers.id)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(receiver_numbers.id.ilike(f"%{search_filter}%"))\
            .order_by(receiver_numbers.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/remove_receiver_number_association/", methods = ["POST"])
def data_entry_remove_receiver_number_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    receiver_number = form_data["receiver_number"]
    search_filter = form_data["search_filter"]

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        results = session.query(inspection_receiver_numbers)\
            .filter(and_(inspection_receiver_numbers.inspection_id == report_id, func.lower(inspection_receiver_numbers.receiver_number_id) == receiver_number))\
            .delete()

        # logic gate
        if results == 0:
            return {
                "status": "ok_alt",
                "response": "no records deleted; none matched the provided criteria"
            }
        else:
            session.commit()

        # get the new list
        results = session.query(receiver_numbers.id)\
            .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(receiver_numbers.id.ilike(f"%{search_filter}%"))\
            .order_by(receiver_numbers.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'receiver_numbers', and 'inspection_receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - purchase orders

@app.route("/data_entry/get_filtered_purchase_orders/", methods = ["POST"])
def data_entry_get_filtered_purchase_orders():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    search_filter = form_data["search_filter"]

    try:
    
        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(purchase_orders.id.ilike(f"%{search_filter}%"))\
            .order_by(purchase_orders.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/assign_purchase_order_association/", methods = ["POST"])
def data_entry_assign_purchase_order_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    purchase_order = form_data["purchase_order"]
    search_filter = form_data["search_filter"]

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        results = session.query(inspection_purchase_orders.inspection_id)\
            .filter(and_(inspection_purchase_orders.inspection_id == report_id, func.lower(inspection_purchase_orders.purchase_order_id) == purchase_order)).all()

        # logic gate
        if len(results) > 0:
            return {
                "status": "ok_alt",
                "response": "this purchase order association already exists"
            }
        
        # add the new association
        session.add(inspection_purchase_orders(inspection_id = report_id, purchase_order_id = purchase_order))
        session.commit()

        # query the database
        results = session.query(purchase_orders.id)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(purchase_orders.id.ilike(f"%{search_filter}%"))\
            .order_by(purchase_orders.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/remove_purchase_order_association/", methods = ["POST"])
def remove_purchase_order_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    report_id = form_data["report_id"]
    purchase_order = form_data["purchase_order"]
    search_filter = form_data["search_filter"]

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        results = session.query(inspection_purchase_orders)\
            .filter(and_(inspection_purchase_orders.inspection_id == report_id, func.lower(inspection_purchase_orders.purchase_order_id) == purchase_order))\
            .delete()

        # logic gate
        if results == 0:
            return {
                "status": "ok_alt",
                "response": "no records deleted; none matched the provided criteria"
            }
        else:
            session.commit()

        # query the database
        results = session.query(purchase_orders.id)\
            .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
            .filter(inspection_reports.id == report_id)\
            .filter(purchase_orders.id.ilike(f"%{search_filter}%"))\
            .order_by(purchase_orders.id.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id in results:
                output_arr.append({
                    "report_id": report_id,
                    "item": id[0]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "no connection found between 'inspection_reports', 'purchase_orders', and 'inspection_purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

#endregion

#region data entry - lots


#endregion

@app.route("/commit_characteristic_data/<int:report_id>/", methods = ["POST"])
def commit_characteristic_data(report_id:int):

    # handle a null report id
    if report_id == -1:
        return {
            "status": "ok_alt",
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
                        "status": "ok_alt",
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
                    "status": "ok_alt",
                    "response": "no rows affected"
                }

        except SQLAlchemyError as e:
            error_msg = str(e.__dict__["orig"])
            return {
                "status": "not_ok",
                "response": error_msg
            }

    else:
        return {
            "status": "ok_alt",
            "response": "no data passed to flask server"
        }

@app.route("/get_schema_type_lists/")
def get_schema_type_lists():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results_spec_types = session.query(specification_types.id).order_by(specification_types.id.asc()).all()
        results_char_types = session.query(characteristic_types.id).order_by(characteristic_types.id.asc()).all()
        results_gauge_types = session.query(gauge_types.id).order_by(gauge_types.id.asc()).all()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

    # return the results
    if len(results_spec_types) > 0 and len(results_char_types) > 0 and len(results_gauge_types) > 0:
        output_arr_spec_types = []
        for id in results_spec_types:
            output_arr_spec_types.append({
                "item": id[0]
            })

        output_arr_char_types = []
        for id in results_char_types:
            output_arr_char_types.append({
                "item": id[0]
            })

        output_arr_gauge_types = []
        for id in results_gauge_types:
            output_arr_gauge_types.append({
                "item": id[0]
            })

        return {
            "status": "ok",
            "response": {
                "spec_types": output_arr_spec_types,
                "char_types": output_arr_char_types,
                "gauge_types": output_arr_gauge_types
            }
        }
    else:
        return {
            "status": "ok_alt",
            "response": "no schema type records found"
        }

@app.route("/get_filtered_char_schemas/<string:search_term>/")
def get_filtered_char_schemas(search_term:str):

    # handle the null value
    if search_term == "__null":
        search_term = ""

    # enforce lower case
    search_term = search_term.lower()

    try:
        schema_list = list(filter(lambda item:
                                isfile(join(char_schema_destination, item))
                                and item[-len(".csv"):].lower() == ".csv"
                                and search_term in item.lower(), listdir(char_schema_destination)))
    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

    if len(schema_list) > 0:
        return {
            "status": "ok",
            "response": [splitext(x)[0] for x in schema_list]
        }
    else:
        return {
            "status": "ok_alt",
            "response": "no matching schema files found"
        }

@app.route("/save_schema_csv/<string:file_name>/", methods = ["POST"])
def save_schema_csv(file_name:str):

    # enforce lower case
    file_name = file_name.lower()

    # interpret the form data
    schema_data = {
        "name": [],
        "nominal": [],
        "usl": [],
        "lsl": [],
        "precision": [],
        "spec_type": [],
        "char_type": [],
        "gauge_type": []
    }

    for k, v in request.form.items():
        key_split = k.split("-")
        field = str(key_split[1])
        schema_data[field].append(v)

    if len(schema_data["name"]) == 0:
        return {
            "status": "ok_alt",
            "response": "no data to be saved"
        }

    try:
        pd.DataFrame(schema_data).to_csv(join("char_schema_templates", f"{file_name}.csv"), index = False)
        return {
            "status": "ok",
            "response": "schema file successfully saved"
        }
    except Exception as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/load_schema_from_csv/<string:file_name>/")
def load_schema_from_csv(file_name:str):

    # attach the file extension
    file_name = f"{file_name}.csv".lower()

    try:
        available_files = listdir(char_schema_destination)
        if file_name in available_files:

            # read the file into a dataframe
            df = pd.read_csv(join(char_schema_destination, file_name))

            # construct the output object
            output_arr = []
            for index, row in df.iterrows():
                output_arr.append({
                    "name": row["name"],
                    "nominal": row["nominal"],
                    "usl": row["usl"],
                    "lsl": row["lsl"],
                    "precision": row["precision"],
                    "spec_type": row["spec_type"],
                    "char_type": row["char_type"],
                    "gauge_type": row["gauge_type"]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_alt",
                "response": "file not found"
            }

    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/delete_schema/<string:file_name>/")
def delete_schema(file_name:str):

    # attach the file extension
    file_name = f"{file_name}.csv".lower()

    try:
        available_files = listdir(char_schema_destination)
        if file_name in available_files:
            remove(join(char_schema_destination, file_name))
            return {
                "status": "ok",
                "response": "schema file successfully deleted"
            }
        else:
            return {
                "status": "ok_alt",
                "response": "file not found"
            }

    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/commit_new_characteristic_schema/<string:item>/<string:drawing>/<string:revision>/", methods = ["POST"])
def commit_new_characteristic_schema(item:str, drawing:str, revision:str):

    # enforce lower case
    item = item.lower()
    drawing = drawing.lower()
    revision = revision.lower()

    # interpret the form data
    schema_data = {
        "name": [],
        "nominal": [],
        "usl": [],
        "lsl": [],
        "precision": [],
        "spec_type": [],
        "char_type": [],
        "gauge_type": []
    }

    for k, v in request.form.items():
        key_split = k.split("-")
        field = str(key_split[1])
        schema_data[field].append(v)

    if len(schema_data["name"]) == 0:
        return {
            "status": "ok_alt",
            "response": "no schema data to be applied"
        }

    try:

        # open the database session
        session = Session(engine)

        # check if the inspection report already exists
        results = session.query(parts.id)\
            .join(parts, (inspection_reports.part_id == parts.id))\
            .filter(func.lower(parts.item) == item)\
            .filter(func.lower(parts.drawing) == drawing)\
            .filter(func.lower(parts.revision) == revision).all()
        if len(results) == 0:
            return {
                "status": "ok_alt",
                "response": f"no matching inspection report for the part ({item}, {drawing}, {revision})"
            }

        # results = session.query(characteristics).filter(characteristics.part_id == par)
        for i in range(len(schema_data["name"])):

            
            print(i)

        # close the database session
        session.close()

        return {
            "status": "ok",
            "response": "hello world"
        }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/create_new_inspection_report/<string:item>/<string:drawing>/<string:revision>/")
def create_new_inspection_report(item:str, drawing:str, revision:str):

    # handle null values
    if revision == "__null":
        return {
            "status": "ok_alt",
            "response": "revision must be defined"
        }

    # enforce lower case
    item = item.lower()
    drawing = drawing.lower()
    revision = revision.lower()

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

@app.route("/save_inspection_report_metadata/", methods = ["POST"])
def save_inspection_report_metadata():

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





# @app.route("/get_all_employee_ids/")
# def get_all_employees():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(employees.id).order_by(employees.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_disposition_types/")
# def get_all_disposition_types():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(disposition_types.id).order_by(disposition_types.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_item_numbers/")
# def get_all_item_numbers():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(parts.item).order_by(parts.drawing.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_drawings/")
# def get_all_drawings():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(parts.drawing).order_by(parts.drawing.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_job_orders/")
# def get_all_job_orders():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(job_orders.id).order_by(job_orders.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_receiver_numbers/")
# def get_all_receiver_numbers():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(receiver_numbers.id).order_by(receiver_numbers.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })
        
#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_all_purchase_orders/")
# def get_all_purchase_orders():

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(purchase_orders.id).order_by(purchase_orders.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })
        
#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/inspection_report_drawing_changed/<string:drawing>/")
# def inspection_report_drawing_changed(drawing:str):

#     # open the database connection
#     session = Session(engine)

#     # query the database
#     results = session.query(parts.item).filter(parts.drawing == drawing).order_by(parts.drawing.asc()).first()

#     # close the session
#     session.close()

#     # return the results
#     if results is not None:
#         return {
#             "status": "ok",
#             "response": results[0]
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/inspection_report_item_number_changed/<string:item_number>/")
# def inspection_report_item_number_changed(item_number:str):

#     # open the database connection
#     session = Session(engine)

#     # query the database
#     results = session.query(parts.drawing).filter(parts.item == item_number).order_by(parts.drawing.asc()).first()

#     # close the session
#     session.close()

#     # return the results
#     if results is not None:
#         return {
#             "status": "ok",
#             "response": results[0]
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/add_receiver_number_association/<int:report_id>/<string:receiver_number>/")
# def add_receiver_number_association(report_id:int, receiver_number:str):

#     # open the database session
#     session = Session(engine)

#     # make sure the new receiver number isn't already associated with the report id
#     results = session.query(inspection_receiver_numbers.id)\
#         .filter(and_(inspection_receiver_numbers.inspection_id == report_id, inspection_receiver_numbers.receiver_number_id == receiver_number))\
#         .order_by(inspection_receiver_numbers.id.asc()).all()

#     # logic gate
#     if len(results) > 0:
#         return {
#             "status": "not_ok",
#             "response": "association already exists"
#         }

#     # add the new association
#     session.add(inspection_receiver_numbers(inspection_id = report_id, receiver_number_id = receiver_number))
#     session.commit()
    
#     # get the new list of associated receiver numbers
#     new_response = get_receiver_numbers_from_report_id(report_id)

#     # logic gate
#     if new_response["status"] == "not_ok":
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query while retrieving the list of associations"
#         }

#     # close the session
#     session.close()

#     # return the results
#     return {
#         "status": "ok",
#         "response": new_response["response"]
#     }

# @app.route("/remove_receiver_number_association/<int:report_id>/<string:receiver_number>/")
# def remove_receiver_number_association(report_id:int, receiver_number:str):

#     # open the database session
#     session = Session(engine)

#     # delete the record that matches the provided criteria
#     results = session.query(inspection_receiver_numbers).filter(and_(inspection_receiver_numbers.inspection_id == report_id, inspection_receiver_numbers.receiver_number_id == receiver_number)).delete()

#     # logic gate
#     if results == 0:
#         return {
#             "status": "not_ok",
#             "response": "no records deleted; none matched the provided criteria"
#         }
#     else:
#         session.commit()

#     # get the new list of associated receiver numbers
#     new_response = get_receiver_numbers_from_report_id(report_id)

#     # logic gate
#     if new_response["status"] == "not_ok":
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query while retrieving the list of associations"
#         }

#     # close the session
#     session.close()

#     # return the results
#     return {
#         "status": "ok",
#         "response": new_response["response"]
#     }

# @app.route("/get_receiver_numbers_from_report_id/<int:report_id>/")
# def get_receiver_numbers_from_report_id(report_id:int):

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(receiver_numbers.id)\
#         .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
#         .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
#         .filter(inspection_reports.id == report_id)\
#         .order_by(receiver_numbers.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/add_purchase_order_association/<int:report_id>/<string:purchase_order>/")
# def add_purchase_order_association(report_id:int, purchase_order:str):

#     # open the database session
#     session = Session(engine)

#     # make sure the new receiver number isn't already associated with the report id
#     results = session.query(inspection_purchase_orders.id)\
#         .filter(and_(inspection_purchase_orders.inspection_id == report_id, inspection_purchase_orders.purchase_order_id == purchase_order)).all()

#     # logic gate
#     if len(results) > 0:
#         return {
#             "status": "not_ok",
#             "response": "association already exists"
#         }

#     # add the new association
#     session.add(inspection_purchase_orders(inspection_id = report_id, purchase_order_id = purchase_order))
#     session.commit()
    
#     # get the new list of associated receiver numbers
#     new_response = get_purchase_orders_from_report_id(report_id)

#     # logic gate
#     if new_response["status"] == "not_ok":
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query while retrieving the list of associations"
#         }

#     # close the session
#     session.close()

#     # return the results
#     return {
#         "status": "ok",
#         "response": new_response["response"]
#     }

# @app.route("/remove_purchase_order_association/<int:report_id>/<string:purchase_order>/")
# def remove_purchase_order_association(report_id:int, purchase_order:str):

#     # open the database session
#     session = Session(engine)

#     # delete the record that matches the provided criteria
#     results = session.query(inspection_purchase_orders).filter(and_(inspection_purchase_orders.inspection_id == report_id, inspection_purchase_orders.purchase_order_id == purchase_order)).delete()

#     # logic gate
#     if results == 0:
#         return {
#             "status": "not_ok",
#             "response": "no records deleted; none matched the provided criteria"
#         }
#     else:
#         session.commit()

#     # get the new list of associated receiver numbers
#     new_response = get_purchase_orders_from_report_id(report_id)

#     # logic gate
#     if new_response["status"] == "not_ok":
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query while retrieving the list of associations"
#         }

#     # close the session
#     session.close()

#     # return the results
#     return {
#         "status": "ok",
#         "response": new_response["response"]
#     }

# @app.route("/get_purchase_orders_from_report_id/<int:report_id>/")
# def get_purchase_orders_from_report_id(report_id:int):

#     # open the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(purchase_orders.id)\
#         .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
#         .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
#         .filter(inspection_reports.id == report_id)\
#         .order_by(purchase_orders.id.asc()).all()

#     # close the session
#     session.close()

#     # return the results
#     if len(results) > 0:
#         output_arr = []
#         for id in results:
#             output_arr.append({
#                 "id": id[0]
#             })

#         return {
#             "status": "ok",
#             "response": output_arr
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_inspection_reports/<int:filter_type>/<string:filter_term>/<string:use_date_span>/<int:start_day>/<int:start_month>/<int:start_year>/<int:stop_day>/<int:stop_month>/<int:stop_year>/")
# def get_inspection_reports(filter_type:int, filter_term:str, use_date_span:str, start_day:int, start_month:int, start_year:int, stop_day:int, stop_month:int, stop_year:int):

#     # build the filtering dates
#     start_date = datetime.date(start_year, start_month, start_day)
#     stop_date = datetime.date(stop_year, stop_month, stop_day)

#     # define the output fields
#     output_arr = [
#         inspection_reports.id,
#         parts.drawing,
#         parts.revision,
#         parts.item,
#         inspection_reports.day_started,
#         inspection_reports.day_finished,
#         inspection_reports.employee_id,
#         inspection_reports.disposition,
#         inspection_reports.job_order_id
#     ]

#     # open the database session
#     session = Session(engine)

#     # start the database query
#     results = session.query(*output_arr).join(parts, (parts.id == inspection_reports.part_id))

#     # add the date filtering
#     if use_date_span == "true":
#         results = results.filter(and_(inspection_reports.day_started >= start_date, inspection_reports.day_finished <= stop_date))

#     # add the drawing or item filtering
#     if filter_type == 1:
#         results = results.filter(parts.drawing.like(f"%{filter_term}%"))
#     elif filter_type == 2:
#         results = results.filter(parts.item.like(f"%{filter_term}%"))

#     # close the session
#     session.close()

#     # assemble the results
#     results_list = results.all()
#     output_data = []
#     if len(results_list) > 0:
#         for id, drawing, revision, item, started, finished, employee_id, disposition, job_order_id in results_list:
#             output_data.append({
#                 "report_id": id,
#                 "drawing": drawing,
#                 "item_number": item,
#                 "revision": revision.upper(),
#                 "start_year": started.year,
#                 "start_month": started.month,
#                 "start_day": started.day,
#                 "finish_year": finished.year,
#                 "finish_month": finished.month,
#                 "finish_day": finished.day,
#                 "started": f"{started.month:02}/{started.day:02}/{started.year:04}",
#                 "finished": f"{finished.month:02}/{finished.day:02}/{finished.year:04}",
#                 "employee": employee_id,
#                 "disposition": disposition,
#                 "job_order": job_order_id
#             })

#         return {
#             "status": "ok",
#             "response": output_data
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# @app.route("/get_inspection_report_characteristics/<int:report_id>/<string:part_item>/<string:part_drawing>/<string:part_revision>/<string:name_filter>/")
# def get_inspection_report_characteristics(report_id:int, part_item:str, part_drawing:str, part_revision:str, name_filter:str):

#     # specify the output columns
#     columns = [
#         characteristics.name,
#         characteristics.nominal,
#         characteristics.usl,
#         characteristics.lsl,
#         characteristics.measured,
#         characteristics.precision,
#         specification_types.id,
#         characteristic_types.id,
#         characteristic_types.is_gdt,
#         employees.id,
#         gauges.id,
#         gauge_types.id
#     ]

#     # open the database session
#     session = Session(engine)

#     # get all the employee ids
#     results = session.query(employees.id).all()
#     employee_ids = []
#     if len(results) > 0:
#         for id in results:
#             employee_ids.append(id[0])

#     # close the session
#     session.close()

#     # reopen the database session
#     session = Session(engine)

#     # query the database
#     results = session.query(*columns)\
#         .join(specification_types, (characteristics.specification_type_id == specification_types.id))\
#         .join(characteristic_types, (characteristics.characteristic_type_id == characteristic_types.id))\
#         .join(employees, (characteristics.employee_id == employees.id))\
#         .join(gauges, (characteristics.gauge_id == gauges.id))\
#         .join(gauge_types, (gauges.gauge_type_id == gauge_types.id))\
#         .join(inspection_reports, (characteristics.part_id == inspection_reports.part_id))\
#         .join(parts, (characteristics.part_id == parts.id))\
#         .filter(inspection_reports.id == report_id)\
#         .filter(and_(parts.item == part_item.lower(), parts.drawing == part_drawing.lower(), parts.revision == part_revision.lower()))

#     # close the session
#     session.close()

#     # apply the name filter if it was specified
#     if name_filter != "__none":
#         results = results.filter(characteristics.name.like(f"%{name_filter}%"))

#     # convert results to a list of tuples
#     results_list = results.all()

#     # return the results
#     if len(results_list) > 0:
#         output_arr = []
#         for name, nominal, usl, lsl, measured, precision, specification_type, characteristic_type, is_gdt, employee_id, gauge_id, gauge_type in results_list:
#             nominal_float = round(float(nominal), precision)
#             usl_float = round(float(usl), precision)
#             lsl_float = round(float(lsl), precision)
#             measured_float = float(measured)

#             state = "null"
#             if isnan(measured_float):
#                 measured_float = None
#                 state = "null"
#             else:
#                 measured_float = round(float(measured), precision)
#                 if usl_float >= measured_float and lsl_float <= measured_float:
#                     state = "pass"
#                 else:
#                     state = "fail"

#             output_arr.append({
#                 "name": name,
#                 "nominal": nominal_float,
#                 "usl": usl_float,
#                 "lsl": lsl_float,
#                 "measured": measured_float,
#                 "precision": precision,
#                 "specification_type": specification_type,
#                 "characteristic_type": characteristic_type,
#                 "is_gdt": is_gdt,
#                 "employee_id": employee_id,
#                 "gauge_id": gauge_id,
#                 "gauge_type": gauge_type,
#                 "state": state
#             })

#         return {
#             "status": "ok",
#             "response": {
#                 "cell_data": output_arr,
#                 "employee_ids": employee_ids
#             }
#         }
#     else:
#         return {
#             "status": "not_ok",
#             "response": "error within the flask server or database query"
#         }

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)