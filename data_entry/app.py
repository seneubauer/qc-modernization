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
from enum import Enum
from inspect import stack

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
deviation_types = base.classes.deviation_types
disposition_types = base.classes.disposition_types
location_types = base.classes.location_types
machine_types = base.classes.machine_types
gauge_types = base.classes.gauge_types
dimension_types = base.classes.dimension_types
specification_types = base.classes.specification_types
project_types = base.classes.project_types
material_types = base.classes.material_types
frequency_types = base.classes.frequency_types
inspection_types = base.classes.inspection_types
lot_numbers = base.classes.lot_numbers
suppliers = base.classes.suppliers
job_numbers = base.classes.job_numbers
purchase_orders = base.classes.purchase_orders
receiver_numbers = base.classes.receiver_numbers
projects = base.classes.projects
departments = base.classes.departments
locations = base.classes.locations
employees = base.classes.employees
machines = base.classes.machines
inspection_records = base.classes.inspection_records
parts = base.classes.parts
gauges = base.classes.gauges
inspections = base.classes.inspections
features = base.classes.features
deviations = base.classes.deviations
inspection_schemas = base.classes.inspection_schemas
inspection_schema_details = base.classes.inspection_schema_details
employee_projects = base.classes.employee_projects
inspections_job_numbers = base.classes.inspections_job_numbers
inspection_records_purchase_orders = base.classes.inspection_records_purchase_orders
inspection_records_lot_numbers = base.classes.inspection_records_lot_numbers

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# --------------------------------------------------

#region messaging

# message type enumerations
class message_type(Enum):
    records_not_found = 0
    record_already_exists = 1
    record_locked = 2
    records_deleted = 3
    records_updated = 4
    records_not_deleted = 5
    records_not_updated = 6
    no_records_added = 7
    no_association_found = 8
    sql_exception = 9
    generic = 10

def text_response(current_method:str, type:message_type, **kwargs):

    output_str = ""
    if type == message_type.records_not_found:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"no matching records found in the following tables; {tables}"
    elif type == message_type.record_already_exists:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"record already exists in {tables}"
    elif type == message_type.record_locked:
        output_str = f"editing is not allowed; '{kwargs['table'].__table__.name}' is locked"
    elif type == message_type.records_deleted:
        output_str = f"{kwargs['qty']} records deleted from '{kwargs['table']}'"
    elif type == message_type.records_updated:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"{kwargs['qty']} records updated in {tables}"
    elif type == message_type.records_not_deleted:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"no records deleted from the following tables; {tables}"
    elif type == message_type.records_not_updated:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"no records updated in the following tables; {tables}"
    elif type == message_type.no_records_added:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"no records added to the following tables; {tables}"
    elif type == message_type.no_association_found:
        tables = ", ".join([f"'{x.__table__.name}'" for x in kwargs["tables"]])
        output_str = f"no association found between the following tables; {tables}"
    elif type == message_type.sql_exception:
        output_str = str(kwargs["error"])
    elif type == message_type.generic:
        output_str = kwargs["err_msg"]
    else:
        output_str = "response type not given"

    return f"def {current_method}()\n{output_str}"

#endregion

# --------------------------------------------------

#region page navigation

@app.route("/inspection_schemas/")
def open_measurement_set_schemas():
    return render_template("inspection_schemas.html")

@app.route("/inspection_records/")
def open_inspection_reports():
    return render_template("inspection_records.html")

#endregion

# --------------------------------------------------

#region get enumerations

@app.route("/get_all_dimension_types/")
def get_all_dimension_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(dimension_types.id, dimension_types.name).order_by(dimension_types.name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }

        else:
            return {
                "status": "log",
                "response": "no records found in 'dimension_types'"
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/get_all_deviation_types/")
def get_all_deviation_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(deviation_types.id, deviation_types.name).order_by(deviation_types.name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }

        else:
            return {
                "status": "log",
                "response": "no records found in 'deviation_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

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
                "status": "ok",
                "response": output_arr
            }

        else:
            return {
                "status": "log",
                "response": "no records found in 'gauges'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'gauge_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'specification_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'frequency_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/get_all_inspection_types/")
def get_all_inspection_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(inspection_types.id, inspection_types.name).order_by(inspection_types.name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'inspection_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
        results = session.query(*columns).order_by(employees.last_name.asc(), employees.first_name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'employees'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/get_filtered_employees/", methods = ["POST"])
def get_filtered_employees():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

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
        results = session.query(*columns)\
            .filter(or_(employees.first_name.ilike(f"%{search_term}%"), employees.last_name.ilike(f"%{search_term}%")))\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'employees'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'disposition_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
        results = session.query(*columns).order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc()).all()

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
                    "item": item,
                    "name": f"{item}, {drawing}, {revision.upper()}"
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'parts'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/get_all_job_numbers/")
def get_all_job_numbers():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_numbers.id, job_numbers.name).order_by(job_numbers.name.asc()).all()

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'job_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'material_types'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'suppliers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no record found in 'receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'purchase_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

# --------------------------------------------------

#region inspection schemas - schemas

# routes

@app.route("/inspection_schemas/schemas/create_new_schema/", methods = ["POST"])
def inspection_schemas_schemas_create_new_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = form_data["part_id"]
    search_term = form_data["search_term"]
    is_locked = int(form_data["is_locked"])

    try:

        # open the database session
        session = Session(engine)

        # make sure the measurement schema doesn't already exist
        exists = session.query(inspection_schemas.id)\
            .filter(inspection_schemas.part_id == part_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [inspection_schemas])
            }

        # create new governing record in the database
        results = inspection_schemas(
            is_locked = False,
            part_id = part_id
        )
        session.add(results)
        session.commit()
        schema_id = results.id
        if schema_id is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.no_records_added, tables = [inspection_schemas])
            }

        # close the database session
        session.close()

        # create the first measurement in the new schema
        returned_obj0 = func_inspection_schemas_add_detail_record(schema_id)

        # requery the schemas with the same filter parameters
        returned_obj1 = func_inspection_schemas_get_filtered_schemas(search_term, is_locked)

        # return the results
        if returned_obj0["status"] == "ok" and returned_obj1["status"] == "ok":
            return {
                "status": "ok",
                "response": {
                    "schema_list": returned_obj1["response"],
                    "schema_measurements": returned_obj0["response"]
                }
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.no_records_added, tables = [inspection_schemas, inspection_schema_details])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_schemas/schemas/add_row/", methods = ["POST"])
def inspection_schemas_schemas_add_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # measurement_set if the schema is locked
        locked_query = session.query(inspection_schemas.is_locked)\
            .filter(inspection_schemas.id == schema_id)\
            .first()[0]
        if locked_query:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_locked, table = inspection_schemas)
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

    return func_inspection_schemas_add_detail_record(schema_id)

@app.route("/inspection_schemas/schemas/remove_row/", methods = ["POST"])
def inspection_schemas_schemas_remove_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    detail_id = form_data["detail_id"]

    try:

        # open the database session
        session = Session(engine)

        # get the schema id
        schema_id = session.query(inspection_schema_details.schema_id)\
            .filter(inspection_schema_details.id == detail_id)\
            .first()[0]

        # measurement_set if the schema is locked
        locked_query = session.query(inspection_schemas.is_locked)\
            .filter(inspection_schemas.id == schema_id)\
            .first()[0]
        if locked_query:
            session.close()
            return text_response(stack()[0][3], message_type.record_locked, table = inspection_schemas)

        # make sure there is something to be deleted
        results = session.query(inspection_schema_details.id)\
            .filter(inspection_schema_details.id == detail_id)\
            .first()
        if results is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [inspection_schema_details])
            }

        # remove the matching schema id
        results = session.query(inspection_schema_details)\
            .filter(inspection_schema_details.id == detail_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if results > 0:
            return {
                "status": "ok",
                "response": text_response(stack()[0][3], message_type.records_deleted, qty = results, table = inspection_schema_details)
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_deleted, qty = results, table = inspection_schema_details)
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_schemas/schemas/toggle_lock_schema/", methods = ["POST"])
def inspection_schemas_schemas_toggle_lock_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]
    is_locked = int(form_data["is_locked"])
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the measurement schema exists
        exists = session.query(inspection_schemas.id)\
            .filter(inspection_schemas.id == schema_id)\
            .first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [inspection_schemas])
            }

        # get the current locked status
        locked_query = session.query(inspection_schemas.is_locked)\
            .filter(inspection_schemas.id == schema_id)\
            .first()[0]

        # set the locked status
        rows_affected = session.query(inspection_schemas)\
            .filter(inspection_schemas.id == schema_id)\
            .update({ "is_locked": not locked_query })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # logic gate
        if rows_affected == 0:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [inspection_schemas])
            }

        # requery the schemas
        returned_obj = func_inspection_schemas_get_filtered_schemas(search_term, is_locked)

        # return the results
        if returned_obj["status"] == "ok":
            return {
                "status": "ok",
                "response": {
                    "is_locked": not locked_query,
                    "schema_list": returned_obj["response"]
                }
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_schemas/schemas/save_inspection_schema/", methods = ["POST"])
def inspection_schemas_schemas_save_inspection_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the measurement schema exists
        exists = session.query(inspection_schema_details.id)\
            .filter(inspection_schema_details.schema_id == schema_id)\
            .first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [inspection_schema_details])
            }

        # query the database
        rows_affected = 0
        for obj in form_data["data"]:
            results = session.query(inspection_schema_details)\
                .filter(inspection_schema_details.id == obj["detail_id"])
            field_affected = 0
            for x in obj["contents"]:
                field_affected += results.update({ x["key"]: x["value"] })
            if field_affected > 0:
                rows_affected += 1

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if rows_affected > 0:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [inspection_schema_details])
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [inspection_schema_details])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_schemas/schemas/delete_inspection_schema/", methods = ["POST"])
def inspection_schemas_schemas_delete_inspection_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]
    search_term = form_data["search_term"]
    is_locked = int(form_data["is_locked"])

    try:

        # open the database session
        session = Session(engine)

        # make sure the referenced schema exists
        exists = session.query(inspection_schemas.id)\
            .filter(inspection_schemas.id == schema_id).first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [inspection_schemas])
            }

        # measurement_set if the schema is already locked
        schema_is_locked = session.query(inspection_schemas.is_locked)\
            .filter(inspection_schemas.id == schema_id)\
            .first()[0]
        if schema_is_locked:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_locked, table = inspection_schemas)
            }

        # delete the referenced schema
        details_results = session.query(inspection_schema_details)\
            .filter(inspection_schema_details.schema_id == schema_id)\
            .delete()
        schema_results = session.query(inspection_schemas)\
            .filter(inspection_schemas.id == schema_id)\
            .delete()

        # logic gate
        if details_results == 0 and schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_deleted, tables = [inspection_schemas, inspection_schema_details])
            }
        elif details_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_deleted, qty = details_results, table = inspection_schema_details)
            }
        elif schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_deleted, qty = schema_results, table = inspection_schemas)
            }

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # requery the schemas
        return func_inspection_schemas_get_filtered_schemas(search_term, is_locked)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_schemas/schemas/get_filtered_inspection_schemas/", methods = ["POST"])
def inspection_schemas_schema_get_filtered_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    is_locked = int(form_data["is_locked"])

    # call the relevant method
    return func_inspection_schemas_get_filtered_schemas(search_term, is_locked)

@app.route("/inspection_schemas/schemas/get_filtered_parts/", methods = ["POST"])
def inspection_schemas_schema_get_filtered_parts():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # start the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.item, parts.drawing, parts.revision)\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, item, drawing, revision in results:
                output_arr.append({
                    "id": id,
                    "item": item,
                    "drawing": drawing,
                    "revision": revision,
                    "part_name": f"{item}, {drawing}, {revision.upper()}"
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_inspection_schemas_add_detail_record(schema_id:int):

    try:

        # open the database session
        session = Session(engine)

        # get the default specification type id
        default_specification_type_id = session.query(specification_types.id)\
            .order_by(specification_types.name.asc())\
            .first()[0]

        # get the default dimension type id
        default_dimension_type_id = session.query(dimension_types.id)\
            .order_by(dimension_types.name.asc())\
            .first()[0]

        # get the default frequency type id
        default_frequency_type_id = session.query(frequency_types.id)\
            .order_by(frequency_types.name.asc())\
            .first()[0]

        # get the default gauge type id
        default_gauge_type_id = session.query(gauge_types.id)\
            .order_by(gauge_types.name.asc())\
            .first()[0]

        # define the placeholder values
        default_name = "DIM X"
        default_nominal = 0
        default_usl = 0
        default_lsl = 0
        default_precision = 1

        # set the placeholder data
        results = inspection_schema_details(
            name = default_name,
            nominal = default_nominal,
            usl = default_usl,
            lsl = default_lsl,
            precision = default_precision,
            specification_type_id = default_specification_type_id,
            dimension_type_id = default_dimension_type_id,
            frequency_type_id = default_frequency_type_id,
            gauge_type_id = default_gauge_type_id,
            schema_id = schema_id
        )
        session.add(results)
        session.commit()

        # capture the new serial id
        detail_id = results.id

        # close the database session
        session.close()

        # return the results
        if results.id is not None:
            return {
                "status": "ok",
                "response": {
                    "id": detail_id,
                    "name": default_name,
                    "nominal": default_nominal,
                    "usl": default_usl,
                    "lsl": default_lsl,
                    "precision": default_precision,
                    "specification_type_id": default_specification_type_id,
                    "dimension_type_id": default_dimension_type_id,
                    "frequency_type_id": default_frequency_type_id,
                    "gauge_type_id": default_gauge_type_id,
                    "schema_id": schema_id
                }
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.no_records_added, tables = [inspection_schema_details])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

def func_inspection_schemas_get_filtered_schemas(search_term:str, is_locked:int):

    # define the output columns
    columns = [
        inspection_schemas.id,
        inspection_schemas.is_locked,
        parts.id,
        parts.item,
        parts.drawing,
        parts.revision
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(parts, (parts.id == inspection_schemas.part_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))
        if is_locked >= 0:
            results = results.filter(inspection_schemas.is_locked == bool(is_locked))
        results = results.order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for schema_id, is_locked, part_id, item, drawing, revision in results:
                output_arr.append({
                    "schema_id": schema_id,
                    "is_locked": is_locked,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "revision": revision.upper()
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection schemas - schema view

@app.route("/inspection_schemas/view/get_schema_features/", methods = ["POST"])
def inspection_schemas_view_get_schema_measurements():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    # define the output columns
    columns = [
        inspection_schemas.id,
        inspection_schemas.is_locked,
        parts.id,
        inspection_schema_details.id,
        inspection_schema_details.name,
        inspection_schema_details.nominal,
        inspection_schema_details.usl,
        inspection_schema_details.lsl,
        inspection_schema_details.precision,
        inspection_schema_details.specification_type_id,
        inspection_schema_details.dimension_type_id,
        inspection_schema_details.frequency_type_id,
        inspection_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the requested schema
        results = session.query(*columns)\
            .join(parts, (parts.id == inspection_schemas.part_id))\
            .join(inspection_schema_details, (inspection_schema_details.schema_id == inspection_schemas.id))\
            .filter(inspection_schemas.id == schema_id)\
            .order_by(inspection_schema_details.id.asc(), inspection_schema_details.name.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for schema_id, is_locked, part_id, detail_id, name, nominal, usl, lsl, precision, specification_type_id, dimension_type_id, frequency_type_id, gauge_type_id in results:

                # parse decimal to float
                nominal_flt = round(float(nominal), precision)
                usl_flt = round(float(usl), precision)
                lsl_flt = round(float(lsl), precision)

                output_arr.append({
                    "schema_id": schema_id,
                    "is_locked": is_locked,
                    "part_id": part_id,
                    "detail_id": detail_id,
                    "name": name,
                    "nominal": nominal_flt,
                    "usl": usl_flt,
                    "lsl": lsl_flt,
                    "precision": precision,
                    "specification_type_id": specification_type_id,
                    "dimension_type_id": dimension_type_id,
                    "frequency_type_id": frequency_type_id,
                    "gauge_type_id": gauge_type_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspection_schemas, inspection_schema_details])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

# --------------------------------------------------

#region inspection records - inspection records

# routes

@app.route("/inspection_records/inspection_records/create_new_record/", methods = ["POST"])
def inspection_records_inspection_records_create_new_record():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = int(form_data["part_id"])
    schema_id = int(form_data["schema_id"])
    employee_id = int(form_data["employee_id"])
    part_search_term = str(form_data["part_search_term"])
    job_number_search_term = str(form_data["job_number_search_term"])
    started_after_str = str(form_data["started_after"])
    finished_before_str = str(form_data["finished_before"])
    material_type_search_term = str(form_data["material_type_search_term"])
    employee_search_term = str(form_data["employee_search_term"])
    disposition_search_term = str(form_data["disposition_search_term"])
    receiver_number_search_term = str(form_data["receiver_number_search_term"])
    purchase_order_search_term = str(form_data["purchase_order_search_term"])
    lot_number_search_term = str(form_data["lot_number_search_term"])
    supplier_search_term = str(form_data["supplier_search_term"])

    # convert date strings to datetime objects
    started_after = datetime.date(1970, 1, 1)
    finished_before = datetime.date(2100, 1, 1)
    if started_after_str != "":
        started_after = datetime.datetime.strptime(started_after_str, "%Y-%m-%d")
    if finished_before_str != "":
        finished_before = datetime.datetime.strptime(finished_before_str, "%Y-%m-%d")

    try:

        # open the database session
        session = Session(engine)

        # make sure the part exists
        exists = session.query(parts.id)\
            .filter(parts.id == part_id).first()
        if exists is None:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts])
            }

        # make sure this part isn't already associated with an inspection report
        exists = session.query(parts.id, inspection_records.id, inspections.id)\
            .join(parts, (parts.id == inspections.part_id))\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .filter(parts.id == part_id).first()
        if exists is not None:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [parts, inspection_records])
            }

        # close the database session
        session.close()

        # create the new records
        func_inspections_add_inspection(part_id, -1, schema_id, employee_id, 0)

        # return the filtered records
        return func_inspection_records_get_filtered_records(
            part_search_term,
            started_after,
            finished_before,
            material_type_search_term,
            employee_search_term,
            disposition_search_term,
            receiver_number_search_term,
            purchase_order_search_term,
            job_number_search_term,
            lot_number_search_term,
            supplier_search_term
        )

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspection_records/delete_record/", methods = ["POST"])
def inspection_records_inspection_records_delete_record():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = form_data["inspection_record_id"]
    part_search_term = str(form_data["part_search_term"])
    job_number_search_term = str(form_data["job_number_search_term"])
    started_after_str = form_data["started_after"]
    finished_before_str = form_data["finished_before"]
    material_type_search_term = str(form_data["material_type_search_term"])
    employee_search_term = str(form_data["employee_search_term"])
    disposition_search_term = str(form_data["disposition_search_term"])
    receiver_number_search_term = str(form_data["receiver_number_search_term"])
    purchase_order_search_term = str(form_data["purchase_order_search_term"])
    lot_number_search_term = str(form_data["lot_number_search_term"])
    supplier_search_term = str(form_data["supplier_search_term"])

    # convert date strings to datetime objects
    started_after = datetime.date(1970, 1, 1)
    finished_before = datetime.date(2100, 1, 1)
    if started_after_str != "":
        started_after = datetime.datetime.strptime(started_after_str, "%Y-%m-%d")
    if finished_before_str != "":
        finished_before = datetime.datetime.strptime(finished_before_str, "%Y-%m-%d")

    try:

        # open the database connection
        session = Session(engine)

        # make sure the required records exist
        inspection_exists = session.query(inspection_records.id)\
            .filter(inspection_records.id == inspection_record_id).first()
        if inspection_exists is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [inspection_records])
            }

        # get the associated ids
        inspection_ids_query = session.query(inspections.id)\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id).all()
        inspection_ids = [x[0] for x in inspection_ids_query]

        feature_ids_query = session.query(features.id)\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id).all()
        feature_ids = [x[0] for x in feature_ids_query]

        deviation_ids_query = session.query(deviations.id)\
            .join(features, (features.id == deviations.feature_id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id).all()
        deviation_ids = [x[0] for x in deviation_ids_query]

        # delete the referenced records
        session.query(deviations)\
            .filter(deviations.id.in_(deviation_ids)).delete(synchronize_session = False)

        session.query(features)\
            .filter(features.id.in_(feature_ids)).delete(synchronize_session = False)

        session.query(inspections)\
            .filter(inspections.id.in_(inspection_ids)).delete(synchronize_session = False)

        session.query(inspection_records_purchase_orders)\
            .filter(inspection_records_purchase_orders.inspection_record_id == inspection_record_id).delete(synchronize_session = False)

        session.query(inspection_records_lot_numbers)\
            .filter(inspection_records_lot_numbers.inspection_record_id == inspection_record_id).delete(synchronize_session = False)

        session.query(inspection_records)\
            .filter(inspection_records.id == inspection_record_id).delete(synchronize_session = False)

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the filtered records
        return func_inspection_records_get_filtered_records(
            part_search_term,
            started_after,
            finished_before,
            material_type_search_term,
            employee_search_term,
            disposition_search_term,
            receiver_number_search_term,
            purchase_order_search_term,
            job_number_search_term,
            lot_number_search_term,
            supplier_search_term
        )

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspection_records/get_filtered_records/", methods = ["POST"])
def inspection_records_inspection_records_get_filtered_records():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_search_term = str(form_data["part"])
    started_after_str = str(form_data["started_after"])
    finished_before_str = str(form_data["finished_before"])
    material_type_search_term = str(form_data["material_type"])
    employee_search_term = str(form_data["employee"])
    disposition_search_term = str(form_data["disposition"])
    receiver_number_search_term = str(form_data["receiver_number"])
    purchase_order_search_term = str(form_data["purchase_order"])
    job_number_search_term = str(form_data["job_number"])
    lot_number_search_term = str(form_data["lot_number"])
    supplier_search_term = str(form_data["supplier"])

    # convert date strings to datetime objects
    started_after = datetime.date(1970, 1, 1)
    finished_before = datetime.date(2100, 1, 1)
    if started_after_str != "":
        started_after = datetime.datetime.strptime(started_after_str, "%Y-%m-%d")
    if finished_before_str != "":
        finished_before = datetime.datetime.strptime(finished_before_str, "%Y-%m-%d")

    return func_inspection_records_get_filtered_records(
        part_search_term,
        started_after,
        finished_before,
        material_type_search_term,
        employee_search_term,
        disposition_search_term,
        receiver_number_search_term,
        purchase_order_search_term,
        job_number_search_term,
        lot_number_search_term,
        supplier_search_term
    )

@app.route("/inspection_records/inspection_records/get_filtered_parts/", methods = ["POST"])
def inspection_records_inspection_records_get_filtered_parts():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]

    try:

        # start the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.item, parts.drawing)\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%")))\
            .order_by(parts.item.asc(), parts.drawing.asc())\
            .distinct(parts.item, parts.drawing).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, item, drawing in results:
                output_arr.append({
                    "id": id,
                    "item": item,
                    "drawing": drawing,
                    "part_name": f"{item}, {drawing}"
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspection_records/get_filtered_schemas/", methods = ["POST"])
def inspection_records_inspection_records_get_filtered_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    part_id = int(form_data["part_id"])

    # define the output columns
    columns = [
        inspection_schemas.id,
        parts.item,
        parts.drawing,
        parts.revision
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the associated item and drawing from part id
        part_query = session.query(parts.item, parts.drawing)\
            .filter(parts.id == part_id).first()
        if part_query is None:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts])
            }
        item, drawing = part_query

        # query the database
        results = session.query(*columns)\
            .join(parts, (parts.id == inspection_schemas.part_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .filter(and_(parts.item.ilike(item), parts.drawing.ilike(drawing)))\
            .order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for schema_id, item, drawing, revision in results:
                output_arr.append({
                    "schema_id": schema_id,
                    "name": f"{item}, {drawing}, {revision.upper()}"
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspection_schemas])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspection_records/get_filtered_employees/", methods = ["POST"])
def inspection_records_inspection_records_get_filtered_employees():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]

    # define the required fields
    columns = [
        employees.id,
        employees.first_name,
        employees.last_name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .filter(or_(employees.first_name.ilike(f"%{search_term}%"), employees.last_name.ilike(f"%{search_term}%")))\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).all()
        if search_term.isnumeric():
            results = session.query(*columns)\
                .filter(employees.id == search_term)\
                .order_by(employees.last_name.asc(), employees.first_name.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, first_name, last_name in results:
                output_arr.append({
                    "id": id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "name": f"{last_name}, {first_name}"
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [employees])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_inspection_records_get_filtered_records(part_search_term:str, started_after:datetime, finished_before:datetime, material_type_search_term:str, employee_search_term:str, disposition_search_term:str, receiver_number_search_term:str, purchase_order_search_term:str, job_number_search_term:str, lot_number_search_term:str, supplier_search_term:str):

    # define the required fields
    columns = [
        inspection_records.id,
        parts.id,
        parts.item,
        parts.drawing,
        inspections.disposition_id,
        inspection_records.material_type_id,
        inspection_records.employee_id,
        disposition_types.name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(inspections, (inspections.inspection_record_id == inspection_records.id))\
            .join(parts, (inspections.part_id == parts.id))\
            .outerjoin(material_types, (material_types.id == inspection_records.material_type_id))\
            .outerjoin(employees, (employees.id == inspection_records.employee_id))\
            .outerjoin(disposition_types, (disposition_types.id == inspections.disposition_id))\
            .outerjoin(inspection_records_purchase_orders, (inspection_records_purchase_orders.inspection_record_id == inspection_records.id))\
            .outerjoin(purchase_orders, (purchase_orders.id == inspection_records_purchase_orders.purchase_order_id))\
            .outerjoin(receiver_numbers, (receiver_numbers.purchase_order_id == purchase_orders.id))\
            .outerjoin(inspections_job_numbers, (inspections_job_numbers.inspection_id == inspections.id))\
            .outerjoin(job_numbers, (job_numbers.id == inspections_job_numbers.job_number_id))\
            .outerjoin(inspection_records_lot_numbers, (inspection_records_lot_numbers.inspection_record_id == inspection_records.id))\
            .outerjoin(lot_numbers, (lot_numbers.id == inspection_records_lot_numbers.lot_number_id))\
            .outerjoin(suppliers, (suppliers.id == purchase_orders.supplier_id))\
            .filter(inspections.datetime_measured >= started_after)\
            .filter(or_(inspections.datetime_measured <= finished_before, inspections.datetime_measured == None))\
            .filter(or_(parts.item.ilike(f"%{part_search_term}%"), parts.drawing.ilike(f"%{part_search_term}%"), parts.revision.ilike(f"%{part_search_term}%")))\
            .filter(material_types.name.ilike(f"%{material_type_search_term}%"))\
            .filter(or_(employees.first_name.ilike(f"%{employee_search_term}%"), employees.last_name.ilike(f"%{employee_search_term}%")))\
            .filter(disposition_types.name.ilike(f"%{disposition_search_term}%"))\
            .filter(or_(receiver_numbers.name == None, receiver_numbers.name.ilike(f"%{receiver_number_search_term}%")))\
            .filter(or_(purchase_orders.name == None, purchase_orders.name.ilike(f"%{purchase_order_search_term}%")))\
            .filter(or_(job_numbers.name == None, job_numbers.name.ilike(f"%{job_number_search_term}%")))\
            .filter(or_(lot_numbers.name == None, lot_numbers.name.ilike(f"%{lot_number_search_term}%")))\
            .filter(or_(suppliers.name == None, suppliers.name.ilike(f"%{supplier_search_term}%")))\
            .order_by(parts.drawing.asc(), parts.item.asc())\
            .distinct(parts.drawing, parts.item)

        # close the database session
        session.close()

        # return the results
        if len(results.all()) > 0:
            output_arr = []
            for inspection_record_id, part_id, item, drawing, disposition_type_id, material_type_id, employee_id, disposition in results.all():
                output_arr.append({
                    "inspection_record_id": inspection_record_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "disposition_type_id": disposition_type_id,
                    "material_type_id": material_type_id,
                    "employee_id": employee_id,
                    "disposition": disposition
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - inspections

# routes

@app.route("/inspection_records/inspections/add_inspection/", methods = ["POST"])
def inspection_records_inspections_add_inspection():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    schema_id = int(form_data["schema_id"])
    employee_id = int(form_data["employee_id"])
    started_after = datetime.datetime.strptime(str(form_data["started_after"]), "%Y-%m-%dT%H:%M")
    finished_before = datetime.datetime.strptime(str(form_data["finished_before"]), "%Y-%m-%dT%H:%M")
    employee = str(form_data["employee_filter"])
    part_index_str = str(form_data["part_index_filter"])
    revision = str(form_data["revision_filter"])
    inspection_type = int(form_data["inspection_type_filter"])
    disposition_type = int(form_data["disposition_type_filter"])
    shown_job_numbers = list(form_data["shown_job_numbers"])
    shown_purchase_orders = list(form_data["shown_purchase_orders"])
    jn_active = bool(form_data["job_numbers_active"])
    po_active = bool(form_data["purchase_orders_active"])

    if part_index_str == "":
        part_index = -1
    else:
        part_index = int(part_index_str)

    try:

        # open the database session
        session = Session(engine)

        # get the part id
        part_id = session.query(inspection_schemas.part_id)\
            .filter(inspection_schemas.id == schema_id).first()[0]

        # close the database session
        session.close()

        # add the records
        func_inspections_add_inspection(part_id, inspection_record_id, schema_id, employee_id, -1)

        # return an updated list of measurement sets
        return func_inspections_get_filtered_inspections(inspection_record_id, started_after, finished_before, employee, part_index, revision, inspection_type, disposition_type, shown_job_numbers, shown_purchase_orders, jn_active, po_active)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/delete_inspection/", methods = ["POST"])
def inspection_records_inspections_delete_inspection():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    inspection_id = int(form_data["inspection_id"])
    started_after = datetime.datetime.strptime(str(form_data["started_after"]), "%Y-%m-%dT%H:%M")
    finished_before = datetime.datetime.strptime(str(form_data["finished_before"]), "%Y-%m-%dT%H:%M")
    employee = str(form_data["employee_filter"])
    part_index_str = str(form_data["part_index_filter"])
    revision = str(form_data["revision_filter"])
    inspection_type = int(form_data["inspection_type_filter"])
    disposition_type = int(form_data["disposition_type_filter"])
    shown_job_numbers = list(form_data["shown_job_numbers"])
    shown_purchase_orders = list(form_data["shown_purchase_orders"])
    jn_active = bool(form_data["job_numbers_active"])
    po_active = bool(form_data["purchase_orders_active"])

    if part_index_str == "":
        part_index = -1
    else:
        part_index = int(part_index_str)

    try:

        # open the database session
        session = Session(engine)

        # remove associated measurements
        measurements_query = session.query(features)\
            .filter(features.inspection_id == inspection_id)\
            .delete()

        # narrow search to measurement set
        measurement_set_query = session.query(inspections)\
            .filter(inspections.id == inspection_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated list of measurement sets
        return func_inspections_get_filtered_inspections(inspection_record_id, started_after, finished_before, employee, part_index, revision, inspection_type, disposition_type, shown_job_numbers, shown_purchase_orders, jn_active, po_active)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/copy_inspection/", methods = ["POST"])
def inspection_records_inspections_copy_inspection():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    inspection_id = int(form_data["inspection_id"])
    started_after = datetime.datetime.strptime(str(form_data["started_after"]), "%Y-%m-%dT%H:%M")
    finished_before = datetime.datetime.strptime(str(form_data["finished_before"]), "%Y-%m-%dT%H:%M")
    employee = str(form_data["employee_filter"])
    part_index_str = str(form_data["part_index_filter"])
    revision = str(form_data["revision_filter"])
    inspection_type = int(form_data["inspection_type_filter"])
    disposition_type = int(form_data["disposition_type_filter"])
    shown_job_numbers = list(form_data["shown_job_numbers"])
    shown_purchase_orders = list(form_data["shown_purchase_orders"])
    jn_active = bool(form_data["job_numbers_active"])
    po_active = bool(form_data["purchase_orders_active"])

    if part_index_str == "":
        part_index = -1
    else:
        part_index = int(part_index_str)

    # define the query columns
    inspection_columns = [
        inspections.part_index,
        inspections.inspection_record_id,
        inspections.part_id,
        inspections.employee_id,
        inspections.inspection_type_id,
        inspections.disposition_id
    ]
    feature_columns = [
        features.name,
        features.nominal,
        features.usl,
        features.lsl,
        features.measured,
        features.precision,
        features.specification_type_id,
        features.dimension_type_id,
        features.frequency_type_id,
        features.gauge_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the current inspection
        current_inspection = session.query(*inspection_columns).filter(inspections.id == inspection_id).first()
        if current_inspection is None:
            session.close()
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
            }
        current_part_index, current_inspection_record_id, current_part_id, current_employee_id, current_inspection_type_id, current_disposition_id = current_inspection

        # get the current features
        current_features = session.query(*feature_columns).filter(features.inspection_id == inspection_id).all()
        if len(current_features) == 0:
            session.close()
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
            }
        features_arr = []
        for name, nominal, usl, lsl, measured, precision, specification_type_id, dimension_type_id, frequency_type_id, gauge_id in current_features:

            measured_flt = 0
            if measured is None:
                measured_flt = None
            else:
                measured_flt = float(measured)

            features_arr.append({
                "name": name,
                "nominal": float(nominal),
                "usl": float(usl),
                "lsl": float(lsl),
                "measured": measured_flt,
                "precision": int(precision),
                "specification_type_id": int(specification_type_id),
                "dimension_type_id": int(dimension_type_id),
                "frequency_type_id": int(frequency_type_id),
                "gauge_id": int(gauge_id)
            })

        # create the new inspection
        new_inspection = inspections(
            part_index = current_part_index,
            datetime_measured = datetime.datetime.now(),
            inspection_record_id = current_inspection_record_id,
            part_id = current_part_id,
            employee_id = current_employee_id,
            inspection_type_id = current_inspection_type_id,
            disposition_id = current_disposition_id
        )
        session.add(new_inspection)
        session.commit()
        new_inspection_id = new_inspection.id

        # create the new features
        for row in features_arr:
            new_feature = features(
                name = row["name"],
                nominal = row["nominal"],
                usl = row["usl"],
                lsl = row["lsl"],
                measured = row["measured"],
                precision = row["precision"],
                inspection_id = new_inspection_id,
                specification_type_id = row["specification_type_id"],
                dimension_type_id = row["dimension_type_id"],
                frequency_type_id = row["frequency_type_id"],
                gauge_id = row["gauge_id"]
            )
            session.add(new_feature)
        session.commit()

        # close the database session
        session.close()

        # return an updated list of measurement sets
        return func_inspections_get_filtered_inspections(inspection_record_id, started_after, finished_before, employee, part_index, revision, inspection_type, disposition_type, shown_job_numbers, shown_purchase_orders, jn_active, po_active)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/save_edits/", methods = ["POST"])
def inspection_records_inspections_save_edits():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    data_list = list(form_data["data"])

    # parse data object
    data_object = []
    for x in data_list:
        data_object.append({
            "inspection_id": int(x["inspection_id"]),
            "data": {
                "part_index": int(x["part_index"]),
                "inspection_type_id": int(x["inspection_type_id"]),
                "datetime_measured": datetime.datetime.strptime(x["timestamp"], "%Y-%m-%dT%H:%M"),
                "employee_id": int(x["employee_id"])
            }
        })

    try:

        # open the database session
        session = Session(engine)

        # narrow query object to proper scope
        rows_affected = 0
        for x in data_object:
            inspections_query = session.query(inspections)\
                .filter(inspections.id == x["inspection_id"])

            is_affected = 0
            for k, v in x["data"].items():
                is_affected += inspections_query.update({ k: v })

            if is_affected > 0:
                rows_affected += 1

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated list of measurement sets
        return {
            "status": "alert",
            "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [inspections])
        }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/get_filtered_schemas/", methods = ["POST"])
def inspection_records_inspections_get_filtered_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    search_term = str(form_data["search_term"])

    # define the output columns
    columns = [
        inspection_schemas.id,
        parts.id,
        parts.item,
        parts.drawing,
        parts.revision
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the item and drawing from the provided inspection id
        part_query = session.query(parts.item, parts.drawing)\
            .join(inspections, (inspections.part_id == parts.id))\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id)\
            .order_by(parts.item.asc(), parts.drawing.asc())
        if part_query.first() is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspections, inspection_records])
            }
        item, drawing = part_query.first()

        # get the list of matching measurement set schemas
        set_schema_query = session.query(*columns)\
            .join(parts, (parts.id == inspection_schemas.part_id))\
            .filter(func.lower(parts.item) == func.lower(item))\
            .filter(func.lower(parts.drawing) == func.lower(drawing))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(set_schema_query) > 0:
            output_arr = []
            for schema_id, part_id, item, drawing, revision in set_schema_query:
                output_arr.append({
                    "schema_id": schema_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "revision": revision.upper(),
                    "name": f"{item}, {drawing}, {revision.upper()}"
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspection_schemas])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/get_filtered_inspections/", methods = ["POST"])
def inspection_records_inspections_get_filtered_inspections():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    started_after = datetime.datetime.strptime(str(form_data["started_after"]), "%Y-%m-%dT%H:%M")
    finished_before = datetime.datetime.strptime(str(form_data["finished_before"]), "%Y-%m-%dT%H:%M")
    employee = str(form_data["employee_filter"])
    part_index_str = str(form_data["part_index_filter"])
    revision = str(form_data["revision_filter"])
    inspection_type = int(form_data["inspection_type_filter"])
    disposition_type = int(form_data["disposition_type_filter"])
    shown_job_numbers = list(form_data["shown_job_numbers"])
    shown_purchase_orders = list(form_data["shown_purchase_orders"])
    jn_active = bool(form_data["job_numbers_active"])
    po_active = bool(form_data["purchase_orders_active"])

    if part_index_str == "":
        part_index = -1
    else:
        part_index = int(part_index_str)

    return func_inspections_get_filtered_inspections(inspection_record_id, started_after, finished_before, employee, part_index, revision, inspection_type, disposition_type, shown_job_numbers, shown_purchase_orders, jn_active, po_active)

@app.route("/inspection_records/inspections/get_job_numbers/", methods = ["POST"])
def inspection_records_inspections_get_job_numbers():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_numbers.id, job_numbers.name)\
            .join(inspections_job_numbers, (inspections_job_numbers.job_number_id == job_numbers.id))\
            .join(inspections, (inspections.id == inspections_job_numbers.inspection_id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .order_by(job_numbers.name.asc()).distinct(job_numbers.name).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "is_active": False
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/inspections/get_purchase_orders/", methods = ["POST"])
def inspection_records_inpsections_get_purchase_orders():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id, purchase_orders.name)\
            .join(inspection_records_purchase_orders, (inspection_records_purchase_orders.purchase_order_id == purchase_orders.id))\
            .join(inspection_records, (inspection_records.id == inspection_records_purchase_orders.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id)\
            .order_by(purchase_orders.name.asc()).distinct(purchase_orders.name).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "is_active": False
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_inspections_add_inspection(part_id:int, inspection_record_id:int, schema_id:int, employee_id:int, part_index:int):

    # schema detail columns
    schema_details_columns = [
        inspection_schema_details.name,
        inspection_schema_details.nominal,
        inspection_schema_details.usl,
        inspection_schema_details.lsl,
        inspection_schema_details.precision,
        inspection_schema_details.specification_type_id,
        inspection_schema_details.dimension_type_id,
        inspection_schema_details.frequency_type_id,
        inspection_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the inspection schema details
        schema_query = session.query(parts.item, parts.drawing)\
            .join(inspection_schemas, (inspection_schemas.part_id == parts.id))\
            .filter(inspection_schemas.id == schema_id).first()
        if schema_query is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspection_schemas])
            }
        schema_item, schema_drawing = schema_query

        # get the part details
        part_query = session.query(parts.item, parts.drawing)\
            .filter(parts.id == part_id).first()
        if part_query is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts])
            }
        part_item, part_drawing = part_query

        # measurement_set if schema and part match up
        if schema_item != part_item and schema_drawing != part_drawing:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.generic, err_msg = "the provided schema does not match the provided part")
            }

        # create a new inspection report if the provided inspection_id is -1, or ensure it exists
        if inspection_record_id == -1:

            # create a new inspection report
            inspection_record_query = inspection_records(
                material_type_id = 0,
                employee_id = employee_id,
            )
            session.add(inspection_record_query)
            session.commit()
            inspection_record_id = inspection_record_query.id
        else:

            # get the inspection record details
            inspection_record_query = session.query(parts.item, parts.drawing)\
                .join(inspections, (inspections.part_id == parts.id))\
                .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
                .filter(inspection_records.id == inspection_record_id).first()
            if inspection_record_query is None:
                session.close()
                return {
                    "status": "alert",
                    "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspections, inspection_records])
                }
            inspection_item, inspection_drawing = inspection_record_query

            # make sure the inspection record and part match up
            if inspection_item != part_item and inspection_drawing != part_drawing:
                session.close()
                return {
                    "status": "alert",
                    "response": text_response(stack()[0][3], message_type.generic, err_msg = "the provided inspection report does not match the provided part")
                }

        # calculate the part index if the provided part_index is -1
        if part_index == -1:
            part_index_arr = session.query(inspections.part_index)\
                .filter(inspections.part_id == part_id)\
                .filter(inspections.inspection_record_id == inspection_record_id).all()
            part_index = max([x[0] for x in part_index_arr]) + 1

        # create a new inspection
        inspection_query = inspections(
            part_index = part_index,
            datetime_measured = datetime.datetime.now(),
            inspection_record_id = inspection_record_id,
            part_id = part_id,
            employee_id = employee_id,
            inspection_type_id = 0,
            disposition_id = 2
        )
        session.add(inspection_query)
        session.commit()
        inspection_id = inspection_query.id

        # get the schema details
        schema_details = session.query(*schema_details_columns)\
            .filter(inspection_schema_details.schema_id == schema_id)\
            .order_by(inspection_schema_details.name.asc()).all()
        schema_details_list = []
        for name, nominal, usl, lsl, precision, spectype, dimetype, freqtype, gauge_type_id in schema_details:

            gauge_id = session.query(gauges.id)\
                .filter(gauges.gauge_type_id == gauge_type_id)\
                .order_by(gauges.name.asc())\
                .first()[0]

            schema_details_list.append({
                "name": name,
                "nominal": nominal,
                "usl": usl,
                "lsl": lsl,
                "precision": precision,
                "specification_type_id": spectype,
                "dimension_type_id": dimetype,
                "frequency_type_id": freqtype,
                "gauge_id": gauge_id
            })

        # create the feature records
        for obj in schema_details_list:
            features_query = features(
                name = obj["name"],
                nominal = obj["nominal"],
                usl = obj["usl"],
                lsl = obj["lsl"],
                precision = obj["precision"],
                inspection_id = inspection_id,
                specification_type_id = obj["specification_type_id"],
                dimension_type_id = obj["dimension_type_id"],
                frequency_type_id = obj["frequency_type_id"],
                gauge_id = obj["gauge_id"]
            )
            session.add(features_query)
        session.commit()

        # close the database session
        session.close()

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

def func_inspections_get_filtered_inspections(inspection_record_id:int, started_after:datetime, finished_before:datetime, employee_filter:str, part_index_filter:int, revision_filter:str, inspection_type_filter:int, disposition_type_filter:int, shown_job_numbers:list, shown_purchase_orders:list, jn_active:bool, po_active:bool):

    # define the output columns
    columns = [
        inspections.id,
        inspections.datetime_measured,
        inspections.part_index,
        inspections.employee_id,
        inspections.inspection_record_id,
        inspections.inspection_type_id,
        inspections.disposition_id,
        parts.item,
        parts.drawing,
        parts.revision
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the list of matching inspection schemas
        inspections_query = session.query(*columns)\
            .join(parts, (parts.id == inspections.part_id))\
            .join(employees, (employees.id == inspections.employee_id))\
            .outerjoin(inspections_job_numbers, (inspections_job_numbers.inspection_id == inspections.id))\
            .outerjoin(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .outerjoin(inspection_records_purchase_orders, (inspection_records_purchase_orders.inspection_record_id == inspection_records.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(parts.revision.ilike(f"%{revision_filter}%"))\
            .filter(and_(inspections.datetime_measured >= started_after, inspections.datetime_measured <= finished_before))\
            .filter(or_(employees.first_name.ilike(f"%{employee_filter}%"), employees.last_name.ilike(f"%{employee_filter}%")))

        # additional filters
        if jn_active:
            inspections_query = inspections_query.filter(inspections_job_numbers.job_number_id.in_(shown_job_numbers))
        if po_active:
            inspections_query = inspections_query.filter(inspection_records_purchase_orders.purchase_order_id.in_(shown_purchase_orders))
        if part_index_filter > -1:
            inspections_query = inspections_query.filter(inspections.part_index == part_index_filter)
        if inspection_type_filter > -1:
            inspections_query = inspections_query.filter(inspections.inspection_type_id == inspection_type_filter)
        if disposition_type_filter > -1:
            inspections_query = inspections_query.filter(inspections.disposition_id == disposition_type_filter)

        # convert to list of tuples
        inspections_query = inspections_query\
            .order_by(inspections.part_index.asc(), parts.revision.asc(), inspections.datetime_measured.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(inspections_query) > 0:
            output_arr = []
            for inspection_id, timestamp, part_index, employee_id, current_inspection_record_id, inspection_type_id, disposition_type_id, item, drawing, revision in inspections_query:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M"),
                    "part_index": part_index,
                    "employee_id": employee_id,
                    "inspection_record_id": current_inspection_record_id,
                    "inspection_type_id": inspection_type_id,
                    "disposition_type_id": disposition_type_id,
                    "item": item,
                    "drawing": drawing,
                    "revision": revision.upper()
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - features

@app.route("/inspection_records/features/get_filtered_features/", methods = ["POST"])
def inspection_records_features_get_filtered_features():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["identity"]["inspection_record_id"])
    item = str(form_data["identity"]["item"])
    drawing = str(form_data["identity"]["drawing"])
    name = str(form_data["content"]["name"])
    frequency_type_id = int(form_data["content"]["frequency_type_id"])
    has_deviations = int(form_data["content"]["has_deviations"])
    inspector_id = int(form_data["content"]["employee_id"])
    gauge_id = int(form_data["content"]["gauge_id"])
    gauge_type_id = int(form_data["content"]["gauge_type_id"])
    specification_type_id = int(form_data["content"]["specification_type_id"])
    dimension_type_id = int(form_data["content"]["dimension_type_id"])
    inspection_type_id = int(form_data["content"]["inspection_type_id"])
    revision = str(form_data["content"]["revision"])
    part_index = int(form_data["content"]["part_index"])

    # make a list of acceptable inspection ids
    inspection_ids = []
    for obj in list(form_data["content"]["inspections"]):
        if bool(int(obj["display_state"])):
            inspection_ids.append(int(obj["inspection_id"]))

    # run the required function
    return func_features_get_filtered_features(
        inspection_record_id,
        item,
        drawing,
        frequency_type_id,
        name,
        has_deviations,
        inspector_id,
        gauge_id,
        gauge_type_id,
        specification_type_id,
        dimension_type_id,
        inspection_type_id,
        revision,
        part_index,
        inspection_ids
    )

@app.route("/inspection_records/features/save_features/", methods = ["POST"])
def inspection_records_features_save_features():

    # interpret the posted data
    form_data = json.loads(request.data)

    # extract the required information
    data = form_data["data"]

    try:

        if len(data) > 0:

            # convert the raw data
            my_data = {}
            for row in data:

                # make sure we're only pulling info we want
                if row["column"]["key"] == "measured" or row["column"]["key"] == "gauge_id":

                    # get the feature id
                    meas_id = row["row"]["feature_id"]

                    # check if the feature id already exists in dictionary
                    if meas_id in my_data:
                        my_data[meas_id].append({ row["column"]["key"]: row["row"]["value"] })
                    else:
                        my_data[meas_id] = [{ row["column"]["key"]: row["row"]["value"] }]

            # open the database session
            session = Session(engine)

            # iterate through the data object
            rows_affected = 0
            for k, v in my_data.items():
                results = session.query(features).filter(features.id == k)
                is_affected = 0
                for obj in v:
                    is_affected = results.update(obj)
                if is_affected > 0:
                    rows_affected += 1

            # commit the changes
            session.commit()

            # close the database session
            session.close()

            # return the results
            if rows_affected > 0:
                return {
                    "status": "alert",
                    "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [features])
                }
            else:
                return {
                    "status": "alert",
                    "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [features])
                }
        else:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.generic, err_msg = "no data passed to flask server")
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/features/tunnel_to_physical_part/", methods = ["POST"])
def inspection_records_features_tunnel_to_physical_part():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    part_id = int(form_data["part_id"])
    part_index = int(form_data["part_index"])

    try:

        # open the database connection
        session = Session(engine)

        # get the part details
        part_query = session.query(parts.item, parts.drawing, parts.revision)\
            .filter(parts.id == part_id).first()
        if part_query is None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts])
            }
        item, drawing, revision = part_query

        # close the database connection
        session.close()

        # run the required function
        return func_features_get_filtered_features(
            inspection_record_id,
            item,
            drawing,
            -1,
            "",
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            revision,
            part_index,
            None
        )

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_reports/features/get_filter_parameters/", methods = ["POST"])
def inspection_records_features_get_filter_parameters():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])
    item = form_data["item"]
    drawing = form_data["drawing"]

    try:

        # open the database session
        session = Session(engine)

        # measurement type list
        inspection_types_query = session.query(inspection_types.id, inspection_types.name)\
            .join(inspections, (inspections.inspection_type_id == inspection_types.id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}")))\
            .order_by(inspection_types.name.asc()).distinct(inspection_types.name).all()

        # part index list
        part_index_query = session.query(inspections.part_index)\
            .join(parts, (parts.id == inspections.part_id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .order_by(inspections.part_index.asc()).distinct(inspections.part_index).all()

        # revisions list
        revisions_query = session.query(parts.revision)\
            .join(inspections, (parts.id == inspections.part_id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .order_by(parts.revision.asc()).distinct(parts.revision).all()

        # frequency type list
        frequency_types_query = session.query(frequency_types.id, frequency_types.name)\
            .join(features, (features.frequency_type_id == frequency_types.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(frequency_types.name.asc()).distinct(frequency_types.name).all()

        # inspectors list
        inspectors_query = session.query(employees.id, employees.first_name, employees.last_name)\
            .join(inspections, (inspections.employee_id == employees.id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).distinct(employees.first_name, employees.last_name).all()

        # gauges list
        gauges_query = session.query(gauges.id, gauges.name)\
            .join(features, (features.gauge_id == gauges.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauges.name.asc()).distinct(gauges.name).all()

        # gauges types list
        gauge_types_query = session.query(gauge_types.id, gauge_types.name)\
            .join(gauges, (gauges.gauge_type_id == gauge_types.id))\
            .join(features, (features.gauge_id == gauges.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauge_types.name.asc()).distinct(gauge_types.name).all()

        # specification types list
        specification_types_query = session.query(specification_types.id, specification_types.name)\
            .join(features, (features.specification_type_id == specification_types.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(specification_types.name.asc()).distinct(specification_types.name).all()

        # dimension types list
        dimension_types_query = session.query(dimension_types.id, dimension_types.name)\
            .join(features, (features.dimension_type_id == dimension_types.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .filter(inspections.inspection_record_id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(dimension_types.name.asc()).distinct(dimension_types.name).all()

        # close the database session
        session.close()

        # return the results
        inspection_types_list = []
        for id, name in inspection_types_query:
            inspection_types_list.append({
                "id": id,
                "name": name
            })

        part_index_list = []
        for index in part_index_query:
            part_index_list.append({
                "id": index[0],
                "name": index[0]
            })

        revisions_list = []
        for revision in revisions_query:
            revisions_list.append({
                "id": revision[0],
                "name": revision[0].upper()
            })

        frequency_types_list = []
        for id, name in frequency_types_query:
            frequency_types_list.append({
                "id": id,
                "name": name
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

        dimension_types_list = []
        for id, name in dimension_types_query:
            dimension_types_list.append({
                "id": id,
                "name": name
            })

        # return the data object
        return {
            "status": "ok",
            "response": {
                "inspection_types": inspection_types_list,
                "frequency_types": frequency_types_list,
                "inspectors": inspectors_list,
                "gauges": gauges_list,
                "gauge_types": gauge_types_list,
                "specification_types": specification_types_list,
                "dimension_types": dimension_types_list,
                "revisions": revisions_list,
                "part_indices": part_index_list
            }
        }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_features_get_filtered_features(inspection_record_id:int, item:str, drawing:str, frequency_type_id:int, name:str, has_deviations:int, inspector_id:int, gauge_id:int, gauge_type_id:int, specification_type_id:int, dimension_type_id:int, inspection_type_id:int, revision:str, part_index:int, inspection_ids:list):

    # define the columns
    columns = [
        inspections.id,
        inspections.part_index,
        inspections.datetime_measured,
        inspections.employee_id,
        parts.id,
        parts.revision,
        features.id,
        features.name,
        features.nominal,
        features.usl,
        features.lsl,
        features.measured,
        features.precision,
        gauges.id,
        gauge_types.id,
        gauge_types.name,
        specification_types.name,
        dimension_types.name,
        frequency_types.name,
        inspection_types.name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(gauges, (features.gauge_id == gauges.id))\
            .join(gauge_types, (gauges.gauge_type_id == gauge_types.id))\
            .join(inspections, (inspections.id == features.inspection_id))\
            .join(parts, (inspections.part_id == parts.id))\
            .join(inspection_records, (inspections.inspection_record_id == inspection_records.id))\
            .join(specification_types, (features.specification_type_id == specification_types.id))\
            .join(dimension_types, (features.dimension_type_id == dimension_types.id))\
            .join(frequency_types, (features.frequency_type_id == frequency_types.id))\
            .join(inspection_types, (inspections.inspection_type_id == inspection_types.id))\
            .filter(inspection_records.id == inspection_record_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .filter(features.name.ilike(f"%{name}%"))\
            .filter(parts.revision.ilike(f"%{revision}%"))

        if part_index > -1:
            results = results.filter(inspections.part_index == part_index)
        if dimension_type_id > -1:
            results = results.filter(dimension_types.id == dimension_type_id)
        if frequency_type_id > -1:
            results = results.filter(features.frequency_type_id == frequency_type_id)
        if has_deviations == 0:
            results = results.filter(features.id.notin_(session.query(deviations.feature_id)))
        elif has_deviations == 1:
            results = results.filter(features.id.in_(session.query(deviations.feature_id)))
        if inspector_id > -1:
            results = results.filter(inspections.employee_id == inspector_id)
        if gauge_id > -1:
            results = results.filter(features.gauge_id == gauge_id)
        if gauge_type_id > -1:
            results = results.filter(gauges.gauge_type_id == gauge_type_id)
        if specification_type_id > -1:
            results = results.filter(features.specification_type_id == specification_type_id)
        if inspection_type_id > -1:
            results = results.filter(inspections.inspection_type_id == inspection_type_id)
        if inspection_ids is not None:
            results = results.filter(features.inspection_id.in_(inspection_ids))

        # convert to a list
        measurement_list = results\
            .order_by(inspections.id.asc(), inspections.part_id.asc(), parts.revision.asc(), features.id.asc()).all()

        # get the list of features that have deviations
        deviations_list = [{ "feature_id": x[0], "deviation_type_id": x[1] } for x in session.query(deviations.feature_id, deviations.deviation_type_id).all()]
        temp_deviations = [x["feature_id"] for x in deviations_list if x["deviation_type_id"] == 0]
        perm_deviations = [x["feature_id"] for x in deviations_list if x["deviation_type_id"] == 1]

        # close the database session
        session.close()

        # return the results
        if len(measurement_list) > 0:

            # assemble measurements output
            output_arr = []
            for inspection_id, part_index, timestamp, employee_id, part_id, revision, feature_id, name, nominal, usl, lsl, measured, precision, gauge_id, gauge_type_id, gauge_type, specification_type, dimension_type, frequency_type, inspection_type in measurement_list:

                # determine data input type (numerical or boolean)
                input_type = "numerical"
                if gauge_type_id == 6 or gauge_type_id == 10 or gauge_type_id == 11 or gauge_type_id == 13:
                    input_type = "boolean"

                # parse to floats
                nominal_flt = float(nominal)
                usl_flt = float(usl)
                lsl_flt = float(lsl)

                # evaluate measurements
                state = "incomplete"
                measured_flt = 0
                if measured is None:
                    measured_flt = None
                else:
                    measured_flt = float(measured)
                    if usl_flt >= measured_flt and lsl_flt <= measured_flt:
                        state = "pass"
                    else:
                        state = "fail"

                # inspection for deviation flag
                if (feature_id in temp_deviations) and (feature_id not in perm_deviations):
                    deviation_code = "*"
                elif (feature_id not in temp_deviations) and (feature_id in perm_deviations):
                    deviation_code = "**"
                elif (feature_id in temp_deviations) and (feature_id in perm_deviations):
                    deviation_code = "***"
                else:
                    deviation_code = ""

                output_arr.append({
                    "inspection_record_id": inspection_record_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "timestamp": timestamp.strftime("%Y-%m-%d, %H:%M"),
                    "deviation_code": deviation_code,
                    "feature_id": feature_id,
                    "inspection_id": inspection_id,
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
                    "gauge_type_id": gauge_type_id,
                    "gauge_type": gauge_type,
                    "specification_type": specification_type,
                    "dimension_type": dimension_type,
                    "inspection_type": inspection_type,
                    "frequency_type": frequency_type,
                    "state": state,
                    "input_type": input_type
                })

            # return the data object
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - manufactured

# routes

@app.route("/inspection_records/manufactured/add_associated_job_number/", methods = ["POST"])
def inspection_records_manufactured_add_associated_job_number():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    inspection_id = int(form_data["inspection_id"])
    job_number_id = int(form_data["job_number_id"])

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        exists = session.query(inspections_job_numbers.id)\
            .filter(inspections_job_numbers.inspection_id == inspection_id)\
            .filter(inspections_job_numbers.job_number_id == job_number_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [inspections_job_numbers])
            }

        # add the association
        session.add(inspections_job_numbers(**{
            "inspection_id": inspection_id,
            "job_number_id": job_number_id,
        }))

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # reacquire the association list
        return func_manufactured_get_associated_job_numbers(inspection_record_id, search_term)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/manufactured/save_associated_job_numbers/", methods = ["POST"])
def inspection_records_manufactured_save_associated_job_numbers():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    raw_data = list(form_data["data"])

    # convert the raw data
    clean_data = []
    for x in raw_data:
        clean_data.append({
            "id": int(x["id"]),
            "data": {
                "full_inspect_interval": int(x["full_inspect_interval"]),
                "released_qty": int(x["released_qty"]),
                "completed_qty": int(x["completed_qty"])
            }
        })

    try:

        # open the database session
        session = Session(engine)

        # update the database
        rows_affected = 0
        for x in clean_data:
            results = session.query(job_numbers).filter(job_numbers.id == int(x["id"]))
            is_affected = 0
            for k, v in x["data"].items():
                is_affected += results.update({ k: v })
            if is_affected > 0:
                rows_affected += 1

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if rows_affected > 0:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [job_numbers])
            }
        else:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [job_numbers])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/manufactured/delete_associated_job_number/", methods = ["POST"])
def inspection_records_manufactured_delete_associated_job_number():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    inspection_id = int(form_data["inspection_id"])
    job_number_id = int(form_data["job_number_id"])

    try:

        # open the database session
        session = Session(engine)

        # delete the associated record
        rows_deleted = session.query(inspections_job_numbers)\
            .filter(inspections_job_numbers.inspection_id == inspection_id)\
            .filter(inspections_job_numbers.job_number_id == job_number_id)\
            .delete()

        # commit the changes
        if rows_deleted > 0:
            session.commit()

        # close the database session
        session.close()

        # reacquire the association list
        return func_manufactured_get_associated_job_numbers(inspection_record_id, search_term)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/manufactured/get_associated_job_numbers/", methods = ["POST"])
def inspection_records_manufactured_get_associated_job_numbers():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])

    # return the results
    return func_manufactured_get_associated_job_numbers(inspection_record_id, search_term)

@app.route("/inspection_records/manufactured/get_filtered_job_numbers/", methods = ["POST"])
def inspection_records_manufactured_get_filtered_job_numbers():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_numbers.id, job_numbers.name)\
            .filter(job_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(job_numbers.name.asc()).all()

        # close the database session
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [job_numbers])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/manufactured/get_filtered_inspections/", methods = ["POST"])
def inspection_records_manufactured_get_filtered_inspections():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_record_id = int(form_data["inspection_record_id"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(inspections.id, inspections.part_index, parts.revision, inspections.datetime_measured)\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .join(parts, (parts.id == inspections.part_id))\
            .filter(inspection_records.id == inspection_record_id)\
            .order_by(inspections.datetime_measured.asc(), inspections.part_index.asc(), parts.revision.asc(), inspections.id.asc())\
            .all()
        # results = session.query(parts.id, parts.item, parts.drawing, parts.revision)\
        #     .join(inspections, (inspections.part_id == parts.id))\
        #     .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
        #     .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
        #     .filter(inspection_records.id == inspection_record_id)\
        #     .order_by(parts.drawing.asc(), parts.revision.asc(), parts.item.asc())\
        #     .distinct(parts.drawing, parts.revision, parts.item).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, part_index, revision, datetime_measured in results:
                output_arr.append({
                    "id": id,
                    "name": f"{part_index}, {revision.upper()}, {datetime_measured.strftime('%Y-%m-%d, %H:%M')}"
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_found, tables = [parts, inspections, inspection_records])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_manufactured_get_associated_job_numbers(inspection_record_id:int, search_term:str):

    # define the output columns
    columns = [
        job_numbers.id,
        job_numbers.name,
        job_numbers.full_inspect_interval,
        job_numbers.released_qty,
        job_numbers.completed_qty,
        parts.revision,
        parts.id,
        inspections.id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(inspections_job_numbers, (inspections_job_numbers.job_number_id == job_numbers.id))\
            .join(inspections, (inspections.id == inspections_job_numbers.inspection_id))\
            .join(inspection_records, (inspection_records.id == inspections.inspection_record_id))\
            .join(parts, (parts.id == inspections.part_id))\
            .filter(inspection_records.id == inspection_record_id)\
            .filter(or_(parts.revision.ilike(f"%{search_term}%"), job_numbers.name.ilike(f"%{search_term}%")))\
            .order_by(job_numbers.name.asc())\
            .distinct(job_numbers.name).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name, full_inspect_interval, released_qty, completed_qty, revision, part_id, inspection_id in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "full_inspect_interval": full_inspect_interval,
                    "released_qty": released_qty,
                    "completed_qty": completed_qty,
                    "revision": revision.upper(),
                    "part_id": part_id,
                    "inspection_id": inspection_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - received

# routes

@app.route("/inspection_records/received/assign_purchase_order_association/", methods = ["POST"])
def inspection_records_received_assign_purchase_order_asociation():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        exists = session.query(inspection_records_purchase_orders.id)\
            .filter(inspection_records_purchase_orders.inspection_record_id == inspection_record_id)\
            .filter(inspection_records_purchase_orders.purchase_order_id == purchase_order_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [inspection_records_purchase_orders])
            }
        
        # add the association
        session.add(inspection_records_purchase_orders(**{
            "inspection_record_id": inspection_record_id,
            "purchase_order_id": purchase_order_id
        }))

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated association list
        return func_received_get_filtered_purchase_order_associations(search_term, inspection_record_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/assign_receiver_number_association/", methods = ["POST"])
def inspection_records_received_assign_receiver_number_association():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    receiver_number_id = int(form_data["receiver_number_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        exists = session.query(receiver_numbers.id)\
            .filter(receiver_numbers.id == receiver_number_id)\
            .filter(receiver_numbers.purchase_order_id == purchase_order_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [receiver_numbers])
            }

        # add the association
        is_affected = session.query(receiver_numbers)\
            .filter(receiver_numbers.id == receiver_number_id)\
            .update({
                "purchase_order_id": purchase_order_id
            })
        if is_affected == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [receiver_numbers])
            }

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated association list
        return func_received_get_filtered_child_associations(search_term, purchase_order_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/set_associated_supplier/", methods = ["POST"])
def inspection_records_received_set_associated_supplier():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    purchase_order_id = int(form_data["purchase_order_id"])
    supplier_id = int(form_data["supplier_id"])

    # account for null condition
    if supplier_id == -1:
        supplier_id = None

    try:

        # open the database session
        session = Session(engine)

        # assign the association
        is_affected = session.query(purchase_orders)\
            .filter(purchase_orders.id == purchase_order_id)\
            .update({
                "supplier_id": supplier_id
            })
        if is_affected == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [purchase_orders])
            }
        else:
            session.commit()
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = is_affected, tables = [purchase_orders])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/save_received_quantities/", methods = ["POST"])
def inspection_records_received_save_received_quantities():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    raw_data = list(form_data["data"])

    # convert the raw data
    clean_data = []
    for x in raw_data:
        clean_data.append({
            "id": int(x["id"]),
            "data": {
                "received_qty": int(x["received_qty"])
            }
        })

    try:

        # open the database session
        session = Session(engine)

        # update the database
        rows_affected = 0
        for x in clean_data:
            results = session.query(receiver_numbers).filter(receiver_numbers.id == int(x["id"]))
            is_affected = 0
            for k, v in x["data"].items():
                is_affected += results.update({ k: v })
            if is_affected > 0:
                rows_affected += 1
        if rows_affected == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [receiver_numbers])
            }
        else:
            session.commit()
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [receiver_numbers])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/remove_purchase_order_association/", methods = ["POST"])
def inspection_records_received_remove_purchase_order_association():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    try:

        # open the database session
        session = Session(engine)

        # delete the records
        rows_affected = session.query(inspection_records_purchase_orders)\
            .filter(inspection_records_purchase_orders.inspection_record_id == inspection_record_id)\
            .filter(inspection_records_purchase_orders.purchase_order_id == purchase_order_id)\
            .delete()
        if rows_affected == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_deleted, tables = [inspection_records_purchase_orders])
            }
        else:
            session.commit()
            session.close()

        # return the updated list
        return func_received_get_filtered_purchase_order_associations(search_term, inspection_record_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/remove_receiver_number_association/", methods = ["POST"])
def inspection_records_received_remove_receiver_number_association():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    purchase_order_id = int(form_data["purchase_order_id"])
    receiver_number_id = int(form_data["receiver_number_id"])

    try:

        # open the database session
        session = Session(engine)

        # delete the records
        rows_affected = session.query(receiver_numbers)\
            .filter(receiver_numbers.id == receiver_number_id)\
            .update({
                "purchase_order_id": None
            })
        if rows_affected == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [inspection_records_purchase_orders])
            }
        else:
            session.commit()
            session.close()

        # return the updated list
        return func_received_get_filtered_child_associations(search_term, purchase_order_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/get_filtered_purchase_order_associations/", methods = ["POST"])
def inspection_records_received_get_filtered_purchase_order_associations():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])

    # return the list of associations
    return func_received_get_filtered_purchase_order_associations(search_term, inspection_record_id)

@app.route("/inspection_records/received/get_filtered_child_associations/", methods = ["POST"])
def inspection_records_received_get_filtered_child_associations():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    purchase_order_id = int(form_data["purchase_order_id"])

    # return the found associations
    return func_received_get_filtered_child_associations(search_term, purchase_order_id)

@app.route("/inspection_records/received/get_filtered_purchase_order_options/", methods = ["POST"])
def inspection_records_received_get_filtered_purchase_order_options():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id, purchase_orders.name, purchase_orders.supplier_id)\
            .filter(purchase_orders.name.ilike(f"%{search_term}%"))\
            .order_by(purchase_orders.name.asc())\
            .all()

        # close the database session
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/get_filtered_receiver_number_options/", methods = ["POST"])
def inspection_records_received_get_filtered_receiver_number_options():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(receiver_numbers.id, receiver_numbers.name, receiver_numbers.received_qty, receiver_numbers.purchase_order_id)\
            .filter(receiver_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(receiver_numbers.name.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name, received_qty, current_purchase_order_id in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "received_qty": received_qty,
                    "purchase_order_id": current_purchase_order_id
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_records/received/get_filtered_supplier_options/", methods = ["POST"])
def inspection_records_received_get_filtered_supplier_options():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(suppliers.id, suppliers.name)\
            .filter(suppliers.name.ilike(f"%{search_term}%"))\
            .order_by(suppliers.name.asc())\
            .all()

        # close the database session
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

# recycled methods

def func_received_get_filtered_purchase_order_associations(search_term:str, inspection_record_id:int):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(purchase_orders.id, purchase_orders.name, inspection_records_purchase_orders.inspection_record_id)\
            .join(purchase_orders, (purchase_orders.id == inspection_records_purchase_orders.purchase_order_id))\
            .filter(purchase_orders.name.ilike(f"%{search_term}%"))\
            .filter(inspection_records_purchase_orders.inspection_record_id == inspection_record_id)\
            .order_by(purchase_orders.name.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for current_purchase_order_id, name, current_inspection_record_id in results:
                output_arr.append({
                    "purchase_order_id": current_purchase_order_id,
                    "name": name,
                    "inspection_record_id": current_inspection_record_id
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

def func_received_get_filtered_child_associations(search_term:str, purchase_order_id:int):

    try:

        # open the database session
        session = Session(engine)

        # get the supplier id
        supplier_id = session.query(purchase_orders.supplier_id)\
            .filter(purchase_orders.id == purchase_order_id)\
            .first()[0]
        
        # get the receiver numbers
        receiver_numbers_query = session.query(receiver_numbers.id, receiver_numbers.name, receiver_numbers.received_qty, receiver_numbers.purchase_order_id)\
            .filter(receiver_numbers.purchase_order_id == purchase_order_id)\
            .filter(receiver_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(receiver_numbers.name.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(receiver_numbers_query) > 0:
            output_arr = []
            for id, name, received_qty, current_purchase_order_id in receiver_numbers_query:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "received_qty": received_qty,
                    "purchase_order_id": current_purchase_order_id
                })
            return {
                "status": "ok",
                "response": {
                    "supplier_id": supplier_id,
                    "receiver_numbers": output_arr
                }
            }
        else:
            return {
                "status": "ok",
                "response": {
                    "supplier_id": supplier_id,
                    "receiver_numbers": None
                }
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - lot numbers

# routes

@app.route("/inspection_records/lot_numbers/assign_lot_number/", methods = ["POST"])
def inspection_records_lot_numbers_assign_lot_number():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_lot_numbers_assign(
        search_term,
        inspection_record_id,
        lot_number_id
    )

@app.route("/inspection_records/lot_numbers/unassign_lot_number/", methods = ["POST"])
def inspection_records_lot_numbers_unassign_lot_number():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_lot_numbers_association_remove(
        search_term,
        inspection_record_id,
        lot_number_id
    )

@app.route("/inspection_records/lot_numbers/get_filtered_options/", methods = ["POST"])
def inspection_records_lot_numbers_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_lot_numbers_get_filtered_options(
        search_term
    )

@app.route("/inspection_records/lot_numbers/get_filtered_associations/", methods = ["POST"])
def inspection_records_lot_numbers_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_record_id = int(form_data["inspection_record_id"])

    return func_lot_numbers_get_filtered_associations(
        search_term,
        inspection_record_id
    )

# recycled methods

def func_lot_numbers_assign(search_term:str, inspection_record_id:int, lot_number_id:int):

    try:

        # open the database session
        session = Session(engine)

        # measurement_set if the association already exists
        results = session.query(inspection_records_lot_numbers.inspection_record_id)\
            .filter(inspection_records_lot_numbers.inspection_record_id == inspection_record_id)\
            .filter(inspection_records_lot_numbers.lot_number_id == lot_number_id).all()

        # logic gate
        if len(results) > 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.record_already_exists, tables = [inspection_records_lot_numbers])
            }

        # add the new association
        session.add(inspection_records_lot_numbers(**{
            "inspection_record_id": inspection_record_id,
            "lot_number_id": lot_number_id
        }))
        session.commit()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

    return func_lot_numbers_get_filtered_associations(
        search_term,
        inspection_record_id
    )

def func_lot_numbers_association_remove(search_term:str, inspection_record_id:int, lot_number_id:int):

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        deleted_count = session.query(inspection_records_lot_numbers)\
            .filter(inspection_records_lot_numbers.inspection_record_id == inspection_record_id)\
            .filter(inspection_records_lot_numbers.lot_number_id == lot_number_id)\
            .delete()

        # logic gate
        if deleted_count == 0:
            session.close()
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_not_deleted, tables = [inspection_records_lot_numbers])
            }
        else:
            session.commit()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

    return func_lot_numbers_get_filtered_associations(search_term, inspection_record_id)

def func_lot_numbers_get_filtered_associations(search_term:str, inspection_record_id:int):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(lot_numbers.id, lot_numbers.name)\
            .join(inspection_records_lot_numbers, (lot_numbers.id == inspection_records_lot_numbers.lot_number_id))\
            .join(inspection_records, (inspection_records.id == inspection_records_lot_numbers.inspection_record_id))\
            .filter(inspection_records.id == inspection_record_id)\
            .filter(lot_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(lot_numbers.name.asc()).all()

        # close the session
        session.close()

        # return the results
        arr_size = len(results)
        if arr_size > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "inspection_record_id": inspection_record_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

def func_lot_numbers_get_filtered_options(search_term:str):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(lot_numbers.id, lot_numbers.name)\
            .filter(lot_numbers.name.ilike(f"%{search_term}%"))\
            .order_by(lot_numbers.name.asc())\
            .all()

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

#region inspection records - deviations

# routes

@app.route("/inspection_records/deviations/save_deviations/", methods = ["POST"])
def inspection_records_deviations_save_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # extract the required information
    feature_id = int(form_data["feature_id"])
    data = list(form_data["data"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        rows_affected = 0
        for row in data:
            deviation_id = int(row["id"])
            results = session.query(deviations).filter(deviations.id == deviation_id)

            is_affected = results.update({
                "nominal": float(row["nominal"]),
                "usl": float(row["usl"]),
                "lsl": float(row["lsl"]),
                "precision": int(row["precision"]),
                "date_implemented": datetime.datetime.strptime(str(row["date_implemented"]), "%Y-%m-%d"),
                "notes": str(row["notes"]),
                "deviation_type_id": int(row["deviation_type_id"]),
                "employee_id": int(row["employee_id"]),
                "feature_id": feature_id
            })

            if is_affected > 0:
                rows_affected += 1

        # commit the changes
        session.commit()

        # close the session
        session.close()

        # return the results
        if rows_affected > 0:
            return {
                "status": "alert",
                "response": text_response(stack()[0][3], message_type.records_updated, qty = rows_affected, tables = [deviations])
            }
        else:
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_updated, tables = [deviations])
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_reports/deviations/add_deviation/", methods = ["POST"])
def inspection_reports_deviations_add_deviation():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    feature_id = int(form_data["feature_id"])

    try:

        # open the database session
        session = Session(engine)

        # get the inspection's employee
        employee_id = session.query(inspections.employee_id)\
            .join(features, (features.inspection_id == inspections.id))\
            .filter(features.id == feature_id)\
            .first()[0]

        # add the placeholder data to the database
        new_record = deviations(
            nominal = 1,
            usl = 1.1,
            lsl = 0.9,
            precision = 1,
            date_implemented = datetime.datetime.now(),
            notes = "none",
            deviation_type_id = 0,
            employee_id = employee_id,
            feature_id = feature_id
        )
        session.add(new_record)
        session.commit()

        # close the session
        session.close()

        # return the new deviation data
        return func_deviations_get_feature_deviations(feature_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_reports/deviations/delete_deviation/", methods = ["POST"])
def inspection_reports_deviations_delete_deviation():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    feature_id = int(form_data["feature_id"])
    deviation_id = int(form_data["deviation_id"])

    try:

        # open the database session
        session = Session(engine)

        # remove the deviation
        rows_deleted = session.query(deviations)\
            .filter(deviations.id == deviation_id)\
            .delete()
        if rows_deleted == 0:
            session.close()
            return {
                "status": "log",
                "response": text_response(stack()[0][3], message_type.records_not_deleted, tables = [deviations])
            }

        # commit the changes
        session.commit()

        # close the session
        session.close()

        # return the updated deviations
        return func_deviations_get_feature_deviations(feature_id)

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

@app.route("/inspection_reports/deviations/get_feature_deviations/", methods = ["POST"])
def inspection_reports_deviations_get_feature_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    feature_id = int(form_data["feature_id"])

    # return the results
    return func_deviations_get_feature_deviations(feature_id)

# recycled methods

def func_deviations_get_feature_deviations(feature_id:int):

    # define the columns
    columns = [
        deviations.id,
        deviations.nominal,
        deviations.usl,
        deviations.lsl,
        deviations.precision,
        deviations.date_implemented,
        deviations.notes,
        deviation_types.id,
        employees.id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(employees, (employees.id == deviations.employee_id))\
            .join(deviation_types, (deviation_types.id == deviations.deviation_type_id))\
            .filter(deviations.feature_id == feature_id)\
            .order_by(deviations.id.asc())\
            .distinct(deviations.id).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:

            output_arr = []
            for id, nominal, usl, lsl, precision, date_implemented, notes, deviation_type_id, employee_id in results:

                # parse decimal to float
                nominal_flt = round(float(nominal), precision)
                usl_flt = round(float(usl), precision)
                lsl_flt = round(float(lsl), precision)

                # parse date to string
                date_implemented_str = date_implemented.strftime("%Y-%m-%d")

                output_arr.append({
                    "id": id,
                    "nominal": nominal_flt,
                    "usl": usl_flt,
                    "lsl": lsl_flt,
                    "precision": precision,
                    "date_implemented": date_implemented_str,
                    "notes": notes,
                    "deviation_type_id": deviation_type_id,
                    "employee_id": employee_id,
                    "feature_id": feature_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "ok",
                "response": None
            }

    except SQLAlchemyError as e:
        return {
            "status": "log",
            "response": text_response(stack()[0][3], message_type.sql_exception, error = e)
        }

#endregion

# --------------------------------------------------

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)