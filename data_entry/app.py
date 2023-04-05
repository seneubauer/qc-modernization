# import dependencies for flask
from flask import Flask, render_template, redirect, request

# import dependencies for sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, and_, or_

# import general dependencies
import datetime
from math import isnan

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
disposition_types = base.classes.disposition_types
employee_projects = base.classes.employee_projects
employees = base.classes.employees
gauge_types = base.classes.gauge_types
gauges = base.classes.gauges
inspection_purchase_orders = base.classes.inspection_purchase_orders
inspection_receiver_numbers = base.classes.inspection_receiver_numbers
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
characteristics = base.classes.characteristics
material_types = base.classes.material_types
quantity_types = base.classes.quantity_types
suppliers = base.classes.suppliers

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/test_page/")
def test_page():
    return render_template("test_page.html")

@app.route("/get_all_employee_ids/")
def get_all_employees_ids():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_disposition_types/")
def get_all_disposition_types():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_item_numbers/")
def get_all_item_numbers():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(parts.item).order_by(parts.drawing.asc()).all()

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_drawings/")
def get_all_drawings():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(parts.drawing).order_by(parts.drawing.asc()).all()

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_job_order_ids/")
def get_all_job_order_ids():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_material_types/")
def get_all_material_types():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_suppliers/")
def get_all_suppliers():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_quantity_types/")
def get_all_quantity_types():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(quantity_types.id).order_by(quantity_types.id.asc()).all()

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_receiver_numbers/")
def get_all_receiver_numbers():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_all_purchase_orders/")
def get_all_purchase_orders():

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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_drawing_from_item_number/<string:item_number>/")
def get_drawing_from_item_number(item_number:str):

    # open the database session
    session = Session(engine)

    # query the database
    result = session.query(parts.drawing).filter(parts.item == item_number).first()

    # close the session
    session.close()

    # return the result
    if result is not None:
        return {
            "status": "ok",
            "response": result[0]
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_item_number_from_drawing/<string:drawing>/")
def get_item_number_from_drawing(drawing:str):

    # open the database session
    session = Session(engine)

    # query the database
    result = session.query(parts.item).filter(parts.drawing == drawing).first()

    # close the session
    session.close()

    # return the result
    if result is not None:
        return {
            "status": "ok",
            "response": result[0]
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/get_filtered_inspection_reports/<string:item_number>/<string:drawing>/<int:start_day>/<int:start_month>/<int:start_year>/<int:finish_day>/<int:finish_month>/<int:finish_year>/")
def get_filtered_inspection_reports(item_number:str, drawing:str, start_day:int, start_month:int, start_year:int, finish_day:int, finish_month:int, finish_year:int):

    # interpret the parameters
    started_after = datetime.date(start_year, start_month, start_day)
    finished_before = datetime.date(finish_year, finish_month, finish_day)
    if item_number == "__null":
        item_number = ""
    if drawing == "__null":
        drawing = ""

    # define the required fields
    columns = [
        inspection_reports.id,
        inspection_reports.employee_id,
        inspection_reports.disposition,
        parts.item,
        parts.drawing,
        parts.revision,
        inspection_reports.job_order_id,
        inspection_reports.material_type_id,
        inspection_reports.supplier_id,
        inspection_reports.day_started,
        inspection_reports.day_finished,
        inspection_reports.full_inspect_qty_type,
        inspection_reports.full_inspect_qty,
        inspection_reports.released_qty_type,
        inspection_reports.released_qty,
        inspection_reports.completed_qty_type,
        inspection_reports.completed_qty
    ]

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(*columns).join(inspection_reports, (inspection_reports.part_id == parts.id))\
        .filter(and_(inspection_reports.day_started >= started_after, inspection_reports.day_finished <= finished_before))\
        .filter(parts.item.like(f"%{item_number}%"))\
        .filter(parts.drawing.like(f"%{drawing}%"))\
        .order_by(parts.drawing.asc()).all()

    # close the database session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for report_id, employee_id, disposition, item, drawing, revision, job_order_id, material_type_id, supplier_id, day_started, day_finished, full_inspect_type, full_inspect_qty, released_type, released_qty, completed_type, completed_qty in results:
            output_arr.append({
                "report_id": report_id,
                "employee_id": employee_id,
                "disposition": disposition,
                "item": item,
                "drawing": drawing,
                "revision": revision,
                "job_order_id": job_order_id,
                "material_type_id": material_type_id,
                "supplier_id": supplier_id,
                "day_started": f"{day_started.month:02}/{day_started.day:02}/{day_started.year:04}",
                "day_finished": f"{day_finished.month:02}/{day_finished.day:02}/{day_finished.year:04}",
                "js_day_started": f"{day_started.year:04}-{day_started.month:02}-{day_started.day:02}",
                "js_day_finished": f"{day_finished.year:04}-{day_finished.month:02}-{day_finished.day:02}",
                "full_inspect_type": full_inspect_type,
                "full_inspect_qty": full_inspect_qty,
                "released_type": released_type,
                "released_qty": released_qty,
                "completed_type": completed_type,
                "completed_qty": completed_qty
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

# data entry
# @app.route("/data_entry")
# def data_entry_route():
    return render_template("data_entry.html")

@app.route("/get_filtered_receiver_numbers/<int:report_id>/<string:filter>/")
def get_filtered_receiver_numbers(report_id:int, filter:str):

    # convert the incoming filter if needed
    if filter == "__null":
        filter = ""
    
    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(receiver_numbers.id)\
        .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
        .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
        .filter(inspection_reports.id == report_id)\
        .filter(receiver_numbers.id.like(f"%{filter}%"))\
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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/assign_receiver_number_association/<int:report_id>/<string:receiver_number>/")
def assign_receiver_number_association(report_id:int, receiver_number:str):

    # open the database session
    session = Session(engine)

    # check if the association already exists
    results = session.query(inspection_receiver_numbers.inspection_id)\
        .filter(and_(inspection_receiver_numbers.inspection_id == report_id, inspection_receiver_numbers.receiver_number_id == receiver_number)).all()

    # logic gate
    if len(results) > 0:
        return {
            "status": "ok_alt",
            "response": "this receiver number association already exists"
        }
    
    # add the new association
    session.add(inspection_receiver_numbers(inspection_id = report_id, receiver_number_id = receiver_number))
    session.commit()

    # close the session
    session.close()

    # get the new list
    return get_filtered_receiver_numbers(report_id, "")

@app.route("/remove_receiver_number_association/<int:report_id>/<string:receiver_number>/")
def remove_receiver_number_association(report_id:int, receiver_number:str):

    # open the database session
    session = Session(engine)

    # delete the record that matches the provided criteria
    results = session.query(inspection_receiver_numbers)\
        .filter(and_(inspection_receiver_numbers.inspection_id == report_id, inspection_receiver_numbers.receiver_number_id == receiver_number))\
        .delete()

    # logic gate
    if results == 0:
        return {
            "status": "ok_alt",
            "response": "no records deleted; none matched the provided criteria"
        }
    else:
        session.commit()

    # close the session
    session.close()

    # get the new list
    return get_filtered_receiver_numbers(report_id, "")

@app.route("/get_filtered_purchase_orders/<int:report_id>/<string:filter>/")
def get_filtered_purchase_orders(report_id:int, filter:str):

    # convert the incoming filter if needed
    if filter == "__null":
        filter = ""
    
    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(purchase_orders.id)\
        .join(inspection_purchase_orders, (purchase_orders.id == inspection_purchase_orders.purchase_order_id))\
        .join(inspection_reports, (inspection_reports.id == inspection_purchase_orders.inspection_id))\
        .filter(inspection_reports.id == report_id)\
        .filter(purchase_orders.id.like(f"%{filter}%"))\
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
            "status": "not_ok",
            "response": "error within the flask server or in the database query"
        }

@app.route("/assign_purchase_order_association/<int:report_id>/<string:purchase_order>/")
def assign_purchase_order_association(report_id:int, purchase_order:str):

    # open the database session
    session = Session(engine)

    # check if the association already exists
    results = session.query(inspection_purchase_orders.inspection_id)\
        .filter(and_(inspection_purchase_orders.inspection_id == report_id, inspection_purchase_orders.purchase_order_id == purchase_order)).all()

    # logic gate
    if len(results) > 0:
        return {
            "status": "ok_alt",
            "response": "this purchase order association already exists"
        }
    
    # add the new association
    session.add(inspection_purchase_orders(inspection_id = report_id, purchase_order_id = purchase_order))
    session.commit()

    # close the session
    session.close()

    # get the new list
    return get_filtered_purchase_orders(report_id, "")

@app.route("/remove_purchase_order_association/<int:report_id>/<string:receiver_number>/")
def remove_purchase_order_association(report_id:int, receiver_number:str):

    # open the database session
    session = Session(engine)

    # delete the record that matches the provided criteria
    results = session.query(inspection_purchase_orders)\
        .filter(and_(inspection_purchase_orders.inspection_id == report_id, inspection_purchase_orders.purchase_order_id == receiver_number))\
        .delete()

    # logic gate
    if results == 0:
        return {
            "status": "ok_alt",
            "response": "no records deleted; none matched the provided criteria"
        }
    else:
        session.commit()

    # close the session
    session.close()

    # get the new list
    return get_filtered_purchase_orders(report_id, "")





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