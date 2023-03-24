// control definitions
let existing_report_button = d3.select("#existing_report_button");
let existing_report_table = d3.select("#existing_reports_table");
let existing_report_filter_type = d3.select("#existing_report_filter_type");
let existing_report_filter_term = d3.select("#existing_report_filter_term");
let existing_report_filter_apply = d3.select("#existing_report_filter_apply");
let existing_report_start_date = d3.select("#existing_report_start_date");
let existing_report_stop_date = d3.select("#existing_report_stop_date");
let existing_report_use_date = d3.select("#existing_report_use_date");

let report_id = d3.select("#report_id");
let report_creator = d3.select("#report_creator");
let report_disposition = d3.select("#report_disposition");
let report_item_number = d3.select("#report_item_number");
let report_drawing = d3.select("#report_drawing");
let report_revision = d3.select("#report_revision");
let report_job_order = d3.select("#report_job_order");
let report_start_date = d3.select("#report_start_date");
let report_finish_date = d3.select("#report_finish_date");

let receiver_number_view_edit = d3.select("#view_edit_receiver_numbers");
let receiver_number_current = d3.select("#current_receiver_number");
let receiver_number_add = d3.select("#add_receiver_number");
let receiver_number_remove = d3.select("#remove_receiver_number");
let receiver_number_group = d3.select("#receiver_number_group");

// add events
existing_report_button.on("click", update_existing_reports_panel);
existing_report_filter_apply.on("click", update_existing_reports_panel);

receiver_number_view_edit.on("click", show_receiver_number_modal);

report_drawing.on("change", drawing_changed);

init();

// #region page initialization

// initialization function
function init()
{
    // populate selectors
    populate_dropdowns();

    // set initial values
    existing_report_start_date.property("value", "1970-01-01");
    existing_report_stop_date.property("value", "1970-01-01");
    existing_report_use_date.property("checked", false);

    report_start_date.property("value", "1970-01-01");
    report_finish_date.property("value", "1970-01-01");
}

// populate dropdowns
function populate_dropdowns()
{
    // get the employee ids
    d3.json("/get_all_employee_ids").then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_creator.selectAll("option")
                .data(returned_object.response)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // get the dispositions
    d3.json("/get_all_disposition_types/").then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_disposition.selectAll("option")
                .data(returned_object.response)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // get the item numbers
    d3.json("/get_all_item_numbers/").then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_item_number.selectAll("option")
                .data(returned_object.response)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // get the drawing numbers
    d3.json("/get_all_drawings/").then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_drawing.selectAll("option")
                .data(returned_object.response)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // get the job orders
    d3.json("/get_all_job_orders/").then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_job_order.selectAll("option")
                .data(returned_object.response)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region existing report

// update the existing reports panel
function update_existing_reports_panel()
{
    // define the filter
    let filter_type = existing_report_filter_type.property("value");
    let filter_term = existing_report_filter_term.property("value");
    let start_date = new Date(existing_report_start_date.property("value") + "T00:00:00");
    let stop_date = new Date(existing_report_stop_date.property("value") + "T00:00:00");
    let use_date = existing_report_use_date.property("checked");
    let start_day = start_date.getDate();
    let start_month = start_date.getMonth() + 1;
    let start_year = start_date.getFullYear();
    let stop_day = stop_date.getDate();
    let stop_month = stop_date.getMonth() + 1;
    let stop_year = stop_date.getFullYear();

    // make sure the filter term is not null
    if (filter_term == "") { filter_term = "null"; }

    // define the route
    let route = `get_inspection_reports/${filter_type}/${filter_term}/${use_date}/${start_day}/${start_month}/${start_year}/${stop_day}/${stop_month}/${stop_year}/`;

    // query the database for inspection reports
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract data from the returned object
            let dataset = returned_object.response;

            // remove previous data
            existing_report_table.selectAll("tbody").remove();

            // create the table rows & attach the row click event
            let rows = existing_report_table.append("tbody").selectAll("tr")
                .data(dataset)
                .enter()
                .append("tr")
                .on("click", (p, data) => inspection_report_selected(data));

            // assign the cell contents
            rows.selectAll("td")
                .data(function (row) {
                    return ["drawing", "item_number", "revision", "started", "finished"].map(function (column) {
                        return { column: column, value: row[column] };
                    });
                })
                .enter()
                .append("td")
                .text((x) => x.value);
        }
        else if (returned_object.status == "not_ok") {

            // remove previous data
            existing_report_table.selectAll("tbody").remove();

            // log the error message
            console.log(returned_object.response);
        }
    });
}

// user selected an inspection report from the existing inspection reports
function inspection_report_selected(data)
{
    // construct the date components
    let s_year = data.start_year.toString().padStart(4, "0");
    let s_month = data.start_month.toString().padStart(2, "0");
    let s_day = data.start_day.toString().padStart(2, "0");
    let f_year = data.finish_year.toString().padStart(4, "0");
    let f_month = data.finish_month.toString().padStart(2, "0");
    let f_day = data.finish_day.toString().padStart(2, "0");

    // populate the inspection report values
    report_id.property("value", data.report_id);
    report_creator.property("value", data.employee);
    report_disposition.property("value", data.disposition);
    report_job_order.property("value", data.job_order_id);
    report_item_number.property("value", data.item_number);
    report_drawing.property("value", data.drawing);
    report_revision.property("value", data.revision);
    report_start_date.property("value", `${s_year}-${s_month}-${s_day}`);
    report_finish_date.property("value", `${f_year}-${f_month}-${f_day}`);
}

// user changed the inspection report's drawing
function drawing_changed()
{
    let route = `/inspection_report_drawing_changed/${report_drawing.property("value")}/`;

    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {
            
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// user changed the inspection report's item number
function item_number_changed()
{
    let route = ``;
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region receiver number group

// user selected the view/edit receiver number associations
function show_receiver_number_modal()
{
    // get the report id
    let report_id_value = report_id.property("value");

    // populate the list
    if (report_id_value != "") {
        populate_receiver_numbers_modal(report_id_value);
    }
}

// populate receiver numbers modal
function populate_receiver_numbers_modal(report_id)
{
    // define the routes
    let route_associated = `/get_receiver_numbers_from_report_id/${report_id}/`;
    let route_all = "/get_all_receiver_numbers/";

    // remove existing items
    existing_report_table.selectAll("div").remove();
    receiver_number_current.selectAll("option").remove();

    // query the flask server
    d3.json(route_associated).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the select control
            receiver_number_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => reciever_number_selected(x.id));
        }
        else {

            // log the error message
            console.log(returned_object.response);
        }
    });

    // query the flask server
    d3.json(route_all).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the dropdown
            receiver_number_current.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.id);
        }
        else {

            // log the error message
            console.log(returned_object.response);
        }
    });
}

// user selected a receiver number from the modal group
function reciever_number_selected(receiver_number_id)
{
    receiver_number_current.property("value", receiver_number_id);
}

// add a new receiver number association to the inspection report
function receiver_number_association_added()
{
    // get the inputs
    let recv = receiver_number_current.property("value");
    let rep_id = report_id.property("value");

    
}

// remove a receiver number association from the inspection report

//#endregion