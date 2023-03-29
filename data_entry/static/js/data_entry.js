// control definitions
const existing_report_button = d3.select("#existing_report_button");
const existing_report_table = d3.select("#existing_reports_table");
const existing_report_filter_type = d3.select("#existing_report_filter_type");
const existing_report_filter_term = d3.select("#existing_report_filter_term");
const existing_report_filter_apply = d3.select("#existing_report_filter_apply");
const existing_report_start_date = d3.select("#existing_report_start_date");
const existing_report_stop_date = d3.select("#existing_report_stop_date");
const existing_report_use_date = d3.select("#existing_report_use_date");

const report_id = d3.select("#report_id");
const report_creator = d3.select("#report_creator");
const report_disposition = d3.select("#report_disposition");
const report_item_number = d3.select("#report_item_number");
const report_drawing = d3.select("#report_drawing");
const report_revision = d3.select("#report_revision");
const report_job_order = d3.select("#report_job_order");
const report_start_date = d3.select("#report_start_date");
const report_finish_date = d3.select("#report_finish_date");
const report_char_filter = d3.select("#report_characteristics_filter");
const report_char_scope = d3.select("#report_characteristics_scope");
const report_char_table = d3.select("#report_characteristics");

const receiver_number_view_edit = d3.select("#view_edit_receiver_numbers");
const receiver_number_current = d3.select("#current_receiver_number");
const receiver_number_add = d3.select("#add_receiver_number");
const receiver_number_remove = d3.select("#remove_receiver_number");
const receiver_number_group = d3.select("#receiver_number_group");

const purchase_order_view_edit = d3.select("#view_edit_purchase_orders");
const purchase_order_current = d3.select("#current_purchase_order");
const purchase_order_add = d3.select("#add_purchase_order");
const purchase_order_remove = d3.select("#remove_purchase_order");
const purchase_order_group = d3.select("#purchase_order_group")

const characteristic_schema_view_edit = d3.select("#view_edit_characteristic_schema");

// define color codes
const pass_color = "rgba(0, 200, 0, 1)";
const fail_color = "rgba(200, 0, 0, 1)";
const null_color = "rgba(0, 0, 200, 1)";

// add events
existing_report_button.on("click", update_existing_reports_panel);
existing_report_filter_apply.on("click", update_existing_reports_panel);

receiver_number_view_edit.on("click", show_receiver_number_modal);
receiver_number_add.on("click", receiver_number_association_added);
receiver_number_remove.on("click", receiver_number_association_removed);

purchase_order_view_edit.on("click", show_purchase_order_modal);
purchase_order_add.on("click", purchase_order_association_added);
purchase_order_remove.on("click", purchase_order_association_removed);

report_drawing.on("change", drawing_changed);
report_item_number.on("change", item_number_changed);
report_char_filter.on("keypress", function(e) { if (e.keyCode == 13) { char_table_update(report_char_scope.property("value")); } })
report_char_scope.on("change", function() { char_table_update(report_char_scope.property("value")); });

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

    // set initial readonly states
    toggle_readonly(true);
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

function toggle_readonly(readonly_state)
{
    receiver_number_view_edit.property("disabled", readonly_state);
    purchase_order_view_edit.property("disabled", readonly_state);
    characteristic_schema_view_edit.property("disabled", readonly_state);
    report_id.property("disabled", readonly_state);
    report_creator.property("disabled", readonly_state);
    report_disposition.property("disabled", readonly_state);
    report_item_number.property("disabled", readonly_state);
    report_drawing.property("disabled", readonly_state);
    report_revision.property("disabled", readonly_state);
    report_job_order.property("disabled", readonly_state);
    report_start_date.property("disabled", readonly_state);
    report_finish_date.property("disabled", readonly_state);
    report_char_filter.property("disabled", readonly_state);
    report_char_scope.property("disabled", readonly_state);
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

    // make report editable
    toggle_readonly(false);

    // update the characteristic table
    char_table_update(report_char_scope.property("value"));
}

// user changed the inspection report's drawing
function drawing_changed()
{
    let route = `/inspection_report_drawing_changed/${report_drawing.property("value")}/`;
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_item_number.property("value", returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// user changed the inspection report's item number
function item_number_changed()
{
    let route = `/inspection_report_item_number_changed/${report_item_number.property("value")}/`;
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {
            report_drawing.property("value", returned_object.response);
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

            // populate the list control
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

    // build the server route
    let route = `/add_receiver_number_association/${rep_id}/${recv}/`;

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // clear the old list
            receiver_number_group.selectAll("div").remove();
            
            // extract the requested data
            let dataset = returned_object.response;
            
            // populate the list control
            receiver_number_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => reciever_number_selected(x.id));
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// remove a receiver number association from the inspection report
function receiver_number_association_removed()
{
    // get the inputs
    let recv = receiver_number_current.property("value");
    let rep_id = report_id.property("value");

    // build the server route
    let route = `/remove_receiver_number_association/${rep_id}/${recv}/`;

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {
    
            // clear the old list
            receiver_number_group.selectAll("div").remove();

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list control
            receiver_number_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => reciever_number_selected(x.id));
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region purchase order group

// user selected the view/edit purchase order associations
function show_purchase_order_modal()
{
    // get the report id
    let report_id_value = report_id.property("value");

    // populate the list
    if (report_id_value != "") {
        populate_purchase_orders_modal(report_id_value);
    }
}

// populate purchase orders modal
function populate_purchase_orders_modal(report_id)
{
    // define the routes
    let route_associated = `/get_purchase_orders_from_report_id/${report_id}/`;
    let route_all = "/get_all_purchase_orders/";

    // remove existing items
    existing_report_table.selectAll("div").remove();
    receiver_number_current.selectAll("option").remove();

    // query the flask server
    d3.json(route_associated).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list control
            purchase_order_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => purchase_order_selected(x.id));
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
            purchase_order_current.selectAll("option")
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

// user selected a purchase order from the modal group
function purchase_order_selected(purchase_order_id)
{
    purchase_order_current.property("value", purchase_order_id);
}

// add a new purchase order association to the inspection report
function purchase_order_association_added()
{
    // get the inputs
    let recv = purchase_order_current.property("value");
    let rep_id = report_id.property("value");

    // build the server route
    let route = `/add_purchase_order_association/${rep_id}/${recv}/`;

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // clear the old list
            purchase_order_group.selectAll("div").remove();
            
            // extract the requested data
            let dataset = returned_object.response;
            
            // populate the list control
            purchase_order_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => purchase_order_selected(x.id));
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// remove a purchase order association from the inspection report
function purchase_order_association_removed()
{
    // get the inputs
    let recv = purchase_order_current.property("value");
    let rep_id = report_id.property("value");

    // build the server route
    let route = `/remove_purchase_order_association/${rep_id}/${recv}/`;

    // query the flask server
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {
    
            // clear the old list
            purchase_order_group.selectAll("div").remove();

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list control
            purchase_order_group.selectAll("div")
                .data(dataset)
                .enter()
                .append("div")
                .attr("class", "list-group-item list-group-item-action")
                .text((x) => x.id)
                .on("click", (p, x) => purchase_order_selected(x.id));
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region characteristic table

// update the characteristic table
function char_table_update(scope)
{
    // define the columns
    let column_names = [];
    switch (scope) {
        case "0":
            column_names = [
                { key: "name", value: "Name", editable: false },
                { key: "nominal", value: "Nominal", editable: false },
                { key: "usl", value: "USL", editable: false },
                { key: "lsl", value: "LSL", editable: false },
                { key: "measured", value: "Measured", editable: true },
                { key: "precision", value: "Precision", editable: true },
                { key: "employee_id", value: "Employee ID", editable: false }
            ];
            break;
        case "1":
            column_names = [
                { key: "name", value: "Name", editable: false },
                { key: "specification_type", value: "Specification Type", editable: false },
                { key: "characteristic_type", value: "Characteristic Type", editable: false },
                { key: "is_gdt", value: "Is GD&T", editable: false },
                { key: "gauge_id", value: "Gauge ID", editable: false },
                { key: "gauge_type", value: "Gauge Type", editable: false }
            ];
            break;
        case "2":
            column_names = [
                { key: "name", value: "Name", editable: false },
                { key: "nominal", value: "Nominal", editable: false },
                { key: "usl", value: "USL", editable: false },
                { key: "lsl", value: "LSL", editable: false },
                { key: "measured", value: "Measured", editable: true },
                { key: "precision", value: "Precision", editable: true },
                { key: "employee_id", value: "Employee ID", editable: false },
                { key: "specification_type", value: "Specification Type", editable: false },
                { key: "characteristic_type", value: "Characteristic Type", editable: false },
                { key: "is_gdt", value: "Is GD&T", editable: false },
                { key: "gauge_id", value: "Gauge ID", editable: false },
                { key: "gauge_type", value: "Gauge Type", editable: false }
            ];
            break;
    }

    // remove previous data
    report_char_table.selectAll("thead").remove();

    // add the specified columns
    report_char_table.append("thead").selectAll("tr")
        .data(column_names)
        .enter()
        .append("th")
        .text((x) => x.value)
        .attr("id", (x) => x.key);

    // get the identifiers
    let rep_id = report_id.property("value");
    let rep_item = report_item_number.property("value");
    let rep_drawing = report_drawing.property("value");
    let rep_revision = report_revision.property("value");
    let char_filter = report_char_filter.property("value");

    // make sure the character filter is not null
    if (char_filter == "") {
        char_filter = "__none";
    }

    // build the route
    let route = `/get_inspection_report_characteristics/${rep_id}/${rep_item}/${rep_drawing}/${rep_revision}/${char_filter}/`;

    // query the database
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response.cell_data;
            let employee_lst = returned_object.response.employee_ids;

            // clear the old data
            report_char_table.selectAll("tbody").remove();

            // create the table rows
            let rows = report_char_table.append("tbody").selectAll("tr")
                .data(dataset)
                .enter()
                .append("tr")
                .style("color", (x) => row_conditioning(x));

            // assign the cell contents
            let cells = rows.selectAll("td")
                .data(function (row) {
                    return column_names.map(function (column) {
                        return { 
                            column: column,
                            value: {
                                cell: row[column.key],
                                key: column.key,
                                editable: column.editable,
                                precision: row["precision"]
                            }
                        }
                    });
                })
                .enter()
                .append("td")
                .text((x) => {
                    if (x.value.key == "nominal" || x.value.key == "usl" || x.value.key == "lsl" || x.value.key == "measured") {
                        if (x.value.cell == null) {
                            return null;
                        }
                        else {
                            return x.value.cell.toFixed(x.value.precision);
                        }
                    }
                    else if (x.value.key != "employee_id") {
                        return x.value.cell;
                    }
                })
                .attr("contenteditable", (x) => x.value.editable);
            
            // add value changed events
            cells.filter(measured_column_filter)
                .on("keypress", (e) => {
                    if (e.keyCode == 13) {
                        e.preventDefault();
                    }
                })
            cells.filter(precision_column_filter)
                .on("keypress", (e) => {
                    if (e.keyCode == 13) {
                        e.preventDefault();
                    }
                })

            // employee id selectors
            cells.filter(employee_id_column_filter)
                .insert("select")
                .attr("class", "form-select")
                .selectAll("option")
                .data(employee_lst)
                .enter()
                .append("option")
                .attr("value", (x) => x)
                .text((x) => x);
            cells.filter(employee_id_column_filter)
                .selectAll("select")
                .property("value", (x) => x.value.cell);
        }
        else {
            console.log(returned_object.response);
        }
    });

    read_char_table();
}

let employee_id_column_filter = function (x) {
    if (x.column.key == "employee_id") {
        return true;
    }
    else {
        return false;
    }
}

let measured_column_filter = function (x) {
    if (x.column.key == "measured") {
        return true;
    }
    else {
        return false;
    }
}

let precision_column_filter = function (x) {
    if (x.column.key == "precision") {
        return true;
    }
    else {
        return false;
    }
}

function row_conditioning(x)
{
    if (x.state == "null") {
        return null_color;
    }
    else if (x.state == "pass") {
        return pass_color;
    }
    else if (x.state == "fail") {
        return fail_color;
    }
}

function read_char_table()
{
    let row_count = report_char_table.rows;

    console.log(row_count);
}

// #endregion