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
characteristic_schemas = base.classes.characteristic_schemas
characteristic_schema_details = base.classes.characteristic_schema_details
employee_projects = base.classes.employee_projects
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
inspection_lot_numbers = base.classes.inspection_lot_numbers

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# --------------------------------------------------

#region page navigation

@app.route("/characteristic_schemas/")
def open_characteristic_schemas():
    return render_template("characteristic_schemas.html")

@app.route("/inspection_reports/")
def open_inspection_reports():
    return render_template("inspection_reports.html")

#endregion

# --------------------------------------------------

#region get enumerations

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
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "log",
                "response": "no records found in 'characteristic_types'"
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

#region characteristic schemas - schemas

# routes

@app.route("/characteristic_schemas/create_new_characteristic_schema/", methods = ["POST"])
def characteristic_schemas_create_new_characteristic_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = form_data["part_id"]
    search_term = form_data["search_term"]
    is_locked = int(form_data["is_locked"])

    try:

        # open the database session
        session = Session(engine)

        # make sure the characteristic schema doesn't already exist
        exists = session.query(characteristic_schemas.id)\
            .filter(characteristic_schemas.part_id == part_id)\
            .first()
        if exists is not None:
            session.close()
            return {
                "status": "alert",
                "response": "this characteristic schema already exists"
            }

        # create new governing record in the database
        results = characteristic_schemas(
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

        # create the first characteristic in the new schema
        returned_obj0 = func_characteristic_schemas_add_row(schema_id)

        # requery the schemas with the same filter parameters
        returned_obj1 = func_characteristic_schemas_get_filtered_schemas(search_term, is_locked)

        # return the results
        if returned_obj0["status"] == "ok" and returned_obj1["status"] == "ok":
            return {
                "status": "ok",
                "response": {
                    "schema_list": returned_obj1["response"],
                    "schema_characteristics": returned_obj0["response"]
                }
            }
        else:
            return {
                "status": "log",
                "response": "no records added to 'characteristic_schemas' and 'characteristic_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/characteristic_schemas/add_row/", methods = ["POST"])
def characteristic_schemas_add_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]
    
    try:

        # open the database session
        session = Session(engine)

        # check if the schema is locked
        locked_query = session.query(characteristic_schemas.is_locked)\
            .filter(characteristic_schemas.id == schema_id)\
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

    return func_characteristic_schemas_add_row(schema_id)

@app.route("/characteristic_schemas/remove_row/", methods = ["POST"])
def characteristic_schemas_remove_row():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    detail_id = form_data["detail_id"]

    try:

        # open the database session
        session = Session(engine)

        # get the schema id
        schema_id = session.query(characteristic_schema_details.schema_id)\
            .filter(characteristic_schema_details.id == detail_id)\
            .first()[0]

        # check if the schema is locked
        locked_query = session.query(characteristic_schemas.is_locked)\
            .filter(characteristic_schemas.id == schema_id)\
            .first()[0]
        if locked_query:
            session.close()
            return {
                "status": "alert",
                "response": "this schema is locked; it cannot be modified"
            }

        # make sure there is something to be deleted
        results = session.query(characteristic_schema_details.id)\
            .filter(characteristic_schema_details.id == detail_id)\
            .first()
        if results is None:
            session.close()
            return {
                "status": "alert",
                "response": "this schema characteristic does not exist in the database"
            }

        # remove the matching schema id
        results = session.query(characteristic_schema_details)\
            .filter(characteristic_schema_details.id == detail_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if results > 0:
            return {
                "status": "ok",
                "response": f"{results} records deleted from 'characteristic_schema_details'"
            }
        else:
            return {
                "status": "log",
                "response": "no records deleted from 'characteristic_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/characteristic_schemas/toggle_lock_schema/", methods = ["POST"])
def characteristic_schemas_toggle_lock_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = form_data["search_term"]
    is_locked = int(form_data["is_locked"])
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the characteristic schema exists
        exists = session.query(characteristic_schemas.id)\
            .filter(characteristic_schemas.id == schema_id)\
            .first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": "this schema does not exists"
            }

        # get the current locked status
        locked_query = session.query(characteristic_schemas.is_locked)\
            .filter(characteristic_schemas.id == schema_id)\
            .first()[0]

        # set the locked status
        rows_affected = session.query(characteristic_schemas)\
            .filter(characteristic_schemas.id == schema_id)\
            .update({ "is_locked": not locked_query })

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # logic gate
        if rows_affected == 0:
            return {
                "status": "log",
                "response": "no records modified in 'characteristic_schemas'"
            }

        # requery the schemas
        returned_obj = func_characteristic_schemas_get_filtered_schemas(search_term, is_locked)

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

@app.route("/characteristic_schemas/save_characteristic_schema/", methods = ["POST"])
def characteristic_schemas_save_characteristic_schema():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the characteristic schema exists
        exists = session.query(characteristic_schema_details.id)\
            .filter(characteristic_schema_details.schema_id == schema_id)\
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
            results = session.query(characteristic_schema_details)\
                .filter(characteristic_schema_details.id == obj["detail_id"])
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
                "response": "no records added to 'characteristic_schemas'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/characteristic_schemas/delete_characteristic_schema/", methods = ["POST"])
def characteristic_schemas_delete_characteristic_schema():

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
        exists = session.query(characteristic_schemas.id)\
            .filter(characteristic_schemas.id == schema_id).first()
        if exists is None:
            session.close()
            return {
                "status": "alert",
                "response": "the referenced schema does not exist in the database"
            }

        # check if the schema is already locked
        schema_is_locked = session.query(characteristic_schemas.is_locked)\
            .filter(characteristic_schemas.id == schema_id)\
            .first()[0]
        if schema_is_locked:
            session.close()
            return {
                "status": "alert",
                "response": "this schema is locked: it cannot be deleted"
            }

        # delete the referenced schema
        details_results = session.query(characteristic_schema_details)\
            .filter(characteristic_schema_details.schema_id == schema_id)\
            .delete()
        schema_results = session.query(characteristic_schemas)\
            .filter(characteristic_schemas.id == schema_id)\
            .delete()

        # logic gate
        if details_results == 0 and schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'characteristic_schemas' and 'characteristic_schema_details' were deleted"
            }
        elif details_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'characteristic_schema_details' were deleted"
            }
        elif schema_results == 0:
            session.close()
            return {
                "status": "alert",
                "response": "no records in 'characteristic_schemas' were deleted"
            }

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # requery the schemas
        return func_characteristic_schemas_get_filtered_schemas(search_term, is_locked)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/characteristic_schemas/get_filtered_characteristic_schemas/", methods = ["POST"])
def characteristic_schemas_get_filtered_schemas():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    is_locked = int(form_data["is_locked"])

    # call the relevant method
    return func_characteristic_schemas_get_filtered_schemas(search_term, is_locked)

@app.route("/characteristic_schemas/get_filtered_parts/", methods = ["POST"])
def characteristic_schemas_get_filtered_parts():

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

# recycled functions

def func_characteristic_schemas_add_row(schema_id:int):

    try:

        # open the database session
        session = Session(engine)

        # get the default specification type id
        default_specification_type_id = session.query(specification_types.id)\
            .order_by(specification_types.name.asc())\
            .first()[0]

        # get the default characteristic type id
        default_characteristic_type_id = session.query(characteristic_types.id)\
            .order_by(characteristic_types.name.asc())\
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
        results = characteristic_schema_details(
            name = default_name,
            nominal = default_nominal,
            usl = default_usl,
            lsl = default_lsl,
            precision = default_precision,
            specification_type_id = default_specification_type_id,
            characteristic_type_id = default_characteristic_type_id,
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
                    "characteristic_type_id": default_characteristic_type_id,
                    "frequency_type_id": default_frequency_type_id,
                    "gauge_type_id": default_gauge_type_id,
                    "schema_id": schema_id
                }
            }
        else:
            return {
                "status": "log",
                "response": "no records added to 'characteristic_schema_details'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_characteristic_schemas_get_filtered_schemas(search_term:str, is_locked:int):

    # define the output columns
    columns = [
        characteristic_schemas.id,
        characteristic_schemas.is_locked,
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
            .join(parts, (parts.id == characteristic_schemas.part_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))
        if is_locked >= 0:
            results = results.filter(characteristic_schemas.is_locked == bool(is_locked))
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

#region characteristic schemas - schema view

@app.route("/characteristic_schemas/get_schema_characteristics/", methods = ["POST"])
def characteristic_schemas_get_schema_characteristics():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    schema_id = form_data["schema_id"]

    # define the output columns
    columns = [
        characteristic_schemas.id,
        characteristic_schemas.is_locked,
        parts.id,
        characteristic_schema_details.id,
        characteristic_schema_details.name,
        characteristic_schema_details.nominal,
        characteristic_schema_details.usl,
        characteristic_schema_details.lsl,
        characteristic_schema_details.precision,
        characteristic_schema_details.specification_type_id,
        characteristic_schema_details.characteristic_type_id,
        characteristic_schema_details.frequency_type_id,
        characteristic_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # get the requested schema
        results = session.query(*columns)\
            .join(parts, (parts.id == characteristic_schemas.part_id))\
            .join(characteristic_schema_details, (characteristic_schema_details.schema_id == characteristic_schemas.id))\
            .filter(characteristic_schemas.id == schema_id)\
            .order_by(characteristic_schema_details.id.asc(), characteristic_schema_details.name.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for schema_id, is_locked, part_id, detail_id, name, nominal, usl, lsl, precision, specification_type_id, characteristic_type_id, frequency_type_id, gauge_type_id in results:

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
                    "characteristic_type_id": characteristic_type_id,
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

@app.route("/data_entry/inspection_reports_create_new_report/", methods = ["POST"])
def data_entry_inspection_reports_create_new_report():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = form_data["part_id"]
    employee_id = form_data["employee_id"]
    schema_id = form_data["schema_id"]
    filter_part_id = int(form_data["filter_part_id"])
    filter_job_order_id = int(form_data["filter_job_order_id"])
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
        exists = session.query(parts.id, inspection_reports.id, checks.id)\
            .join(parts, (parts.id == checks.part_id))\
            .join(inspection_reports, (inspection_reports.id == checks.inspection_id))\
            .filter(parts.id == part_id).first()
        if exists is not None:
            return {
                "status": "alert",
                "response": f"the referenced part ({part_id}) already exists in an inspection report ({exists[1]})"
            }

        # close the database session
        session.close()

        # create the new records
        func_data_entry_inspection_reports_add_new_check_set(part_id, -1, schema_id, employee_id, 0)

        # return the results
        return func_data_entry_inspection_reports_get_filtered_reports(filter_part_id, filter_job_order_id, started_after, finished_before)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/data_entry/inspection_reports_add_check_set/", methods = ["POST"])
def data_entry_inspection_reports_add_check_set():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    schema_id = form_data["schema_id"]

    try:

        # open the database session
        session = Session(engine)

        # get the part id
        part_id = session.query(characteristic_schemas.part_id)\
            .filter(characteristic_schemas.id == schema_id).first()[0]

        # get the employee id
        employee_id = session.query(inspection_reports.employee_id)\
            .filter(inspection_reports.id == inspection_id).first()[0]

        # close the database session
        session.close()

        # add the records
        return func_data_entry_inspection_reports_add_new_check_set(part_id, inspection_id, schema_id, employee_id, -1)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/data_entry/inspection_reports_delete/", methods = ["POST"])
def data_entry_inspection_reports_delete():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = form_data["inspection_id"]
    part_id = int(form_data["part_id"])
    job_order_id = int(form_data["job_order_id"])
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
        check_ids_query = session.query(checks.id)\
            .join(inspection_reports, (inspection_reports.id == checks.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        check_ids = [x[0] for x in check_ids_query]

        characteristic_ids_query = session.query(characteristics.id)\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(inspection_reports, (inspection_reports.id == checks.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        characteristic_ids = [x[0] for x in characteristic_ids_query]

        deviation_ids_query = session.query(deviations.id)\
            .join(characteristics, (characteristics.id == deviations.characteristic_id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(inspection_reports, (inspection_reports.id == checks.inspection_id))\
            .filter(inspection_reports.id == inspection_id).all()
        deviation_ids = [x[0] for x in deviation_ids_query]

        # delete the referenced records
        deviations_deleted = session.query(deviations)\
            .filter(deviations.id.in_(deviation_ids)).delete(synchronize_session = False)

        characteristics_deleted = session.query(characteristics)\
            .filter(characteristics.id.in_(characteristic_ids)).delete(synchronize_session = False)

        checks_deleted = session.query(checks)\
            .filter(checks.id.in_(check_ids)).delete(synchronize_session = False)

        inspection_reports_query = session.query(inspection_reports)\
            .filter(inspection_reports.id == inspection_id).delete(synchronize_session = False)

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        return func_data_entry_inspection_reports_get_filtered_reports(part_id, job_order_id, started_after, finished_before)

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/data_entry/inspection_reports_get_filtered_reports/", methods = ["POST"])
def data_entry_inspection_reports_get_filtered_reports():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    part_id = int(form_data["part_id"])
    job_order_id = int(form_data["job_order_id"])
    started_after_str = form_data["started_after"]
    finished_before_str = form_data["finished_before"]

    # convert date strings to datetime objects
    started_after = datetime.date(1970, 1, 1)
    finished_before = datetime.date(2100, 1, 1)
    if started_after_str != "":
        started_after = datetime.datetime.strptime(started_after_str, "%Y-%m-%d")
    if finished_before_str != "":
        finished_before = datetime.datetime.strptime(finished_before_str, "%Y-%m-%d")

    return func_data_entry_inspection_reports_get_filtered_reports(part_id, job_order_id, started_after, finished_before)

@app.route("/data_entry/get_filtered_parts/", methods = ["POST"])
def data_entry_get_filtered_parts():

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
            .order_by(parts.item.asc(), parts.drawing.asc()).all()

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
    search_term = form_data["search_term"]

    # define the output columns
    columns = [
        characteristic_schemas.id,
        characteristic_schemas.is_locked,
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
            .join(parts, (parts.id == characteristic_schemas.part_id))\
            .filter(or_(parts.item.ilike(f"%{search_term}%"), parts.drawing.ilike(f"%{search_term}%"), parts.revision.ilike(f"%{search_term}%")))\
            .order_by(parts.item.asc(), parts.drawing.asc(), parts.revision.asc()).all()

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
                "response": "no records found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "not_ok",
            "response": error_msg
        }

@app.route("/data_entry/get_filtered_employees/", methods = ["POST"])
def data_entry_get_filtered_employees():

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

# recycled functions

def func_data_entry_inspection_reports_get_filtered_reports(part_id:int, job_order_id:int, started_after:datetime, finished_before:datetime):

    # define the required fields
    columns = [
        inspection_reports.id,
        parts.id,
        parts.item,
        parts.drawing,
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
        results = session.query(*columns)\
            .join(checks, (checks.inspection_id == inspection_reports.id))\
            .join(parts, (checks.part_id == parts.id))\
            .join(job_orders, (inspection_reports.job_order_id == job_orders.id), isouter = True)\
            .filter(checks.datetime_measured >= started_after)\
            .filter(or_(checks.datetime_measured <= finished_before, checks.datetime_measured == None))
        
        # additional filtering
        if part_id >= 0:
            part_query = session.query(parts.item, parts.drawing)\
                .filter(parts.id == part_id)\
                .first()
            if part_query is None:
                session.close()
                return {
                    "status": "alert",
                    "response": "the supplied part does not exist in 'parts'"
                }
            results = results.filter(parts.item.ilike(f"%{part_query[0]}%"))\
                .filter(parts.drawing.ilike(f"%{part_query[1]}%"))
        if job_order_id >= 0:
            results = results.filter(job_orders.id == job_order_id)

        # convert to list of tuples
        results = results\
            .order_by(parts.drawing.asc(), parts.item.asc())\
            .distinct(parts.drawing, parts.item).all()

        # close the database session
        session.close()

        # return the results
        if len(results) > 0:
            output_arr = []
            for inspection_id, part_id, item, drawing, job_order_id, job_order, disposition_type_id, material_type_id, employee_id, supplier_id in results:
                output_arr.append({
                    "inspection_id": inspection_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "job_order_id": job_order_id,
                    "job_order": job_order,
                    "disposition_type_id": disposition_type_id,
                    "material_type_id": material_type_id,
                    "employee_id": employee_id,
                    "supplier_id": supplier_id
                })

            return {
                "status": "ok",
                "response": output_arr
            }
        else:
            return {
                "status": "alert",
                "response": "no matching records found in 'inspection_reports', 'parts', 'job_orders', and 'checks'"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

def func_data_entry_inspection_reports_add_new_check_set(part_id:int, inspection_id:int, schema_id:int, employee_id:int, part_index:int):

    # schema detail columns
    schema_details_columns = [
        characteristic_schema_details.name,
        characteristic_schema_details.nominal,
        characteristic_schema_details.usl,
        characteristic_schema_details.lsl,
        characteristic_schema_details.precision,
        characteristic_schema_details.specification_type_id,
        characteristic_schema_details.characteristic_type_id,
        characteristic_schema_details.frequency_type_id,
        characteristic_schema_details.gauge_type_id
    ]

    try:

        # open the database session
        session = Session(engine)

        # check for schema
        schema_query = session.query(parts.item, parts.drawing)\
            .join(characteristic_schemas, (characteristic_schemas.part_id == parts.id))\
            .filter(characteristic_schemas.id == schema_id).first()
        if schema_query is None:
            session.close()
            return {
                "status": "alert",
                "response": f"the referenced characteristic schema ({schema_id}) does not exist in the database"
            }
        schema_item, schema_drawing = schema_query

        # check for part
        part_query = session.query(parts.item, parts.drawing)\
            .filter(parts.id == part_id).first()
        if part_query is None:
            session.close()
            return {
                "status": "alert",
                "response": f"the referenced part ({part_id}) does not exist in the database"
            }
        part_item, part_drawing = part_query

        # check if schema and part match up
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
                .join(checks, (checks.part_id == parts.id))\
                .join(inspection_reports, (inspection_reports.id == checks.inspection_id))\
                .filter(inspection_reports.id == inspection_id).first()
            if inspection_query is None:
                session.close()
                return {
                    "status": "alert",
                    "response": f"the referenced inspection report ({inspection_id}) does not exist in the database"
                }
            inspection_item, inspection_drawing = inspection_query

            # check if the inspection and part match up
            if inspection_item != part_item and inspection_drawing != part_drawing:
                session.close()
                return {
                    "status": "alert",
                    "response": "the provided inspection report does not match the provided part"
                }

        # calculate the part index if the provided part_index is -1
        if part_index == -1:
            part_index_arr = session.query(checks.part_index)\
                .filter(checks.part_id == part_id)\
                .filter(checks.inspection_id == inspection_id).all()
            part_index = max([x[0] for x in part_index_arr]) + 1

        # create a new check set
        check_query = checks(
            part_index = part_index,
            datetime_measured = datetime.datetime.now(),
            inspection_id = inspection_id,
            part_id = part_id,
            employee_id = employee_id
        )
        session.add(check_query)
        session.commit()
        check_id = check_query.id

        # get the schema details
        schema_details = session.query(*schema_details_columns)\
            .filter(characteristic_schema_details.schema_id == schema_id)\
            .order_by(characteristic_schema_details.name.asc()).all()
        schema_details_list = []
        for name, nominal, usl, lsl, precision, spectype, chartype, freqtype, gauge_type_id in schema_details:

            new_gauge_id = session.query(gauges.id)\
                .join(characteristic_schema_details, (characteristic_schema_details.gauge_type_id == gauges.gauge_type_id))\
                .filter(characteristic_schema_details.gauge_type_id == gauge_type_id)\
                .order_by(gauges.name.asc())\
                .first()[0]

            schema_details_list.append({
                "name": name,
                "nominal": nominal,
                "usl": usl,
                "lsl": lsl,
                "precision": precision,
                "specification_type_id": spectype,
                "characteristic_type_id": chartype,
                "frequency_type_id": freqtype,
                "gauge_id": new_gauge_id
            })

        # create the characteristic records
        for obj in schema_details_list:
            characteristics_query = characteristics(
                name = obj["name"],
                nominal = obj["nominal"],
                usl = obj["usl"],
                lsl = obj["lsl"],
                precision = obj["precision"],
                check_id = check_id,
                specification_type_id = obj["specification_type_id"],
                characteristic_type_id = obj["characteristic_type_id"],
                frequency_type_id = obj["frequency_type_id"],
                gauge_id = obj["gauge_id"]
            )
            session.add(characteristics_query)
        session.commit()

        # close the database session
        session.close()

        # get the updated characteristics
        return func_data_entry_characteristic_display_get_filtered_characteristics(
            inspection_id,
            schema_item,
            schema_drawing,
            -1,
            -1,
            "",
            "",
            -1,
            -1,
            -1,
            -1,
            -1,
            -1
        )

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - characteristic display

@app.route("/data_entry/characteristic_display_get_filtered_characteristics/", methods = ["POST"])
def data_entry_characteristic_display_get_filtered_characteristics():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["identity"]["inspection_id"])
    item = form_data["identity"]["item"]
    drawing = form_data["identity"]["drawing"]
    part_index = int(form_data["content"]["part_index"])
    frequency_type_id = int(form_data["content"]["frequency_type_id"])
    revision = form_data["content"]["revision"]
    name = form_data["content"]["name"]
    has_deviations = int(form_data["content"]["has_deviations"])
    inspector_id = int(form_data["content"]["inspector_id"])
    gauge_id = int(form_data["content"]["gauge_id"])
    gauge_type_id = int(form_data["content"]["gauge_type_id"])
    specification_type_id = int(form_data["content"]["specification_type_id"])
    characteristic_type_id = int(form_data["content"]["characteristic_type_id"])

    # run the required function
    return func_data_entry_characteristic_display_get_filtered_characteristics(
        inspection_id,
        item,
        drawing,
        part_index,
        frequency_type_id,
        revision,
        name,
        has_deviations,
        inspector_id,
        gauge_id,
        gauge_type_id,
        specification_type_id,
        characteristic_type_id
    )

@app.route("/data_entry/characteristic_display_save_characteristics/", methods = ["POST"])
def data_entry_characteristic_display_save_characteristics():

    # interpret the posted data
    form_data = json.loads(request.data)

    # proceed if the dictionary has contents
    if len(form_data["checks"]) > 0 and len(form_data["characteristics"]) > 0:
        try:

            # open the database session
            session = Session(engine)

            # assign new check table values
            check_rows_affected = 0
            for obj in form_data["checks"]:

                # narrow the database scope
                results = session.query(checks)\
                    .filter(checks.id == obj["check_id"])

                is_affected = 0
                for x in obj["contents"]:
                    is_affected += results.update({ x["key"]: x["value"] })
                if is_affected > 0:
                    check_rows_affected += len(results.all())

            # assign new characteristic table values
            characteristic_rows_affected = 0
            for obj in form_data["characteristics"]:

                # narrow the database scope
                results = session.query(characteristics)\
                    .filter(characteristics.id == obj["characteristic_id"])

                is_affected = 0
                for x in obj["contents"]:
                    is_affected += results.update({ x["key"]: x["value"] })
                if is_affected > 0:
                    characteristic_rows_affected += len(results.all())

            # commit the changes
            session.commit()

            # close the database session
            session.close()

            # return the result
            if check_rows_affected > 0 and characteristic_rows_affected > 0:
                return {
                    "status": "ok",
                    "response": f"{check_rows_affected} 'check' table rows and {characteristic_rows_affected} 'characteristic' table rows were updated"
                }
            else:
                return {
                    "status": "alert",
                    "response": "no rows affected"
                }

        except SQLAlchemyError as e:
            error_msg = str(e.__dict__["orig"])
            return {
                "status": "log",
                "response": error_msg
            }

    else:
        return {
            "status": "alert",
            "response": "no data passed to flask server"
        }

@app.route("/data_entry/characteristic_display_tunnel_to_physical_part/", methods = ["POST"])
def data_entry_characteristic_display_tunnel_to_physical_part():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    part_id = int(form_data["part_id"])

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
        return func_data_entry_characteristic_display_get_filtered_characteristics(
            inspection_id,
            item,
            drawing,
            -1,
            -1,
            revision,
            "",
            -1,
            -1,
            -1,
            -1,
            -1,
            -1
        )

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/data_entry/characteristic_display_delete_check_set/", methods = ["POST"])
def data_entry_characteristic_display_delete_check_set():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    check_id = int(form_data["identity"]["check_id"])
    inspection_id = int(form_data["identity"]["inspection_id"])
    item = form_data["identity"]["item"]
    drawing = form_data["identity"]["drawing"]
    part_index = int(form_data["content"]["part_index"])
    frequency_type_id = int(form_data["content"]["frequency_type_id"])
    revision = form_data["content"]["revision"]
    name = form_data["content"]["name"]
    has_deviations = int(form_data["content"]["has_deviations"])
    inspector_id = int(form_data["content"]["inspector_id"])
    gauge_id = int(form_data["content"]["gauge_id"])
    gauge_type_id = int(form_data["content"]["gauge_type_id"])
    specification_type_id = int(form_data["content"]["specification_type_id"])
    characteristic_type_id = int(form_data["content"]["characteristic_type_id"])

    try:

        # open the database session
        session = Session(engine)

        # assign characteristics for deletion
        characteristics_deleted = session.query(characteristics)\
            .filter(characteristics.check_id == check_id)\
            .delete()

        # assign checks for deletion
        checks_deleted = session.query(checks)\
            .filter(checks.id == check_id)\
            .delete()

        # commit the changes
        session.commit()

        # close the database session
        session.close()

        # return the results
        if characteristics_deleted == 0 or checks_deleted == 0:
            return {
                "status": "alert",
                "response": "records not found; none deleted"
            }

        # run the required function
        return func_data_entry_characteristic_display_get_filtered_characteristics(
            inspection_id,
            item,
            drawing,
            part_index,
            frequency_type_id,
            revision,
            name,
            has_deviations,
            inspector_id,
            gauge_id,
            gauge_type_id,
            specification_type_id,
            characteristic_type_id
        )

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

@app.route("/data_entry/characteristic_display_get_filter_selector_lists/", methods = ["POST"])
def data_entry_characteristic_display_get_filter_selector_lists():
    
    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    inspection_id = int(form_data["inspection_id"])
    item = form_data["item"]
    drawing = form_data["drawing"]

    try:

        # open the database session
        session = Session(engine)

        # frequency type list
        frequency_types_query = session.query(frequency_types.id, frequency_types.name)\
            .join(characteristics, (characteristics.frequency_type_id == frequency_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(frequency_types.name.asc()).distinct(frequency_types.name).all()

        # revisions list
        revisions_query = session.query(parts.id, parts.revision)\
            .join(checks, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(parts.revision.asc()).distinct(parts.revision).all()

        # part indices list
        part_indices_query = session.query(checks.part_index)\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(checks.part_index.asc()).distinct(checks.part_index).all()

        # inspectors list
        inspectors_query = session.query(employees.id, employees.first_name, employees.last_name)\
            .join(checks, (checks.employee_id == employees.id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).distinct(employees.first_name, employees.last_name).all()

        # gauges list
        gauges_query = session.query(gauges.id, gauges.name)\
            .join(characteristics, (characteristics.gauge_id == gauges.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauges.name.asc()).distinct(gauges.name).all()

        # gauges types list
        gauge_types_query = session.query(gauge_types.id, gauge_types.name)\
            .join(gauges, (gauges.gauge_type_id == gauge_types.id))\
            .join(characteristics, (characteristics.gauge_id == gauges.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(gauge_types.name.asc()).distinct(gauge_types.name).all()

        # specification types list
        specification_types_query = session.query(specification_types.id, specification_types.name)\
            .join(characteristics, (characteristics.specification_type_id == specification_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(specification_types.name.asc()).distinct(specification_types.name).all()

        # characteristic types list
        characteristic_types_query = session.query(characteristic_types.id, characteristic_types.name)\
            .join(characteristics, (characteristics.characteristic_type_id == characteristic_types.id))\
            .join(checks, (checks.id == characteristics.check_id))\
            .join(parts, (checks.part_id == parts.id))\
            .filter(checks.inspection_id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"{drawing}%")))\
            .order_by(characteristic_types.name.asc()).distinct(characteristic_types.name).all()

        # close the database session
        session.close()

        # return the results
        if len(frequency_types_query) > 0 and len(revisions_query) > 0 and len(inspectors_query) > 0 and len(gauges_query) > 0 and len(gauge_types_query) > 0 and len(specification_types_query) > 0 and len(characteristic_types_query) > 0:

            frequency_types_list = []
            for id, name in frequency_types_query:
                frequency_types_list.append({
                    "id": id,
                    "name": name
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
                "status": "ok",
                "response": {
                    "frequency_types": frequency_types_list,
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
                "status": "log",
                "response": "queries returned null values"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

# recycled functions

def func_data_entry_characteristic_display_get_filtered_characteristics(inspection_id:int, item:str, drawing:str, part_index:int, frequency_type_id:int, revision:str, name:str, has_deviations:int, inspector_id:int, gauge_id:int, gauge_type_id:int, specification_type_id:int, characteristic_type_id:int):

    # deviation prefix
    deviation_prefix = {
        True: "**",
        False: ""
    }

    # define the columns
    columns = [
        checks.id,
        checks.part_index,
        parts.id,
        parts.revision,
        characteristics.name,
        characteristics.nominal,
        characteristics.usl,
        characteristics.lsl,
        characteristics.measured,
        characteristics.precision,
        checks.employee_id,
        gauges.id,
        gauge_types.id,
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
            .filter(inspection_reports.id == inspection_id)\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%")))\
            .filter(characteristics.name.ilike(f"%{name}%"))\
            .filter(parts.revision.ilike(f"%{revision}%"))

        if part_index > -1:
            results = results.filter(checks.part_index == part_index)
        if frequency_type_id > -1:
            results = results.filter(characteristics.frequency_type_id == frequency_type_id)
        if has_deviations == 0:
            results = results.filter(characteristics.id.notin_(session.query(deviations.characteristic_id)))
        elif has_deviations == 1:
            results = results.filter(characteristics.id.in_(session.query(deviations.characteristic_id)))
        if inspector_id > -1:
            results = results.filter(checks.employee_id == inspector_id)
        if gauge_id > -1:
            results = results.filter(characteristics.gauge_id == gauge_id)
        if gauge_type_id > -1:
            results = results.filter(gauges.gauge_type_id == gauge_type_id)
        if specification_type_id > -1:
            results = results.filter(characteristics.specification_type_id == specification_type_id)
        if characteristic_type_id > -1:
            results = results.filter(characteristics.characteristic_type_id == characteristic_type_id)

        # convert to a list
        characteristic_list = results\
            .order_by(checks.id.asc(), checks.part_id.asc(), parts.revision.asc(), characteristics.id.asc(), characteristics.name.asc()).all()

        # get the list of characteristics that have deviations
        deviations_list = [x[0] for x in session.query(deviations.characteristic_id).all()]

        # get the list of inspectors
        inspectors_list = session.query(employees.id, employees.first_name, employees.last_name).order_by(employees.last_name.asc(), employees.first_name.asc()).all()

        # get the list of gauges
        gauges_list = session.query(gauges.id, gauges.name).order_by(gauges.name.asc()).all()

        # close the database session
        session.close()

        # return the results
        if len(characteristic_list) > 0 and len(inspectors_list) > 0 and len(gauges_list) > 0:

            # assemble characteristics output
            output_arr = []
            for check_id, part_index, part_id, revision, name, nominal, usl, lsl, measured, precision, employee_id, gauge_id, gauge_type_id, gauge_type, specification_type, characteristic_type, frequency_type, characteristic_id in characteristic_list:

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

                # check for deviation flag
                has_deviations = characteristic_id in deviations_list

                output_arr.append({
                    "inspection_id": inspection_id,
                    "part_id": part_id,
                    "item": item,
                    "drawing": drawing,
                    "has_deviations": has_deviations,
                    "characteristic_id": characteristic_id,
                    "check_id": check_id,
                    "part_index": part_index,
                    "revision": revision.upper(),
                    "name": f"{deviation_prefix[has_deviations]}{name}",
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
                    "characteristic_type": characteristic_type,
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
                "response": "no matching characteristics found"
            }

    except SQLAlchemyError as e:
        error_msg = str(e.__dict__["orig"])
        return {
            "status": "log",
            "response": error_msg
        }

#endregion

#region inspection reports - metadata

@app.route("/data_entry/get_matching_revisions/", methods = ["POST"])
def data_entry_get_matching_revisions():

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

@app.route("/data_entry/save_metadata/", methods = ["POST"])
def data_entry_save_metadata():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    item = form_data["identity"]["item"]
    drawing = form_data["identity"]["drawing"]
    inspection_id = form_data["identity"]["inspection_id"]

    try:

        # open the database session
        session = Session(engine)

        # make sure the report/part combination exists
        results = session.query(inspection_reports.id).distinct(inspection_reports.id)\
            .join(checks, (checks.inspection_id == inspection_reports.id))\
            .join(parts, (parts.id == checks.part_id))\
            .filter(and_(parts.item.ilike(f"%{item}%"), parts.drawing.ilike(f"%{drawing}%"), inspection_reports.id == inspection_id)).all()
        if len(results) == 0:
            return {
                "status": "log",
                "response": "no matching inspection report and part found"
            }

        # update the inspection report
        results = session.query(inspection_reports).filter(inspection_reports.id == inspection_id)
        ir_is_affected = 0
        for k, v in form_data["content"].items():
            ir_is_affected = results.update({ k: v })

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

#endregion

#region inspection reports - receiver numbers / purchase orders / lot numbers

# routes

@app.route("/data_entry/reciever_numbers_assign_association/", methods = ["POST"])
def data_entry_reciever_numbers_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    receiver_number_id = int(form_data["receiver_number_id"])

    # run the targeted method
    return func_data_entry_inspection_association_add(
        search_term,
        inspection_id,
        receiver_number_id,
        "receiver number",
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/data_entry/reciever_numbers_remove_association/", methods = ["POST"])
def data_entry_reciever_numbers_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    receiver_number_id = int(form_data["receiver_number_id"])

    # run the targeted method
    return func_data_entry_inspection_association_remove(
        search_term,
        inspection_id,
        receiver_number_id,
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/data_entry/receiver_numbers_get_filtered_options/", methods = ["POST"])
def data_entry_receiver_numbers_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_data_entry_inspection_get_filtered_potential_associations(
        search_term,
        receiver_numbers,
    )

@app.route("/data_entry/receiver_numbers_get_filtered_associations/", methods = ["POST"])
def data_entry_receiver_numbers_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_data_entry_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "receiver_number_id",
        receiver_numbers,
        inspection_receiver_numbers
    )

@app.route("/data_entry/purchase_orders_assign_association/", methods = ["POST"])
def data_entry_purchase_orders_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    # run the targeted method
    return func_data_entry_inspection_association_add(
        search_term,
        inspection_id,
        purchase_order_id,
        "purchase number",
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/data_entry/purchase_orders_remove_association/", methods = ["POST"])
def data_entry_purchase_orders_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    purchase_order_id = int(form_data["purchase_order_id"])

    # run the targeted method
    return func_data_entry_inspection_association_remove(
        search_term,
        inspection_id,
        purchase_order_id,
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/data_entry/purchase_orders_get_filtered_options/", methods = ["POST"])
def data_entry_purchase_orders_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_data_entry_inspection_get_filtered_potential_associations(
        search_term,
        purchase_orders,
    )

@app.route("/data_entry/purchase_orders_get_filtered_associations/", methods = ["POST"])
def data_entry_purchase_order_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_data_entry_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "purchase_order_id",
        purchase_orders,
        inspection_purchase_orders
    )

@app.route("/data_entry/lot_numbers_assign_association/", methods = ["POST"])
def data_entry_lot_numbers_assign_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_data_entry_inspection_association_add(
        search_term,
        inspection_id,
        lot_number_id,
        "lot number",
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

@app.route("/data_entry/lot_numbers_remove_association/", methods = ["POST"])
def data_entry_lot_numbers_remove_association():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])
    lot_number_id = int(form_data["lot_number_id"])

    # run the targeted method
    return func_data_entry_inspection_association_remove(
        search_term,
        inspection_id,
        lot_number_id,
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

@app.route("/data_entry/lot_numbers_get_filtered_options/", methods = ["POST"])
def data_entry_lot_numbers_get_filtered_options():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])

    return func_data_entry_inspection_get_filtered_potential_associations(
        search_term,
        lot_numbers,
    )

@app.route("/data_entry/lot_numbers_get_filtered_associations/", methods = ["POST"])
def data_entry_lot_numbers_get_filtered_associations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    search_term = str(form_data["search_term"])
    inspection_id = int(form_data["inspection_id"])

    return func_data_entry_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        "lot_number_id",
        lot_numbers,
        inspection_lot_numbers
    )

# recycled functions

def func_data_entry_inspection_association_add(search_term:str, inspection_id:int, id:int, descriptor:str, link_field:str, solo_table, link_table):

    try:

        # open the database session
        session = Session(engine)

        # check if the association already exists
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
    
    return func_data_entry_inspection_get_filtered_associations(
        search_term,
        inspection_id,
        link_field,
        solo_table,
        link_table
    )

def func_data_entry_inspection_association_remove(search_term:str, inspection_id:int, id:int, link_field:str, solo_table, link_table):

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

    return func_data_entry_inspection_get_filtered_associations(search_term, inspection_id, link_field, solo_table, link_table)

def func_data_entry_inspection_get_filtered_associations(search_term:str, inspection_id:int, link_field:str, solo_table, link_table):

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

def func_data_entry_inspection_get_filtered_potential_associations(search_term:str, solo_table):

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

@app.route("/data_entry/save_deviations/", methods = ["POST"])
def data_entry_save_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)
    print(form_data)
    try:

        # open the database session
        session = Session(engine)

        # query the database
        is_affected = 0
        for row in form_data["data"]:
            deviation_id = row["deviation_id"]
            results = session.query(deviations).filter(deviations.id == deviation_id)

            for k, v in row["content"].items():
                is_affected += results.update({ k: v })

        # commit the changes
        session.commit()

        # close the session
        session.close()

        # return the results
        if is_affected > 0:
            return {
                "status": "alert",
                "response": f"{is_affected} records in 'deviations' has been successfully updated"
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

@app.route("/data_entry/deviations_get_characteristic_deviations/", methods = ["POST"])
def data_entry_deviations_get_characteristic_deviations():

    # interpret the posted data
    form_data = json.loads(request.data)

    # get the required parameters
    characteristic_id = form_data["characteristic_id"]

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
            .filter(deviations.characteristic_id == characteristic_id)\
            .order_by(deviations.id.asc())\
            .distinct(deviations.id).all()
        deviation_type_list = session.query(deviation_types.id, deviation_types.name)\
            .order_by(deviation_types.name.asc()).all()
        employee_list = session.query(employees.id, employees.first_name, employees.last_name)\
            .order_by(employees.last_name.asc(), employees.first_name.asc()).all()

        # close the session
        session.close()

        # return the results
        if len(results) > 0 and len(deviation_type_list) > 0 and len(employee_list) > 0:

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

            deviation_types_lst = []
            for id, name in deviation_type_list:
                deviation_types_lst.append({
                    "id": id,
                    "name": name
                })

            employees_lst = []
            for id, first_name, last_name in employee_list:
                employees_lst.append({
                    "id": id,
                    "name": f"{last_name}, {first_name}"
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