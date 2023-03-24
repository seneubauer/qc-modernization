# import dependencies for flask
from flask import Flask, render_template, send_from_directory

# import dependencies for sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, and_, or_

# import general dependencies
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

# instantiate the flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# data entry
@app.route("/data_entry")
def data_entry_route():
    return render_template("data_entry.html")



@app.route("/get_all_employee_ids/")
def get_all_employees():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(employees.id).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_all_disposition_types/")
def get_all_disposition_types():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(disposition_types.id).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_all_item_numbers/")
def get_all_item_numbers():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(parts.item).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_all_drawings/")
def get_all_drawings():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(parts.drawing).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_all_job_orders/")
def get_all_job_orders():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(job_orders.id).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_all_receiver_numbers/")
def get_all_receiver_numbers():

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(receiver_numbers.id).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })
        
        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/inspection_report_drawing_changed/<string:drawing>/")
def inspection_report_drawing_changed(drawing:str):

    # open the database connection
    session = Session(engine)

    # query the database
    results = session.query(parts.item)\
        .filter(parts.drawing == drawing).all()
    
    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for item in results:
            output_arr.append({
                "id": item[0]
            })
        
        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/assign_receiver_number_association/<int:report_id>/<string:receiver_number>")
def assign_receiver_number_association(report_id:int, receiver_number:str):

    # open the database session
    session = Session(engine)

    # query the database
    exists_result = session.query(inspection_receiver_numbers.id)\
        .filter(and_(inspection_receiver_numbers.inspection_id == report_id, inspection_receiver_numbers.receiver_number_id == receiver_number)).all()

    added = False
    if len(exists_result) > 0:
        added = False
    else:
        session.add(inspection_receiver_numbers(inspection_id = report_id, receiver_number_id = receiver_number))
        session.commit()
        added = True

    # close the session
    session.close()

    return {
        "status": "ok",
        "response": added
    }

@app.route("/get_receiver_numbers_from_report_id/<int:report_id>/")
def get_receiver_numbers_from_report_id(report_id:int):

    # open the database session
    session = Session(engine)

    # query the database
    results = session.query(receiver_numbers.id)\
        .join(inspection_receiver_numbers, (receiver_numbers.id == inspection_receiver_numbers.receiver_number_id))\
        .join(inspection_reports, (inspection_reports.id == inspection_receiver_numbers.inspection_id))\
        .filter(inspection_reports.id == report_id).all()

    # close the session
    session.close()

    # return the results
    if len(results) > 0:
        output_arr = []
        for id in results:
            output_arr.append({
                "id": id[0]
            })

        return {
            "status": "ok",
            "response": output_arr
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

@app.route("/get_inspection_reports/<int:filter_type>/<string:filter_term>/<string:use_date_span>/<int:start_day>/<int:start_month>/<int:start_year>/<int:stop_day>/<int:stop_month>/<int:stop_year>/")
def get_inspection_reports(filter_type:int, filter_term:str, use_date_span:str, start_day:int, start_month:int, start_year:int, stop_day:int, stop_month:int, stop_year:int):

    # build the filtering dates
    start_date = datetime.date(start_year, start_month, start_day)
    stop_date = datetime.date(stop_year, stop_month, stop_day)

    # define the output fields
    output_arr = [
        inspection_reports.id,
        parts.drawing,
        parts.revision,
        parts.item,
        inspection_reports.day_started,
        inspection_reports.day_finished,
        inspection_reports.employee_id,
        inspection_reports.disposition,
        inspection_reports.job_order_id
    ]

    # open the database session
    session = Session(engine)

    # start the database query
    results = session.query(*output_arr).join(parts, (parts.id == inspection_reports.part_id))

    # add the date filtering
    if use_date_span == "true":
        results = results.filter(and_(inspection_reports.day_started >= start_date, inspection_reports.day_finished <= stop_date))

    # add the drawing or item filtering
    if filter_type == 1:
        results = results.filter(parts.drawing.like(f"%{filter_term}%"))
    elif filter_type == 2:
        results = results.filter(parts.item.like(f"%{filter_term}%"))

    # close the session
    session.close()

    # assemble the results
    results_list = results.all()
    output_data = []
    if len(results_list) > 0:
        for id, drawing, revision, item, started, finished, employee_id, disposition, job_order_id in results_list:
            output_data.append({
                "report_id": id,
                "drawing": drawing,
                "item_number": item,
                "revision": revision.upper(),
                "start_year": started.year,
                "start_month": started.month,
                "start_day": started.day,
                "finish_year": finished.year,
                "finish_month": finished.month,
                "finish_day": finished.day,
                "started": f"{started.month:02}/{started.day:02}/{started.year:04}",
                "finished": f"{finished.month:02}/{finished.day:02}/{finished.year:04}",
                "employee": employee_id,
                "disposition": disposition,
                "job_order": job_order_id
            })

        return {
            "status": "ok",
            "response": output_data
        }
    else:
        return {
            "status": "not_ok",
            "response": "error within the flask server or database query"
        }

# run the flask server
if __name__ == "__main__":
    app.run(debug = True, port = 8000)