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


init();

// initialization function
function init()
{
    // populate selectors
    populate_disposition_types();
    populate_job_orders();

    // set initial values
    existing_report_start_date.property("value", "1970-01-01");
    existing_report_stop_date.property("value", "1970-01-01");
    existing_report_use_date.property("checked", false);

    report_start_date.property("value", "1970-01-01");
    report_finish_date.property("value", "1970-01-01");
}

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
                .on("click", (p, data) => inspection_report_selected(data.drawing));

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

// 
function inspection_report_selected(drawing)
{
    
    console.log(drawing);
}


// user selected the view/edit receiver number associations
function show_receiver_number_modal()
{
    // get the report id
    let report_id_value = 1; //report_id.property("value");

    // populate the list
    if (report_id_value != "") {
        console.log(report_id_value);
        get_report_receiver_numbers(report_id_value);
    }
}

// user selected a receiver number from the group
function reciever_number_selected(receiver_number_id)
{
    receiver_number_current.property("value", receiver_number_id);
}


// populate job orders selector
function populate_job_orders()
{
    // define the route
    let route = "/get_job_orders/";

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the select control
            report_job_order.selectAll("option")
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

// populate receiver numbers list group from an inspection report id
function get_report_receiver_numbers(report_id)
{
    // define the route
    let route = `/get_receiver_numbers/${report_id}/`;

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the select control
            receiver_number_group.selectAll("a")
                .data(dataset)
                .enter()
                .append("a")
                .attr("href", "#")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => reciever_number_selected(x.id));
        }
        else {

            // log the error message
            console.log(returned_object.response);
        }
    });
}

// populate disposition type selector
function populate_disposition_types()
{
    // define the route
    let route = "/get_disposition_types/";

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the select control
            report_disposition.selectAll("option")
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