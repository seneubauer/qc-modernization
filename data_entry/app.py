# import dependencies for flask
from flask import Flask, render_template, request

# import dependencies for sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.dialects import postgresql
from sqlalchemy import create_engine, and_, or_, func, delete

# import general dependencies
import json
import datetime

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
measurement_types = base.classes.measurement_types
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
measurement_sets = base.classes.measurement_sets
measurements = base.classes.measurements
deviations = base.classes.deviations
measurement_set_schemas = base.classes.measurement_set_schemas
measurement_set_schema_details = base.classes.measurement_set_schema_details
employee_projects = base.classes.employee_projects
parts_suppliers = base.classes.parts_suppliers
parts_job_orders = base.classes.parts_job_orders
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
inspection_lot_numbers = base.classes.inspection_lot_numbers

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# --------------------------------------------------

#region page navigation

@app.route("/measurement_set_schemas/")
def open_measurement_set_schemas():
    return render_template("measurement_schemas.html")

@app.route("/inspection_reports/")
def open_inspection_reports():
    return render_template("inspection_reports.html")

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
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
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

@app.route("/get_all_measurement_types/")
def get_all_measurement_types():

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(measurement_types.id, measurement_types.name).order_by(measurement_types.name.asc()).all()

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
                "response": "no records found in 'measurement_types'"
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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'job_orders'"
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

#region measurement schemas - schemas

# routes

@app.route("/measurement_set_schemas/create_new_measurement_set_schema/", methods = ["POST"])
def measurement_set_schemas_create_new_measurement_set_schema():

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
        exists = session.query(measurement_set_schemas.id)\
            .filter(measurement_set_schemas.part_id == part_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": "this measurement schema already exists"
            }

        # create new governing record in the database
        results = measurement_set_schemas(
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
                "response": "error in creating the new schema id"
            }

        # close the database session
        session.close()

        # create the first measurement in the new schema
        returned_obj0 = func_measurement_set_schemas_add_row(schema_id)

        # requery the schemas with the same filter parameters
        returned_obj1 = func_measurement_set_schemas_get_filtered_schemas(search_term, is_locked)

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
                "response": "no records added to 'measurement_set_schemas' and 'measurement_set_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/measurement_set_schemas/add_row/", methods = ["POST"])
def measurement_set_schemas_add_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]
    
    try:

        # open the database session
        session = Session(engine)

        # measurement_set if the schema is locked
        locked_query = session.query(measurement_set_schemas.is_locked)\
            .filter(measurement_set_schemas.id == schema_id)\
            .first()[0]
        if locked_query:
            session.close()
            return {
                "status": "alert",
                "response": "this schema is locked; it cannot be modified"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

    return func_measurement_set_schemas_add_row(schema_id)

@app.route("/measurement_set_schemas/remove_row/", methods = ["POST"])
def measurement_set_schemas_remove_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    detail_id = form_data["detail_id"]

    try:

        # open the database session
        session = Session(engine)

        # get the schema id
        schema_id = session.query(measurement_set_schema_details.schema_id)\
            .filter(measurement_set_schema_details.id == detail_id)\
            .first()[0]

        # measurement_set if the schema is locked
        locked_query = session.query(measurement_set_schemas.is_locked)\
            .filter(measurement_set_schemas.id == schema_id)\
            .first()[0]
        if locked_query:
            session.close()
            return {
                "status": "alert",
                "response": "this schema is locked; it cannot be modified"
            }

        # make sure there is something to be deleted
        results = session.query(measurement_set_schema_details.id)\
            .filter(measurement_set_schema_details.id == detail_id)\
            .first()
        if results is None:
            session.close()
            return {
                "status": "alert",
                "response": "this schema measurement does not exist in the database"
            }

        # remove the matching schema id
        results = session.query(measurement_set_schema_details)\
            .filter(measurement_set_schema_details.id == detail_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if results > 0:
            return {
                "status": "ok",
                "response": f"{results} records deleted from 'measurement_set_schema_details'"
            }
        else:
            return {
                "status": "log",
                "response": "no records deleted from 'measurement_set_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/measurement_set_schemas/toggle_lock_schema/", methods = ["POST"])
def measurement_set_schemas_toggle_lock_schema():

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
        exists = session.query(measurement_set_schemas.id)\
            .filter(measurement_set_schemas.id == schema_id)\
            .first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": "this schema does not exists"
            }

        # get the current locked status
        locked_query = session.query(measurement_set_schemas.is_locked)\
            .filter(measurement_set_schemas.id == schema_id)\
            .first()[0]

        # set the locked status
        rows_affected = session.query(measurement_set_schemas)\
            .filter(measurement_set_schemas.id == schema_id)\
            .update({ "is_locked": not locked_query })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # logic gate
        if rows_affected == 0:
            return {
                "status": "log",
                "response": "no records modified in 'measurement_set_schemas'"
            }

        # requery the schemas
        returned_obj = func_measurement_set_schemas_get_filtered_schemas(search_term, is_locked)

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
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/measurement_set_schemas/save_measurement_set_schema/", methods = ["POST"])
def measurement_set_schemas_save_measurement_set_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the measurement schema exists
        exists = session.query(measurement_set_schema_details.id)\
            .filter(measurement_set_schema_details.schema_id == schema_id)\
            .first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": "this schema does not exists"
            }

        # query the database
        rows_affected = 0
        for obj in form_data["data"]:
            results = session.query(measurement_set_schema_details)\
                .filter(measurement_set_schema_details.id == obj["detail_id"])
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
                "response": f"{rows_affected} rows were updated"
            }
        else:
            return {
                "status": "log",
                "response": "no records added to 'measurement_set_schemas'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/measurement_set_schemas/delete_measurement_set_schema/", methods = ["POST"])
def measurement_set_schemas_delete_measurement_set_schema():

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
        exists = session.query(measurement_set_schemas.id)\
            .filter(measurement_set_schemas.id == schema_id).first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": "the referenced schema does not exist in the database"
            }

        # measurement_set if the schema is already locked
        schema_is_locked = session.query(measurement_set_schemas.is_locked)\
            .filter(measurement_set_schemas.id == schema_id)\
            .first()[0]
        if schema_is_locked:
            session.close()
            return {
                "status": "alert",
                "response": "this schema is locked: it cannot be deleted"
            }

        # delete the referenced schema
        details_results = session.query(measurement_set_schema_details)\
            .filter(measurement_set_schema_details.schema_id == schema_id)\
            .delete()
        schema_results = session.query(measurement_set_schemas)\
            .filter(measurement_set_schemas.id == schema_id)\
            .delete()

        # logic gate
        if details_results == 0 and schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'measurement_set_schemas' and 'measurement_set_schema_details' were deleted"
            }
        elif details_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'measurement_set_schema_details' were deleted"
            }
        elif schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'measurement_set_schemas' were deleted"
            }

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # requery the schemas
        return func_measurement_set_schemas_get_filtered_schemas(search_term, is_locked)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/measurement_set_schemas/get_filtered_measurement_set_schemas/", methods = ["POST"])
def measurement_set_schemas_get_filtered_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    is_locked = int(form_data["is_locked"])

    # call the relevant method
    return func_measurement_set_schemas_get_filtered_schemas(search_term, is_locked)

@app.route("/measurement_set_schemas/get_filtered_parts/", methods = ["POST"])
def measurement_set_schemas_get_filtered_parts():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]

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
                "status": "log",
                "response": "no matching parts found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled methods

def func_measurement_set_schemas_add_row(schema_id:int):

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
        results = measurement_set_schema_details(
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
                "response": "no records added to 'measurement_set_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_measurement_set_schemas_get_filtered_schemas(search_term:str, is_locked:int):

    # define the output columns
    columns = [
        measurement_set_schemas.id,
        measurement_set_schemas.is_locked,
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
            .join(parts, (parts.id == measurement_set_schemas.part_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))
        if is_locked >= 0:
            results = results.filter(measurement_set_schemas.is_locked == bool(is_locked))
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
                "status": "log",
                "response": "no matching records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region measurement schemas - schema view

@app.route("/measurement_set_schemas/get_schema_measurements/", methods = ["POST"])
def measurement_set_schemas_get_schema_measurements():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    # define the output columns
    columns = [
        measurement_set_schemas.id,
        measurement_set_schemas.is_locked,
        parts.id,
        measurement_set_schema_details.id,
        measurement_set_schema_details.name,
        measurement_set_schema_details.nominal,
        measurement_set_schema_details.usl,
        measurement_set_schema_details.lsl,
        measurement_set_schema_details.precision,
        measurement_set_schema_details.specification_type_id,
        measurement_set_schema_details.dimension_type_id,
        measurement_set_schema_details.frequency_type_id,
        measurement_set_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the requested schema
        results = session.query(*columns)\
            .join(parts, (parts.id == measurement_set_schemas.part_id))\
            .join(measurement_set_schema_details, (measurement_set_schema_details.schema_id == measurement_set_schemas.id))\
            .filter(measurement_set_schemas.id == schema_id)\
            .order_by(measurement_set_schema_details.id.asc(), measurement_set_schema_details.name.asc()).all()

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
                "response": "no matching records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

# --------------------------------------------------

#region inspection reports - inspection reports

# routes

@app.route("/inspection_reports/inspection_reports_create_new_report/", methods = ["POST"])
def inspection_reports_inspection_reports_create_new_report():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = int(form_data["part_id"])
    schema_id = int(form_data["schema_id"])
    employee_id = int(form_data["employee_id"])
    part_search_term = str(form_data["part_search_term"])
    job_order_search_term = str(form_data["job_order_search_term"])
    started_after_str = str(form_data["started_after"])
    finished_before_str = str(form_data["finished_before"])

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
                "response": f"the referenced part ({part_id}) does not exist"
            }

        # make sure this part isn't already associated with an inspection report
        exists = session.query(parts.id, inspection_reports.id, measurement_sets.id)\
            .join(parts, (parts.id == measurement_sets.part_id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(parts.id == part_id).first()
        if exists is not None:
            return {
                "status": "alert",
                "response": f"the referenced part ({part_id}) already exists in an inspection report ({exists[1]})"
            }

        # close the database session
        session.close()

        # create the new records
        func_measurement_sets_add_new_measurement_set(part_id, -1, schema_id, employee_id, 0)

        return func_inspection_reports_get_filtered_reports(part_search_term, job_order_search_term, started_after, finished_before)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/inspection_reports_delete/", methods = ["POST"])
def inspection_reports_inspection_reports_delete():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    part_search_term = str(form_data["part_search_term"])
    job_order_search_term = str(form_data["job_order_search_term"])
    started_after_str = form_data["started_after"]
    finished_before_str = form_data["finished_before"]

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
        inspection_exists = session.query(inspection_reports.id)\
            .filter(inspection_reports.id == inspection_id).first()
        if inspection_exists is None:
            session.close()
            return {
                "status": "alert",
                "response": f"the referenced inspection report ({inspection_id}) doesn't exist in the database"
            }

        # get the associated ids
        measurement_set_ids_query = session.query(measurement_sets.id)\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        measurement_set_ids = [x[0] for x in measurement_set_ids_query]

        measurement_ids_query = session.query(measurements.id)\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        measurement_ids = [x[0] for x in measurement_ids_query]

        deviation_ids_query = session.query(deviations.id)\
            .join(measurements, (measurements.id == deviations.measurement_id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        deviation_ids = [x[0] for x in deviation_ids_query]

        # delete the referenced records
        deviations_deleted = session.query(deviations)\
            .filter(deviations.id.in_(deviation_ids)).delete(synchronize_session = False)

        measurements_deleted = session.query(measurements)\
            .filter(measurements.id.in_(measurement_ids)).delete(synchronize_session = False)

        measurement_sets_deleted = session.query(measurement_sets)\
            .filter(measurement_sets.id.in_(measurement_set_ids)).delete(synchronize_session = False)

        inspection_purchase_orders_deleted = session.query(inspection_purchase_orders)\
            .filter(inspection_purchase_orders.inspection_id == inspection_id).delete(synchronize_session = False)

        inspection_receiver_numbers_deleted = session.query(inspection_receiver_numbers)\
            .filter(inspection_receiver_numbers.inspection_id == inspection_id).delete(synchronize_session = False)

        inspection_lot_numbers_deleted = session.query(inspection_lot_numbers)\
            .filter(inspection_lot_numbers.inspection_id == inspection_id).delete(synchronize_session = False)

        inspection_reports_deleted = session.query(inspection_reports)\
            .filter(inspection_reports.id == inspection_id).delete(synchronize_session = False)

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        return func_inspection_reports_get_filtered_reports(part_search_term, job_order_search_term, started_after, finished_before)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/inspection_reports_get_filtered_reports/", methods = ["POST"])
def inspection_reports_inspection_reports_get_filtered_reports():

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
    job_order_search_term = str(form_data["job_order"])
    lot_number_search_term = str(form_data["lot_number"])
    supplier_search_term = str(form_data["supplier"])

    # convert date strings to datetime objects
    started_after = datetime.date(1970, 1, 1)
    finished_before = datetime.date(2100, 1, 1)
    if started_after_str != "":
        started_after = datetime.datetime.strptime(started_after_str, "%Y-%m-%d")
    if finished_before_str != "":
        finished_before = datetime.datetime.strptime(finished_before_str, "%Y-%m-%d")

    return func_inspection_reports_get_filtered_reports(
        part_search_term,
        started_after,
        finished_before,
        material_type_search_term,
        employee_search_term,
        disposition_search_term,
        receiver_number_search_term,
        purchase_order_search_term,
        job_order_search_term,
        lot_number_search_term,
        supplier_search_term
    )

@app.route("/inspection_reports/inspection_reports_get_filtered_parts/", methods = ["POST"])
def inspection_reports_inspection_reports_get_filtered_parts():

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
                "response": f"no matching records found in {parts.__table__.name} under the criteria search_term: '{search_term}'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/inspection_reports/inspection_reports_get_filtered_schemas/", methods = ["POST"])
def inspection_reports_inspection_reports_get_filtered_measurement_set_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    part_id = int(form_data["part_id"])

    # define the output columns
    columns = [
        measurement_set_schemas.id,
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
                "response": "part not found in the database"
            }
        item, drawing = part_query

        # query the database
        results = session.query(*columns)\
            .join(parts, (parts.id == measurement_set_schemas.part_id))\
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
                "response": None
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/inspection_reports/inspection_reports_get_filtered_employees/", methods = ["POST"])
def inspection_reports_inspection_report_get_filtered_employees():

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
                "response": "no matching records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled methods

def func_inspection_reports_get_filtered_reports(part_search_term:str, started_after:datetime, finished_before:datetime, material_type_search_term:str, employee_search_term:str, disposition_search_term:str, receiver_number_search_term:str, purchase_order_search_term:str, job_order_search_term:str, lot_number_search_term:str, supplier_search_term:str):

    # define the required fields
    columns = [
        inspection_reports.id,
        parts.id,
        parts.item,
        parts.drawing,
        inspection_reports.disposition_id,
        inspection_reports.material_type_id,
        inspection_reports.employee_id,
        disposition_types.name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(measurement_sets, (measurement_sets.inspection_id == inspection_reports.id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .outerjoin(material_types, (material_types.id == inspection_reports.material_type_id))\
            .outerjoin(employees, (employees.id == inspection_reports.employee_id))\
            .outerjoin(disposition_types, (disposition_types.id == inspection_reports.disposition_id))\
            .outerjoin(inspection_receiver_numbers, (inspection_receiver_numbers.inspection_id == inspection_reports.id))\
            .outerjoin(receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
            .outerjoin(inspection_purchase_orders, (inspection_purchase_orders.inspection_id == inspection_reports.id))\
            .outerjoin(purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
            .outerjoin(parts_job_orders, (parts_job_orders.part_id == parts.id))\
            .outerjoin(job_orders, (job_orders.id == parts_job_orders.job_order_id))\
            .outerjoin(inspection_lot_numbers, (inspection_lot_numbers.inspection_id == inspection_reports.id))\
            .outerjoin(lot_numbers, (lot_numbers.id == inspection_lot_numbers.lot_number_id))\
            .outerjoin(parts_suppliers, (parts_suppliers.part_id == parts.id))\
            .outerjoin(suppliers, (suppliers.id == parts_suppliers.supplier_id))\
            .filter(measurement_sets.datetime_measured >= started_after)\
            .filter(or_(measurement_sets.datetime_measured <= finished_before, measurement_sets.datetime_measured == None))\
            .filter(or_(parts.item.ilike(f"%{part_search_term}%"), parts.drawing.ilike(f"%{part_search_term}%"), parts.revision.ilike(f"%{part_search_term}%")))\
            .filter(material_types.name.ilike(f"%{material_type_search_term}%"))\
            .filter(or_(employees.first_name.ilike(f"%{employee_search_term}%"), employees.last_name.ilike(f"%{employee_search_term}%")))\
            .filter(disposition_types.name.ilike(f"%{disposition_search_term}%"))\
            .filter(or_(receiver_numbers.name == None, receiver_numbers.name.ilike(f"%{receiver_number_search_term}%")))\
            .filter(or_(purchase_orders.name == None, purchase_orders.name.ilike(f"%{purchase_order_search_term}%")))\
            .filter(or_(job_orders.name == None, job_orders.name.ilike(f"%{job_order_search_term}%")))\
            .filter(or_(lot_numbers.name == None, lot_numbers.name.ilike(f"%{lot_number_search_term}%")))\
            .filter(or_(suppliers.name == None, suppliers.name.ilike(f"%{supplier_search_term}%")))\
            .order_by(parts.drawing.asc(), parts.item.asc())\
            .distinct(parts.drawing, parts.item)

        # close the database session
        session.close()

        # return the results
        if len(results.all()) > 0:
            output_arr = []
            for inspection_id, part_id, item, drawing, disposition_type_id, material_type_id, employee_id, disposition in results.all():
                output_arr.append({
                    "inspection_id": inspection_id,
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
                "status": "alert",
                "response": "no matching records found in 'inspection_reports', 'parts', 'job_orders', and 'measurement_sets'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - measurement sets

# routes

@app.route("/inspection_reports/measurement_sets_add_set/", methods = ["POST"])
def inspection_reports_measurement_sets_add_set():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    schema_id = int(form_data["schema_id"])
    employee_id = int(form_data["employee_id"])
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # get the part id
        part_id = session.query(measurement_set_schemas.part_id)\
            .filter(measurement_set_schemas.id == schema_id).first()[0]

        # close the database session
        session.close()

        # add the records
        func_measurement_sets_add_new_measurement_set(part_id, inspection_id, schema_id, employee_id, -1)

        # return an updated list of measurement sets
        return func_measurement_sets_get_filtered_sets(inspection_id, search_term)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/measurement_sets_delete_set/", methods = ["POST"])
def inspection_reports_measurement_sets_delete_set():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    measurement_set_id = int(form_data["measurement_set_id"])
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # remove associated measurements
        measurements_query = session.query(measurements)\
            .filter(measurements.measurement_set_id == measurement_set_id)\
            .delete()

        # narrow search to measurement set
        measurement_set_query = session.query(measurement_sets)\
            .filter(measurement_sets.id == measurement_set_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated list of measurement sets
        return func_measurement_sets_get_filtered_sets(inspection_id, search_term)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/measurement_sets_save_edits/", methods = ["POST"])
def inspection_reports_measurement_sets_save_edits():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    data_list = list(form_data["data"])

    # parse data object
    data_object = []
    for x in data_list:
        data_object.append({
            "measurement_set_id": int(x["measurement_set_id"]),
            "data": {
                "part_index": int(x["part_index"]),
                "measurement_type_id": int(x["measurement_type_id"]),
                "datetime_measured": datetime.datetime.strptime(x["timestamp"], "%Y-%m-%dT%H:%M"),
                "employee_id": int(x["employee_id"])
            }
        })

    try:

        # open the database session
        session = Session(engine)

        # narrow query object to proper scope
        for x in data_object:
            measurement_set_query = session.query(measurement_sets)\
                .filter(measurement_sets.id == x["measurement_set_id"])

            for k, v in x["data"].items():
                measurement_set_query.update({ k: v })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return an updated list of measurement sets
        return {
            "status": "alert",
            "response": "records successfully updated"
        }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/measurement_sets_get_filtered_set_schemas/", methods = ["POST"])
def inspection_reports_measurement_sets_get_filtered_set_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    search_term = str(form_data["search_term"])

    # define the output columns
    columns = [
        measurement_set_schemas.id,
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
            .join(measurement_sets, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .order_by(parts.item.asc(), parts.drawing.asc())
        if part_query.first() is None:
            session.close()
            return {
                "status": "alert",
                "response": f"no results from the following query:\n{str(part_query.statement.compile(dialect = postgresql.dialect()))}"
            }
        item, drawing = part_query.first()

        # get the list of matching measurement set schemas
        set_schema_query = session.query(*columns)\
            .join(parts, (parts.id == measurement_set_schemas.part_id))\
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
                "response": f"no matching records found in the joined query of '{parts.__table__.name}' and '{measurement_set_schemas.__table__.name}' under the criteria of {search_term}, {item}, and {drawing}"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/measurement_sets_get_filtered_sets/", methods = ["POST"])
def inspection_reports_measurement_sets_get_filtered_sets():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    search_term = str(form_data["search_term"])

    return func_measurement_sets_get_filtered_sets(inspection_id, search_term)

# recycled methods

def func_measurement_sets_add_new_measurement_set(part_id:int, inspection_id:int, schema_id:int, employee_id:int, part_index:int):

    # schema detail columns
    schema_details_columns = [
        measurement_set_schema_details.name,
        measurement_set_schema_details.nominal,
        measurement_set_schema_details.usl,
        measurement_set_schema_details.lsl,
        measurement_set_schema_details.precision,
        measurement_set_schema_details.specification_type_id,
        measurement_set_schema_details.dimension_type_id,
        measurement_set_schema_details.frequency_type_id,
        measurement_set_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # measurement_set for schema
        schema_query = session.query(parts.item, parts.drawing)\
            .join(measurement_set_schemas, (measurement_set_schemas.part_id == parts.id))\
            .filter(measurement_set_schemas.id == schema_id).first()
        if schema_query is None:
            session.close()
            return {
                "status": "alert",
                "response": f"the referenced measurement schema ({schema_id}) does not exist in the database"
            }
        schema_item, schema_drawing = schema_query

        # measurement_set for part
        part_query = session.query(parts.item, parts.drawing)\
            .filter(parts.id == part_id).first()
        if part_query is None:
            session.close()
            return {
                "status": "alert",
                "response": f"the referenced part ({part_id}) does not exist in the database"
            }
        part_item, part_drawing = part_query

        # measurement_set if schema and part match up
        if schema_item != part_item and schema_drawing != part_drawing:
            session.close()
            return {
                "status": "alert",
                "response": "the provided schema does not match the provided part"
            }

        # create a new inspection report if the provided inspection_id is -1, or ensure it exists
        if inspection_id == -1:

            # create a new inspection report
            inspection_report_query = inspection_reports(
                material_type_id = 0,
                employee_id = employee_id,
                disposition_id = 2
            )
            session.add(inspection_report_query)
            session.commit()
            inspection_id = inspection_report_query.id
        else:

            # ensure the inspection report exists
            inspection_query = session.query(parts.item, parts.drawing)\
                .join(measurement_sets, (measurement_sets.part_id == parts.id))\
                .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
                .filter(inspection_reports.id == inspection_id).first()
            if inspection_query is None:
                session.close()
                return {
                    "status": "alert",
                    "response": f"the referenced inspection report ({inspection_id}) does not exist in the database"
                }
            inspection_item, inspection_drawing = inspection_query

            # measurement_set if the inspection and part match up
            if inspection_item != part_item and inspection_drawing != part_drawing:
                session.close()
                return {
                    "status": "alert",
                    "response": "the provided inspection report does not match the provided part"
                }

        # calculate the part index if the provided part_index is -1
        if part_index == -1:
            part_index_arr = session.query(measurement_sets.part_index)\
                .filter(measurement_sets.part_id == part_id)\
                .filter(measurement_sets.inspection_id == inspection_id).all()
            part_index = max([x[0] for x in part_index_arr]) + 1

        # create a new measurement_set set
        measurement_set_query = measurement_sets(
            part_index = part_index,
            datetime_measured = datetime.datetime.now(),
            inspection_id = inspection_id,
            part_id = part_id,
            employee_id = employee_id,
            measurement_type_id = 0
        )
        session.add(measurement_set_query)
        session.commit()
        measurement_set_id = measurement_set_query.id

        # get the schema details
        schema_details = session.query(*schema_details_columns)\
            .filter(measurement_set_schema_details.schema_id == schema_id)\
            .order_by(measurement_set_schema_details.name.asc()).all()
        schema_details_list = []
        for name, nominal, usl, lsl, precision, spectype, dimetype, freqtype, gauge_type_id in schema_details:

            gauge_id = session.query(gauges.id)\
                .filter(gauges.gauge_type_id == gauge_type_id)\
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

        # create the measurement records
        for obj in schema_details_list:
            measurements_query = measurements(
                name = obj["name"],
                nominal = obj["nominal"],
                usl = obj["usl"],
                lsl = obj["lsl"],
                precision = obj["precision"],
                measurement_set_id = measurement_set_id,
                specification_type_id = obj["specification_type_id"],
                dimension_type_id = obj["dimension_type_id"],
                frequency_type_id = obj["frequency_type_id"],
                gauge_id = obj["gauge_id"]
            )
            session.add(measurements_query)
        session.commit()

        # close the database session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_measurement_sets_get_filtered_sets(inspection_id:int, search_term:str):

    # define the output columns
    columns = [
        measurement_sets.id,
        measurement_sets.datetime_measured,
        measurement_sets.part_index,
        measurement_sets.employee_id,
        measurement_sets.inspection_id,
        measurement_sets.measurement_type_id,
        parts.item,
        parts.drawing,
        parts.revision
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the list of matching measurement set schemas
        sets_query = session.query(*columns)\
            .join(parts, (parts.id == measurement_sets.part_id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .order_by(measurement_sets.part_index.asc(), parts.revision.asc())\
            .all()

        # close the database session
        session.close()

        # return the results
        if len(sets_query) > 0:
            output_arr = []
            for measurement_set_id, timestamp, part_index, employee_id, inspection_id, measurement_type_id, item, drawing, revision in sets_query:
                output_arr.append({
                    "measurement_set_id": measurement_set_id,
                    "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M"),
                    "part_index": part_index,
                    "employee_id": employee_id,
                    "inspection_id": inspection_id,
                    "measurement_type_id": measurement_type_id,
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
                "status": "log",
                "response": f"no matching records found in the joined query of '{measurement_sets.__table__.name}' and '{parts.__table__.name}' under the criteria of search_term: '{search_term}', inspection_id: '{inspection_id}'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - measurements

@app.route("/inspection_reports/measurements_get_filtered_measurements/", methods = ["POST"])
def inspection_reports_measurements_get_filtered_measurements():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["identity"]["inspection_id"])
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
    measurement_type_id = int(form_data["content"]["measurement_type_id"])
    revision = str(form_data["content"]["revision"])
    part_index = int(form_data["content"]["part_index"])

    # make a list of acceptable measurement set ids
    measurement_set_ids = []
    for obj in list(form_data["content"]["measurement_sets"]):
        if bool(int(obj["display_state"])):
            measurement_set_ids.append(int(obj["measurement_set_id"]))

    # run the required function
    return func_measurements_get_filtered_measurements(
        inspection_id,
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
        measurement_type_id,
        revision,
        part_index,
        measurement_set_ids
    )

@app.route("/inspection_reports/measurements_save_measurements/", methods = ["POST"])
def inspection_reports_measurements_save_measurements():

    # interpret the posted data
    form_data = json.loads(request.data)

    # extract the required information
    data = form_data["data"]

    if len(data) > 0:

        # convert the raw data
        my_data = {}
        for row in data:

            # make sure we're only pulling info we want
            if row["column"]["key"] == "measured" or row["column"]["key"] == "gauge_id":

                # get the measurement id
                meas_id = row["row"]["measurement_id"]

                # check if the measurement id already exists in our dictionary
                if meas_id in my_data:
                    my_data[meas_id].append({ row["column"]["key"]: row["row"]["value"] })
                else:
                    my_data[meas_id] = [{ row["column"]["key"]: row["row"]["value"] }]

        # open the database session
        session = Session(engine)

        # iterate through the data object
        rows_affected = 0
        for k, v in my_data.items():
            results = session.query(measurements).filter(measurements.id == k)
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
                "response": f"{rows_affected} rows updated in 'measurements'"
            }
        else:
            return {
                "status": "alert",
                "response": "no records affected"
            }
    else:
        return {
            "status": "alert",
            "response": "no data passed to flask server"
        }

@app.route("/inspection_reports/measurements_tunnel_to_physical_part/", methods = ["POST"])
def inspection_reports_measurements_tunnel_to_physical_part():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
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
                "response": f"the specified part ({part_id}) does not exist in the database"
            }
        item, drawing, revision = part_query

        # close the database connection
        session.close()

        # run the required function
        return func_measurements_get_filtered_measurements(
            inspection_id,
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
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/measurements_get_filter_parameter_data/", methods = ["POST"])
def inspection_reports_measurements_get_filter_parameter_data():
    
    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    item = form_data["item"]
    drawing = form_data["drawing"]

    try:

        # open the database session
        session = Session(engine)

        # measurement type list
        measurement_types_query = session.query(measurement_types.id, measurement_types.name)\
            .join(measurement_sets, (measurement_sets.measurement_type_id == measurement_types.id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}")))\
            .order_by(measurement_types.name.asc()).distinct(measurement_types.name).all()

        # part index list
        part_index_query = session.query(measurement_sets.part_index)\
            .join(parts, (parts.id == measurement_sets.part_id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .order_by(measurement_sets.part_index.asc()).distinct(measurement_sets.part_index).all()

        # revisions list
        revisions_query = session.query(parts.revision)\
            .join(measurement_sets, (parts.id == measurement_sets.part_id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .order_by(parts.revision.asc()).distinct(parts.revision).all()

        # frequency type list
        frequency_types_query = session.query(frequency_types.id, frequency_types.name)\
            .join(measurements, (measurements.frequency_type_id == frequency_types.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(frequency_types.name.asc()).distinct(frequency_types.name).all()

        # inspectors list
        inspectors_query = session.query(employees.id, employees.first_name, employees.last_name)\
            .join(measurement_sets, (measurement_sets.employee_id == employees.id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).distinct(employees.first_name, employees.last_name).all()

        # gauges list
        gauges_query = session.query(gauges.id, gauges.name)\
            .join(measurements, (measurements.gauge_id == gauges.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauges.name.asc()).distinct(gauges.name).all()

        # gauges types list
        gauge_types_query = session.query(gauge_types.id, gauge_types.name)\
            .join(gauges, (gauges.gauge_type_id == gauge_types.id))\
            .join(measurements, (measurements.gauge_id == gauges.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauge_types.name.asc()).distinct(gauge_types.name).all()

        # specification types list
        specification_types_query = session.query(specification_types.id, specification_types.name)\
            .join(measurements, (measurements.specification_type_id == specification_types.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(specification_types.name.asc()).distinct(specification_types.name).all()

        # dimension types list
        dimension_types_query = session.query(dimension_types.id, dimension_types.name)\
            .join(measurements, (measurements.dimension_type_id == dimension_types.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .filter(measurement_sets.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(dimension_types.name.asc()).distinct(dimension_types.name).all()

        # close the database session
        session.close()

        # return the results
        measurement_types_list = []
        for id, name in measurement_types_query:
            measurement_types_list.append({
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
                "measurement_types": measurement_types_list,
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
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled methods

def func_measurements_get_filtered_measurements(inspection_id:int, item:str, drawing:str, frequency_type_id:int, name:str, has_deviations:int, inspector_id:int, gauge_id:int, gauge_type_id:int, specification_type_id:int, dimension_type_id:int, measurement_type_id:int, revision:str, part_index:int, measurement_set_ids:list):

    # define the columns
    columns = [
        measurement_sets.id,
        measurement_sets.part_index,
        measurement_sets.datetime_measured,
        measurement_sets.employee_id,
        parts.id,
        parts.revision,
        measurements.id,
        measurements.name,
        measurements.nominal,
        measurements.usl,
        measurements.lsl,
        measurements.measured,
        measurements.precision,
        gauges.id,
        gauge_types.id,
        gauge_types.name,
        specification_types.name,
        dimension_types.name,
        frequency_types.name,
        measurement_types.name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(gauges, (measurements.gauge_id == gauges.id))\
            .join(gauge_types, (gauges.gauge_type_id == gauge_types.id))\
            .join(measurement_sets, (measurement_sets.id == measurements.measurement_set_id))\
            .join(parts, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (measurement_sets.inspection_id == inspection_reports.id))\
            .join(specification_types, (measurements.specification_type_id == specification_types.id))\
            .join(dimension_types, (measurements.dimension_type_id == dimension_types.id))\
            .join(frequency_types, (measurements.frequency_type_id == frequency_types.id))\
            .join(measurement_types, (measurement_sets.measurement_type_id == measurement_types.id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .filter(measurements.name.ilike(f"%{name}%"))\
            .filter(parts.revision.ilike(f"%{revision}%"))

        if part_index > -1:
            results = results.filter(measurement_sets.part_index == part_index)
        if dimension_type_id > -1:
            results = results.filter(dimension_types.id == dimension_type_id)
        if frequency_type_id > -1:
            results = results.filter(measurements.frequency_type_id == frequency_type_id)
        if has_deviations == 0:
            results = results.filter(measurements.id.notin_(session.query(deviations.measurement_id)))
        elif has_deviations == 1:
            results = results.filter(measurements.id.in_(session.query(deviations.measurement_id)))
        if inspector_id > -1:
            results = results.filter(measurement_sets.employee_id == inspector_id)
        if gauge_id > -1:
            results = results.filter(measurements.gauge_id == gauge_id)
        if gauge_type_id > -1:
            results = results.filter(gauges.gauge_type_id == gauge_type_id)
        if specification_type_id > -1:
            results = results.filter(measurements.specification_type_id == specification_type_id)
        if measurement_type_id > -1:
            results = results.filter(measurement_sets.measurement_type_id == measurement_type_id)
        if measurement_set_ids is not None:
            results = results.filter(measurements.measurement_set_id.in_(measurement_set_ids))

        # convert to a list
        measurement_list = results\
            .order_by(measurement_sets.id.asc(), measurement_sets.part_id.asc(), parts.revision.asc(), measurements.id.asc(), measurements.name.asc()).all()

        # get the list of measurements that have deviations
        deviations_list = [x[0] for x in session.query(deviations.measurement_id).all()]

        # close the database session
        session.close()

        # return the results
        if len(measurement_list) > 0:

            # assemble measurements output
            output_arr = []
            for measurement_set_id, part_index, timestamp, employee_id, part_id, revision, measurement_id, name, nominal, usl, lsl, measured, precision, gauge_id, gauge_type_id, gauge_type, specification_type, dimension_type, frequency_type, measurement_type in measurement_list:

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

                # measurement_set for deviation flag
                has_deviations = measurement_id in deviations_list

                output_arr.append({
                    "inspection_id": inspection_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "timestamp": timestamp.strftime("%Y-%m-%d, %H:%M"),
                    "has_deviations": has_deviations,
                    "measurement_id": measurement_id,
                    "measurement_set_id": measurement_set_id,
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
                    "measurement_type": measurement_type,
                    "frequency_type": frequency_type,
                    "state": state
                })

            # return the data object
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no matching measurements found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - manufactured

# routes

@app.route("/inspection_reports/manufactured_add_associated_job_order/", methods = ["POST"])
def inspection_reports_manufactured_add_associated_job_order():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])
    job_order_id = int(form_data["job_order_id"])

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        exists = session.query(parts_job_orders.id)\
            .filter(parts_job_orders.part_id == part_id)\
            .filter(parts_job_orders.job_order_id == job_order_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": "this association already exists"
            }

        # add the association
        session.add(parts_job_orders(**{
            "part_id": part_id,
            "job_order_id": job_order_id,
        }))

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # reacquire the association list
        return func_manufactured_get_associated_job_orders(inspection_id, search_term)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/manufactured_save_associated_job_orders/", methods = ["POST"])
def inspection_reports_manufactured_save_associated_job_orders():

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
            results = session.query(job_orders).filter(job_orders.id == int(x["id"]))
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
                "response": f"{rows_affected} records were successfully updated in 'job_orders'"
            }
        else:
            return {
                "status": "alert",
                "response": "no records were successfully updated in 'job_orders'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/manufactured_delete_associated_job_order/", methods = ["POST"])
def inspection_reports_manufactured_delete_associated_job_order():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])
    job_order_id = int(form_data["job_order_id"])

    try:

        # open the database session
        session = Session(engine)

        # delete the associated record
        rows_deleted = session.query(parts_job_orders)\
            .filter(parts_job_orders.part_id == part_id)\
            .filter(parts_job_orders.job_order_id == job_order_id)\
            .delete()

        # commit the changes
        if rows_deleted > 0:
            session.commit()

        # close the database session
        session.close()

        # reacquire the association list
        return func_manufactured_get_associated_job_orders(inspection_id, search_term)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/manufactured_get_associated_job_orders/", methods = ["POST"])
def inspection_reports_manufactured_get_associated_job_orders():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    # return the results
    return func_manufactured_get_associated_job_orders(inspection_id, search_term)

@app.route("/inspection_reports/manufactured_get_filtered_job_orders/", methods = ["POST"])
def inspection_reports_manufactured_get_filtered_job_orders():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(job_orders.id, job_orders.name)\
            .filter(job_orders.name.ilike(f"%{search_term}%"))\
            .order_by(job_orders.name.asc()).all()

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
                "response": "no records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/manufactured_get_filtered_parts/", methods = ["POST"])
def inspection_reports_manufactured_get_filtered_parts():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.item, parts.drawing, parts.revision)\
            .join(measurement_sets, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .filter(inspection_reports.id == inspection_id)\
            .order_by(parts.drawing.asc(), parts.revision.asc(), parts.item.asc())\
            .distinct(parts.drawing, parts.revision, parts.item).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, item, drawing, revision in results:
                output_arr.append({
                    "id": id,
                    "name": f"{item}, {drawing}, {revision.upper()}"
                })
            
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled methods

def func_manufactured_get_associated_job_orders(inspection_id:int, search_term:str):

    # define the output columns
    columns = [
        job_orders.id,
        job_orders.name,
        job_orders.full_inspect_interval,
        job_orders.released_qty,
        job_orders.completed_qty,
        parts.revision,
        parts.id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(parts_job_orders, (parts_job_orders.job_order_id == job_orders.id))\
            .join(parts, (parts.id == parts_job_orders.part_id))\
            .join(measurement_sets, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(or_(parts.revision.ilike(f"%{search_term}%"), job_orders.name.ilike(f"%{search_term}%")))\
            .order_by(job_orders.name.asc())\
            .distinct(job_orders.name).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, name, full_inspect_interval, released_qty, completed_qty, revision, part_id in results:
                output_arr.append({
                    "id": id,
                    "name": name,
                    "full_inspect_interval": full_inspect_interval,
                    "released_qty": released_qty,
                    "completed_qty": completed_qty,
                    "revision": revision.upper(),
                    "part_id": part_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - received

# routes

@app.route("/inspection_reports/received_add_association/", methods = ["POST"])
def inspection_reports_received_add_association():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    target = str(form_data["target"])
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])
    item_id = int(form_data["item_id"])

    # use the targeted tables
    if target == "receiver_numbers":
        return func_received_add_association(
            search_term,
            inspection_id,
            item_id,
            inspection_id,
            "receiver_number_id",
            "inspection_id",
            receiver_numbers,
            inspection_receiver_numbers,
            inspection_reports
        )
    elif target == "purchase_orders":
        return func_received_add_association(
            search_term,
            inspection_id,
            item_id,
            inspection_id,
            "purchase_order_id",
            "inspection_id",
            purchase_orders,
            inspection_purchase_orders,
            inspection_reports
        )
    elif target == "suppliers":
        return func_received_add_association(
            search_term,
            inspection_id,
            item_id,
            part_id,
            "supplier_id",
            "part_id",
            suppliers,
            parts_suppliers,
            parts
        )
    else:
        return {
            "status": "alert",
            "response": "supplied target does not match criteria"
        }

@app.route("/inspection_reports/received_save_receiver_number_associations/", methods = ["POST"])
def inspection_reports_received_save_receiver_number_associations():

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

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if rows_affected > 0:
            return {
                "status": "alert",
                "response": f"{rows_affected} records were successfully updated in 'receiver_numbers'"
            }
        else:
            return {
                "status": "alert",
                "response": "no records were successfully updated in 'receiver_numbers'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/received_delete_association/", methods = ["POST"])
def inspection_reports_received_delete_association():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    target = str(form_data["target"])
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])
    item_id = int(form_data["item_id"])

    # use the targeted tables
    if target == "receiver_numbers":
        return func_received_delete_association(
            search_term,
            inspection_id,
            item_id,
            inspection_id,
            "receiver_number_id",
            "inspection_id",
            receiver_numbers,
            inspection_receiver_numbers
        )
    elif target == "purchase_orders":
        return func_received_delete_association(
            search_term,
            inspection_id,
            item_id,
            inspection_id,
            "purchase_order_id",
            "inspection_id",
            purchase_orders,
            inspection_purchase_orders
        )
    elif target == "suppliers":
        return func_received_delete_association(
            search_term,
            inspection_id,
            item_id,
            part_id,
            "supplier_id",
            "part_id",
            suppliers,
            parts_suppliers
        )
    else:
        return {
            "status": "alert",
            "response": "supplied target does not match criteria"
        }

@app.route("/inspection_reports/received_get_filtered_associations/", methods = ["POST"])
def inspection_reports_received_get_filtered_associations():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    target = str(form_data["target"])
    inspection_id = int(form_data["inspection_id"])

    # use the targeted tables
    if target == "receiver_numbers":
        return func_received_get_filtered_associations(
            search_term,
            inspection_id,
            "receiver_number_id",
            receiver_numbers,
            inspection_receiver_numbers
        )
    elif target == "purchase_orders":
        return func_received_get_filtered_associations(
            search_term,
            inspection_id,
            "purchase_order_id",
            purchase_orders,
            inspection_purchase_orders
        )
    elif target == "suppliers":
        return func_received_get_filtered_associations(
            search_term,
            inspection_id,
            "supplier_id",
            suppliers,
            parts_suppliers
        )
    else:
        return {
            "status": "alert",
            "response": "supplied target does not match criteria"
        }

@app.route("/inspection_reports/received_get_filtered_options/", methods = ["POST"])
def inspection_reports_received_get_filtered_options():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    target = str(form_data["target"])

    # use the targeted tables
    if target == "receiver_numbers":
        return func_received_get_filtered_options(search_term, receiver_numbers)
    elif target == "purchase_orders":
        return func_received_get_filtered_options(search_term, purchase_orders)
    elif target == "suppliers":
        return func_received_get_filtered_options(search_term, suppliers)
    else:
        return {
            "status": "alert",
            "response": "supplied target does not match criteria"
        }

@app.route("/inspection_reports/received_get_filtered_parts/", methods = ["POST"])
def inspection_reports_received_get_filtered_parts():

    # get the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.item, parts.drawing, parts.revision)\
            .join(measurement_sets, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .filter(inspection_reports.id == inspection_id)\
            .order_by(parts.drawing.asc(), parts.revision.asc(), parts.item.asc())\
            .distinct(parts.drawing, parts.revision, parts.item).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, item, drawing, revision in results:
                output_arr.append({
                    "id": id,
                    "name": f"{item}, {drawing}, {revision.upper()}"
                })
            
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled methods

def func_received_add_association(search_term:str, inspection_id:int, solo_id:int, record_id:int, solo_link:str, record_link:str, solo_table, link_table, record_table):

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
        exists = session.query(link_table.id)\
            .filter(link_table.__table__.c[solo_link] == solo_id)\
            .filter(link_table.__table__.c[record_link] == record_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": f"the association between '{solo_table.__table__.name}', '{link_table.__table__.name}', and '{record_table.__table__.name}' already exists"
            }
        
        # add the association
        session.add(link_table(**{
            solo_link: solo_id,
            record_link: record_id
        }))

        # commit the changes
        session.commit()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }
    
    return func_received_get_filtered_associations(
        search_term,
        inspection_id,
        solo_link,
        solo_table,
        link_table
    )

def func_received_delete_association(search_term:str, inspection_id:int, solo_id:int, record_id:int, solo_link:str, record_link:str, solo_table, link_table):

    try:

        # open the database session
        session = Session(engine)

        delete_query = delete(link_table)
        

        # delete the associated record
        rows_deleted = session.query(link_table)\
            .filter(link_table.__table__.c[solo_link] == solo_id)\
            .filter(link_table.__table__.c[record_link] == record_id)\
            .delete()

        # commit the changes
        if rows_deleted > 0:
            session.commit()

        # close the database session
        session.close()

        # reacquire the association list
        return func_received_get_filtered_associations(
            search_term,
            inspection_id,
            solo_link,
            solo_table,
            link_table
        )

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_received_get_filtered_associations(search_term:str, inspection_id:int, solo_link:str, solo_table, link_table):

    # define the output columns
    columns = []
    if solo_table.__table__.name == "receiver_numbers":
        columns = [
            solo_table.id,
            solo_table.name,
            solo_table.received_qty
        ]
    elif solo_table.__table__.name == "suppliers":
        columns = [
            solo_table.id,
            solo_table.name,
            parts.id,
            parts.revision
        ]
    else:
        columns = [
            solo_table.id,
            solo_table.name
        ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        if solo_table.__table__.name == "suppliers":
            results = session.query(*columns)\
                .join(link_table, (solo_table.id == link_table.__table__.c[solo_link]))\
                .join(parts, (parts.id == link_table.__table__.c[solo_link]))\
                .join(measurement_sets, (measurement_sets.part_id == parts.id))\
                .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
                .filter(inspection_reports.id == inspection_id)\
                .filter(solo_table.name.ilike(f"%{search_term}%"))\
                .order_by(solo_table.name.asc())\
                .distinct(solo_table.name).all()
        else:
            results = session.query(*columns)\
                .join(link_table, (solo_table.id == link_table.__table__.c[solo_link]))\
                .join(inspection_reports, (inspection_reports.id == link_table.inspection_id))\
                .filter(inspection_reports.id == inspection_id)\
                .filter(solo_table.name.ilike(f"%{search_term}%"))\
                .order_by(solo_table.name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            if solo_table.__table__.name == "receiver_numbers":
                for id, name, received_qty in results:
                    output_arr.append({
                        "inspection_id": inspection_id,
                        "id": id,
                        "name": name,
                        "received_qty": received_qty
                    })
            elif solo_table.__table__.name == "suppliers":
                for id, name, part_id, revision in results:
                    output_arr.append({
                        "inspection_id": inspection_id,
                        "id": id,
                        "name": name,
                        "part_id": part_id,
                        "revision": revision.upper()
                    })
            else:
                for id, name in results:
                    output_arr.append({
                        "inspection_id": inspection_id,
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
                "response": {
                    "size": 0,
                    "message":f"no connection found between 'inspection_reports', '{solo_table.__table__.name}', and '{link_table.__table__.name}'"
                }
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_received_get_filtered_options(search_term:str, solo_table):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(solo_table.id, solo_table.name)\
            .filter(solo_table.name.ilike(f"%{search_term}%"))\
            .order_by(solo_table.name.asc())\
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
                "status": "log",
                "response": f"no matching records found in '{solo_table.__table__.name}'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }


#endregion

#region inspection reports - metadata

@app.route("/inspection_reports/metadata_save/", methods = ["POST"])
def inspection_reports_metadata_save():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])

    try:

        # open the database session
        session = Session(engine)

        # get the associated item and drawing values
        part_query = session.query(parts.item, parts.drawing)\
            .join(measurement_sets, (measurement_sets.part_id == parts.id))\
            .join(inspection_reports, (inspection_reports.id == measurement_sets.inspection_id))\
            .filter(inspection_reports.id == inspection_id).first()
        if part_query is None:
            return {
                "status": "log",
                "response": "part not found"
            }
        item, drawing = part_query

        # update the inspection report
        results = session.query(inspection_reports).filter(inspection_reports.id == inspection_id)
        ir_is_affected = 0
        for k, v in form_data["content"].items():
            if v == "-1":
                ir_is_affected = results.update({ k: None }, synchronize_session = False)
            else:
                ir_is_affected = results.update({ k: v }, synchronize_session = False)

        # commit to then close the session
        session.commit()
        session.close()

        # open the database session
        session = Session(engine)

        # update the quantities
        pa_is_affected = 0
        for obj in form_data["sub_data"]:
            results = session.query(parts)\
                .filter(parts.item.ilike(f"%{item}%"))\
                .filter(parts.drawing.ilike(f"%{drawing}%"))\
                .filter(parts.revision.ilike(f"%{obj['revision']}%"))
            pa_is_affected = results.update({ "full_inspect_interval": obj["full_inspect_interval"] }, synchronize_session = False)
            pa_is_affected = results.update({ "completed_qty": obj["completed_qty"] }, synchronize_session = False)
            pa_is_affected = results.update({ "released_qty": obj["released_qty"] }, synchronize_session = False)

        # commit to then close the session
        session.commit()
        session.close()

        # return the response
        if ir_is_affected > 0 and pa_is_affected > 0:
            return {
                "status": "ok",
                "response": "tables 'inspection_reports' and 'parts' successfully updated"
            }
        else:
            return {
                "status": "alert",
                "response": "no records in 'inspection_reports' and 'parts' updated"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/metadata_get_parameters/", methods = ["POST"])
def inspection_reports_metadata_get_parameters():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]

    # define the required columns
    columns = [
        inspection_reports.material_type_id,
        inspection_reports.supplier_id,
        inspection_reports.job_order_id,
        inspection_reports.employee_id,
        inspection_reports.disposition_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .filter(inspection_reports.id == inspection_id)\
            .first()

        # close the database session
        session.close()

        # return the results
        if results is not None:
            material_type_id, supplier_id, job_order_id, employee_id, disposition_id = results
            return {
                "status": "ok",
                "response": {
                    "material_type_id": material_type_id,
                    "supplier_id": supplier_id,
                    "job_order_id": job_order_id,
                    "employee_id": employee_id,
                    "disposition_id": disposition_id
                }
            }
        else:
            return {
                "status": "log",
                "response": "no matching inspection report found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/metadata_get_matching_revisions/", methods = ["POST"])
def inspection_reports_metadata_get_matching_revisions():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item = form_data["item"]
    drawing = form_data["drawing"]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(parts.id, parts.revision, parts.full_inspect_interval, parts.released_qty, parts.completed_qty)\
            .filter(and_(func.lower(parts.item) == item.lower(), func.lower(parts.drawing) == drawing.lower())).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for id, revision, full_inspect_interval, released_qty, completed_qty in results:
                output_arr.append({
                    "id": id,
                    "revision": revision.upper(),
                    "full_inspect_interval": full_inspect_interval,
                    "released_qty": released_qty,
                    "completed_qty": completed_qty
                })
            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no matching parts found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - receiver numbers / purchase orders / lot numbers

# routes

@app.route("/inspection_reports/reciever_numbers_assign_association/", methods = ["POST"])
def inspection_reports_reciever_numbers_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    receiver_number_id = int(form_data["receiver_number_id"])

    # run the targeted method
    return func_inspection_association_add(
        search_term,
        inspection_id,
        receiver_number_id,
        "receiver number",
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/inspection_reports/reciever_numbers_remove_association/", methods = ["POST"])
def inspection_reports_reciever_numbers_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    receiver_number_id = int(form_data["receiver_number_id"])

    # run the targeted method
    return func_inspection_association_remove(
        search_term,
        inspection_id,
        receiver_number_id,
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/inspection_reports/receiver_numbers_get_filtered_options/", methods = ["POST"])
def inspection_reports_receiver_numbers_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_inspection_get_filtered_potential_associations(
        search_term,
        receiver_numbers,
    )

@app.route("/inspection_reports/receiver_numbers_get_filtered_associations/", methods = ["POST"])
def inspection_reports_receiver_numbers_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/inspection_reports/purchase_orders_assign_association/", methods = ["POST"])
def inspection_reports_purchase_orders_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    # run the targeted method
    return func_inspection_association_add(
        search_term,
        inspection_id,
        purchase_order_id,
        "purchase number",
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/inspection_reports/purchase_orders_remove_association/", methods = ["POST"])
def inspection_reports_purchase_orders_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    # run the targeted method
    return func_inspection_association_remove(
        search_term,
        inspection_id,
        purchase_order_id,
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/inspection_reports/purchase_orders_get_filtered_options/", methods = ["POST"])
def inspection_reports_purchase_orders_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_inspection_get_filtered_potential_associations(
        search_term,
        purchase_orders,
    )

@app.route("/inspection_reports/purchase_orders_get_filtered_associations/", methods = ["POST"])
def inspection_reports_purchase_order_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/inspection_reports/lot_numbers_assign_association/", methods = ["POST"])
def inspection_reports_lot_numbers_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_inspection_association_add(
        search_term,
        inspection_id,
        lot_number_id,
        "lot number",
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

@app.route("/inspection_reports/lot_numbers_remove_association/", methods = ["POST"])
def inspection_reports_lot_numbers_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_inspection_association_remove(
        search_term,
        inspection_id,
        lot_number_id,
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

@app.route("/inspection_reports/lot_numbers_get_filtered_options/", methods = ["POST"])
def inspection_reports_lot_numbers_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_inspection_get_filtered_potential_associations(
        search_term,
        lot_numbers,
    )

@app.route("/inspection_reports/lot_numbers_get_filtered_associations/", methods = ["POST"])
def inspection_reports_lot_numbers_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

# recycled methods

def func_inspection_association_add(search_term:str, inspection_id:int, id:int, descriptor:str, link_field:str, solo_table, link_table):

    try:

        # open the database session
        session = Session(engine)

        # measurement_set if the association already exists
        results = session.query(link_table.inspection_id)\
            .filter(and_(link_table.inspection_id == inspection_id, link_table.__table__.c[link_field] == id)).all()

        # logic gate
        if len(results) > 0:
            session.close()
            return {
                "status": "alert",
                "response": f"this {descriptor} association already exists"
            }

        # add the new association
        kwargs = {
            "inspection_id": inspection_id,
            link_field: id
        }
        session.add(link_table(**kwargs))
        session.commit()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }
    
    return func_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        link_field,
        solo_table,
        link_table
    )

def func_inspection_association_remove(search_term:str, inspection_id:int, id:int, link_field:str, solo_table, link_table):

    try:

        # open the database session
        session = Session(engine)

        # delete the record that matches the provided criteria
        deleted_count = session.query(link_table)\
            .filter(and_(link_table.inspection_id == inspection_id, link_table.__table__.c[link_field] == id))\
            .delete()

        # logic gate
        if deleted_count == 0:
            session.close()
            return {
                "status": "alert",
                "response": f"no records deleted from {link_table.__table__.name}; none matched the provided criteria"
            }
        else:
            session.commit()

        # close the session
        session.close()

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

    return func_inspection_get_filtered_associations(search_term, inspection_id, link_field, solo_table, link_table)

def func_inspection_get_filtered_associations(search_term:str, inspection_id:int, link_field:str, solo_table, link_table):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(solo_table.id, solo_table.name)\
            .join(link_table, (solo_table.id == link_table.__table__.c[link_field]))\
            .join(inspection_reports, (inspection_reports.id == link_table.inspection_id))\
            .filter(inspection_reports.id == inspection_id)\
            .filter(solo_table.name.ilike(f"%{search_term}%"))\
            .order_by(solo_table.name.asc()).all()

        # close the session
        session.close()

        # return the results
        arr_size = len(results)
        if arr_size > 0:
            output_arr = []
            for id, name in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "id": id,
                    "name": name
                })

            return {
                "status": "ok",
                "response": {
                    "size": arr_size,
                    "data": output_arr
                }
            }
        else:
            return {
                "status": "ok",
                "response": {
                    "size": 0,
                    "message":f"no connection found between 'inspection_reports', '{solo_table.__table__.name}', and '{link_table.__table__.name}'"
                }
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_inspection_get_filtered_potential_associations(search_term:str, solo_table):

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(solo_table.id, solo_table.name)\
            .filter(solo_table.name.ilike(f"%{search_term}%"))\
            .order_by(solo_table.name.asc())\
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
                "status": "log",
                "response": f"no matching records found in '{solo_table.__table__.name}'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - deviations

# routes

@app.route("/inspection_reports/deviations_save/", methods = ["POST"])
def inspection_reports_save_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)
    
    # extract the required information
    measurement_id = int(form_data["measurement_id"])
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
                "measurement_id": measurement_id
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
                "response": f"{rows_affected} record(s) in 'deviations' has been successfully updated"
            }
        else:
            return {
                "status": "log",
                "response": "no records in 'deviations' have been updated"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/deviations_add_deviation/", methods = ["POST"])
def inspection_reports_deviations_add_deviation():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    measurement_id = int(form_data["measurement_id"])

    try:

        # open the database session
        session = Session(engine)

        # get the measurement set's employee
        employee_id = session.query(measurement_sets.employee_id)\
            .join(measurements, (measurements.measurement_set_id == measurement_sets.id))\
            .filter(measurements.id == measurement_id)\
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
            measurement_id = measurement_id
        )
        session.add(new_record)
        session.commit()

        # close the session
        session.close()

        # return the new deviation data
        return func_deviations_get_measurement_deviations(measurement_id)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/deviations_delete_deviation/", methods = ["POST"])
def inspection_reports_deviations_delete_deviation():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    measurement_id = int(form_data["measurement_id"])
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
                "response": "no records deleted in 'deviations'"
            }

        # commit the changes
        session.commit()

        # close the session
        session.close()

        # return the updated deviations
        return func_deviations_get_measurement_deviations(measurement_id)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/inspection_reports/deviations_get_measurement_deviations/", methods = ["POST"])
def inspection_reports_deviations_get_measurement_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    measurement_id = int(form_data["measurement_id"])

    # return the results
    return func_deviations_get_measurement_deviations(measurement_id)

# recycled methods

def func_deviations_get_measurement_deviations(measurement_id:int):

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
        deviation_types.name,
        employees.id,
        employees.first_name,
        employees.last_name
    ]

    try:

        # open the database session
        session = Session(engine)

        # query the database
        results = session.query(*columns)\
            .join(employees, (employees.id == deviations.employee_id))\
            .join(deviation_types, (deviation_types.id == deviations.deviation_type_id))\
            .filter(deviations.measurement_id == measurement_id)\
            .order_by(deviations.id.asc())\
            .distinct(deviations.id).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0:

            output_arr = []
            for id, nominal, usl, lsl, precision, date_implemented, notes, deviation_type_id, deviation_type, employee_id, first_name, last_name in results:

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
                    "deviation_type": deviation_type,
                    "employee_id": employee_id,
                    "employee": f"{last_name}, {first_name}"
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no matching deviations found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

# --------------------------------------------------

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)