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
            results = list(set(results))
            for id, drawing, revision, item in results:
                output_arr.append({
                    "id": id,
                    "drawing": drawing,
                    "revision": revision,
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

@app.route("/commit_characteristic_data/<int:report_id>/", methods = ["POST"])
def commit_characteristic_data(report_id:int):

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

#region data entry - characteristic schemas

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
            "status": "err_log",
            "response": error_msg
        }

    # return the results
    if len(results_spec_types) > 0 and len(results_char_types) > 0 and len(results_gauge_types) > 0:
        output_arr_spec_types = []
        for id, name in results_spec_types:
            output_arr_spec_types.append({
                "id": id,
                "name": name
            })

        output_arr_char_types = []
        for id, name, is_gdt in results_char_types:
            output_arr_char_types.append({
                "id": id,
                "name": name,
                "is_gdt": is_gdt
            })

        output_arr_gauge_types = []
        for id, name in results_gauge_types:
            output_arr_gauge_types.append({
                "id": id,
                "name": name
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
            "status": "ok_log",
            "response": "get schema type lists -> no schema type records found"
        }

@app.route("/get_filtered_char_schemas/", methods = ["POST"])
def get_filtered_char_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"].lower()

    try:
        schema_list = list(filter(lambda item:
                                isfile(join(char_schema_destination, item))
                                and item[-len(".csv"):].lower() == ".csv"
                                and search_term in item.lower(), listdir(char_schema_destination)))
    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

    if len(schema_list) > 0:
        return {
            "status": "ok",
            "response": [splitext(x)[0] for x in schema_list]
        }
    else:
        return {
            "status": "ok_log",
            "response": "get filtered char schemas -> no matching schema files found"
        }

@app.route("/save_schema_csv/", methods = ["POST"])
def save_schema_csv():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    file_name = form_data["file_name"]

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
            "status": "ok_log",
            "response": "save schema csv -> no data to be saved"
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
            "status": "err_log",
            "response": error_msg
        }

@app.route("/load_schema_from_csv/", methods = ["POST"])
def load_schema_from_csv():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    file_name = form_data["file_name"]

    try:
        available_files = listdir(char_schema_destination)
        if file_name in available_files:

            # read the file into a dataframe
            df = pd.read_csv(join(char_schema_destination, file_name))

            # construct the output object
            output_arr = []
            for i, r in df.iterrows():
                output_arr.append({
                    "name": r["name"],
                    "nominal": r["nominal"],
                    "usl": r["usl"],
                    "lsl": r["lsl"],
                    "precision": r["precision"],
                    "spec_type": r["spec_type"],
                    "char_type": r["char_type"],
                    "gauge_type": r["gauge_type"]
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok_log",
                "response": "load schema from file -> file not found"
            }

    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/delete_schema/", methods = ["POST"])
def delete_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    file_name = form_data["file_name"]

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
                "status": "ok_log",
                "response": "delete schema -> file not found"
            }

    except OSError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "err_log",
            "response": error_msg
        }

@app.route("/commit_new_characteristic_schema/", methods = ["POST"])
def commit_new_characteristic_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item = form_data["item"]
    drawing = form_data["drawing"]
    revision = form_data["revision"]

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

@app.route("/create_new_inspection_report/", methods = ["POST"])
def create_new_inspection_report():

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

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)