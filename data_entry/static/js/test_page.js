
// sidebar buttons
const sidebar_btn_existing = d3.select("#sidebar_btn_existing");
const sidebar_btn_metadata = d3.select("#sidebar_btn_metadata");
const sidebar_btn_receiver = d3.select("#sidebar_btn_receiver_numbers");
const sidebar_btn_purchase = d3.select("#sidebar_btn_purchase_orders");
const sidebar_btn_charschema = d3.select("#sidebar_btn_charschema");

// existing inspection report controls
const eir_item_number = d3.select("#select_report_item_number");
const eir_drawing = d3.select("#select_report_drawing");
const eir_start_after = d3.select("#select_report_start");
const eir_finish_before = d3.select("#select_report_finish");
const eir_table = d3.select("#select_report_table");

// metadata controls
const meta_report_id = d3.select("#metadata_report_id");
const meta_inspector_id = d3.select("#metadata_inspector_id");
const meta_disposition = d3.select("#metadata_disposition");
const meta_item_number = d3.select("#metadata_item_number");
const meta_drawing = d3.select("#metadata_drawing");
const meta_revision = d3.select("#metadata_revision");
const meta_job_order = d3.select("#metadata_job_order");
const meta_material_type = d3.select("#metadata_material_type");
const meta_supplier = d3.select("#metadata_supplier");
const meta_start_date = d3.select("#metadata_start_date");
const meta_finish_date = d3.select("#metadata_finish_date");
const meta_full_inspect_type = d3.select("#metadata_qc_full_inspect");
const meta_full_inspect_qty = d3.select("#metadata_qc_full_inspect_qty");
const meta_released_type = d3.select("#metadata_released");
const meta_released_qty = d3.select("#metadata_released_qty");
const meta_completed_type = d3.select("#metadata_completed");
const meta_completed_qty = d3.select("#metadata_completed_qty");

init();

// #region page initialization

// initialize the page
function init()
{
    // connect events
    eir_item_number.on("keydown", (x) => {
        console.log(x);
        if (x.keyCode == 13) {
            get_inspection_reports();
        }
    });
    eir_drawing.on("keydown", (x) => {
        if (x.keyCode == 13) {
            get_inspection_reports();
        }
    });
    eir_start_after.on("keydown", (x) => {
        if (x.keyCode == 13) {
            get_inspection_reports();
        }
    });
    eir_finish_before.on("keydown", (x) => {
        if (x.keyCode == 13) {
            get_inspection_reports();
        }
    });

    // populate selectors
    populate_selectors();

    // set initial values
    eir_start_after.property("value", "1970-01-01");
    eir_finish_before.property("value", "2100-01-01");
    meta_start_date.property("value", "1970-01-01");
    meta_finish_date.property("value", "2100-01-01");

    // set the disabled state
    set_disabled_state(true);
}

// set the controls disabled state
function set_disabled_state(is_disabled)
{
    // sidebar buttons
    sidebar_btn_metadata.property("disabled", is_disabled);
    sidebar_btn_receiver.property("disabled", is_disabled);
    sidebar_btn_purchase.property("disabled", is_disabled);
    sidebar_btn_charschema.property("disabled", is_disabled);

    // metadata
    meta_inspector_id.property("disabled", is_disabled);
    meta_disposition.property("disabled", is_disabled);
    meta_item_number.property("disabled", is_disabled);
    meta_drawing.property("disabled", is_disabled);
    meta_revision.property("disabled", is_disabled);
    meta_job_order.property("disabled", is_disabled);
    meta_material_type.property("disabled", is_disabled);
    meta_supplier.property("disabled", is_disabled);
    meta_start_date.property("disabled", is_disabled);
    meta_finish_date.property("disabled", is_disabled);
    meta_full_inspect_type.property("disabled", is_disabled);
    meta_full_inspect_qty.property("disabled", is_disabled);
    meta_released_type.property("disabled", is_disabled);
    meta_released_qty.property("disabled", is_disabled);
    meta_completed_type.property("disabled", is_disabled);
    meta_completed_qty.property("disabled", is_disabled);
}

function populate_selectors()
{
    // inspector id
    d3.json("/get_all_employee_ids/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_inspector_id.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // disposition
    d3.json("/get_all_disposition_types/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_disposition.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // item number
    d3.json("/get_all_item_numbers/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_item_number.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // drawing
    d3.json("/get_all_drawings/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_drawing.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // job order
    d3.json("/get_all_job_order_ids/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_job_order.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // material types
    d3.json("/get_all_material_types/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_material_type.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // supplier
    d3.json("/get_all_suppliers/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_supplier.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // full inspect/released/completed type
    d3.json("/get_all_quantity_types/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selectors
            meta_full_inspect_type.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
            meta_released_type.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
            meta_completed_type.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region sidebar control

// toggle the open/close state for the sidebar buttons
function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "existing") {
        if (document.getElementById("inspection_report_existing_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_existing_sidebar").style.width = close_width;
            document.getElementById("inspection_report_existing").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_existing_sidebar").style.width = open_width;
            document.getElementById("inspection_report_existing").style.marginLeft = open_width;
            get_inspection_reports();
        }
    }
    else if (destination_arg == "metadata") {
        if (document.getElementById("inspection_report_metadata_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_metadata_sidebar").style.width = close_width;
            document.getElementById("inspection_report_metadata").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_metadata_sidebar").style.width = open_width;
            document.getElementById("inspection_report_metadata").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "receiver_numbers") {
        if (document.getElementById("inspection_report_receiver_numbers_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_receiver_numbers_sidebar").style.width = close_width;
            document.getElementById("inspection_report_receiver_numbers").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_receiver_numbers_sidebar").style.width = open_width;
            document.getElementById("inspection_report_receiver_numbers").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "purchase_orders") {
        if (document.getElementById("inspection_report_purchase_orders_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_purchase_orders_sidebar").style.width = close_width;
            document.getElementById("inspection_report_purchase_orders").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_purchase_orders_sidebar").style.width = open_width;
            document.getElementById("inspection_report_purchase_orders").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "characteristic_schema") {
        if (document.getElementById("inspection_report_characteristic_schema_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_characteristic_schema_sidebar").style.width = close_width;
            document.getElementById("inspection_report_characteristic_schema").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_characteristic_schema_sidebar").style.width = open_width;
            document.getElementById("inspection_report_characteristic_schema").style.marginLeft = open_width;
        }
    }
}

//#endregion

// #region existing reports

// get the matching inspection reports
function get_inspection_reports()
{
    // get the parameters
    let item_number = eir_item_number.property("value");
    let drawing = eir_drawing.property("value");
    let start_after = new Date(eir_start_after.property("value") + "T00:00:00");
    let finish_before = new Date(eir_finish_before.property("value") + "T00:00:00");

    // parse the date parameters
    let start_day = start_after.getDate();
    let start_month = start_after.getMonth() + 1;
    let start_year = start_after.getFullYear();
    let finish_day = finish_before.getDate();
    let finish_month = finish_before.getMonth() + 1;
    let finish_year = finish_before.getFullYear();

    // handle empty parameters
    if (item_number == "") {
        item_number = "__null";
    }
    if (drawing == "") {
        drawing = "__null";
    }

    // define the server route
    route = `/get_filtered_inspection_reports/${item_number}/${drawing}/${start_day}/${start_month}/${start_year}/${finish_day}/${finish_month}/${finish_year}/`;

    // run the server request
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // remove the previous data
            eir_table.selectAll("tbody").remove();

            // create the rows
            let rows = eir_table.append("tbody")
                .selectAll("tr")
                .data(dataset)
                .enter()
                .append("tr")
                .on("click", (i, j) => inspection_report_selected(i, j));

            // assign the cell contents
            rows.selectAll("td")
                .data((r) => {
                    return ["drawing", "revision", "item", "day_started", "day_finished"].map((c) => {
                        return { col: c, value: r[c] };
                    });
                })
                .enter()
                .append("td")
                .text((x) => x.value);

            // set the start cell class
            rows.selectAll("td")
                .filter((x) => {
                    if (x.col == "drawing") {
                        return true;
                    }
                })
                .attr("class", "data_table_start_cell");

            // set the end cell class
            rows.selectAll("td")
                .filter((x) => {
                    if (x.col == "day_finished") {
                        return true;
                    }
                })
                .attr("class", "data_table_end_cell");
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// user selected an inspection report from the list
function inspection_report_selected(pointer, data)
{
    // enable the inspection report dependent controls
    set_disabled_state(false);

    // set the metadata values
    meta_report_id.property("value", `Report ID: ${data.report_id}`);
    meta_report_id.property("data-meta", data.report_id);
    meta_inspector_id.property("value", data.employee_id);
    meta_disposition.property("value", data.disposition);
    meta_item_number.property("value", data.item);
    meta_drawing.property("value", data.drawing);
    meta_revision.property("value", data.revision);
    meta_job_order.property("value", data.job_order_id);
    meta_material_type.property("value", data.material_type_id);
    meta_supplier.property("value", data.supplier_id);
    meta_start_date.property("value", data.js_day_started);
    meta_finish_date.property("value", data.js_day_finished);
    meta_full_inspect_type.property("value", data.full_inspect_type);
    meta_full_inspect_qty.property("value", data.full_inspect_qty);
    meta_released_type.property("value", data.released_type);
    meta_released_qty.property("value", data.released_qty);
    meta_completed_type.property("value", data.completed_type);
    meta_completed_qty.property("value", data.completed_qty);
}

// #endregion