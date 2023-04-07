
// sidebar buttons
const sidebar_btn_existing = d3.select("#sidebar_btn_existing");
const sidebar_btn_metadata = d3.select("#sidebar_btn_metadata");
const sidebar_btn_receiver = d3.select("#sidebar_btn_receiver_numbers");
const sidebar_btn_purchase = d3.select("#sidebar_btn_purchase_orders");
const sidebar_btn_charschema = d3.select("#sidebar_btn_charschema");

// characteristic filter
const filter_name = d3.select("#charfilter_name");
const filter_gauge_id = d3.select("#charfilter_gauge_id");
const filter_gauge_type = d3.select("#charfilter_gauge_type");
const filter_isgdt = d3.select("#charfilter_is_gdt");
const filter_spectype = d3.select("#charfilter_specification_type");
const filter_chartype = d3.select("#charfilter_characteristic_type");
const filter_inspector_id = d3.select("#charfilter_inspector");
const filter_display_type = d3.select("#charfilter_display_type");

// characteristic table
const char_table = d3.select("#char_table");

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
const meta_full_inspect_type = d3.select("#metadata_full_inspect_type");
const meta_full_inspect_qty = d3.select("#metadata_full_inspect_qty");
const meta_released_type = d3.select("#metadata_released_type");
const meta_released_qty = d3.select("#metadata_released_qty");
const meta_completed_type = d3.select("#metadata_completed_type");
const meta_completed_qty = d3.select("#metadata_completed_qty");

// receiver number controls
const rn_filter = d3.select("#rn_filter");
const rn_value = d3.select("#rn_value");
const rn_list = d3.select("#rn_list");
const rn_button = d3.select("#rn_button");

// purchase order controls
const po_filter = d3.select("#po_filter");
const po_value = d3.select("#po_value");
const po_list = d3.select("#po_list");
const po_button = d3.select("#po_button");

init();

// #region page initialization

// initialize the page
function init()
{
    // characteristic filter
    filter_name.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_gauge_id.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_gauge_type.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_isgdt.on("change", retrieve_characteristics);
    filter_spectype.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_chartype.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_inspector_id.on("keydown", (x) => {
        if (x.keyCode == 13) {
            retrieve_characteristics();
        }
    });
    filter_display_type.on("change", change_table_columns);

    // existing reports events
    eir_item_number.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_existing_inspection_reports();
        }
    });
    eir_drawing.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_existing_inspection_reports();
        }
    });
    eir_start_after.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_existing_inspection_reports();
        }
    });
    eir_finish_before.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_existing_inspection_reports();
        }
    });

    // metadata events
    meta_item_number.on("change", item_number_changed);
    meta_drawing.on("change", drawing_changed);

    // receiver number events
    rn_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            populate_receiver_numbers();
        }
    });
    rn_button.on("click", assign_receiver_number_association);

    // purchase order events
    po_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            populate_purchase_orders();
        }
    });
    po_button.on("click", assign_purchase_order_association);

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

    // receiver numbers
    d3.json("/get_all_receiver_numbers/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            rn_value.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .text((x) => x.item);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // purchase orders
    d3.json("/get_all_purchase_orders/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            po_value.selectAll("option")
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

// #region characteristic filter

function retrieve_characteristics()
{
    // get the id values
    let report_id = meta_report_id.property("data-meta");

    // get the filter values
    let name = filter_name.property("value");
    let gauge_id = filter_gauge_id.property("value");
    let gauge_type = filter_gauge_type.property("value");
    let spec_type = filter_spectype.property("value");
    let char_type = filter_chartype.property("value");
    let inspector_id = filter_inspector_id.property("value");
    let is_gdt = filter_isgdt.property("value");

    // convert null values
    if (name == "") {
        name = "__null";
    }
    if (gauge_id == "") {
        gauge_id = "__null";
    }
    if (gauge_type == "") {
        gauge_type = "__null";
    }
    if (spec_type == "") {
        spec_type = "__null";
    }
    if (char_type == "") {
        char_type = "__null";
    }
    if (inspector_id == "") {
        inspector_id = 0;
    }

    if (report_id >= 0) {

        // build the route
        let route = `/get_inspection_report_filtered_characteristics/${report_id}/${name}/${gauge_id}/${gauge_type}/${spec_type}/${char_type}/${inspector_id}/${is_gdt}/`;

        // query the flask server
        d3.json(route).then((returned_object) => {
            if (returned_object.status == "ok") {
                
                // extract the requested data
                let dataset = returned_object.response;

                console.log(dataset);
            }
            else if (returned_object.status == "ok_alt") {
                alert(returned_object.response);
            }
            else {
                console.log(returned_object.response);
            }
        });
    }
}

function change_table_columns()
{
    console.log("columns changed");
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
            update_existing_inspection_reports();
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
function update_existing_inspection_reports()
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
                .on("click", (event, data) => inspection_report_selected(data));

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
function inspection_report_selected(data)
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

    // populate the receiver numbers
    populate_receiver_numbers(data.report_id);
    populate_purchase_orders(data.report_id);
}

// #endregion

// #region metadata

// item number selection has changed
function item_number_changed()
{
    // get the current item number
    let item_number = meta_item_number.property("value");

    // build the route
    let route = `/get_drawing_from_item_number/${item_number}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // set the drawing
            meta_drawing.property("value", dataset);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// drawing selection has changed
function drawing_changed()
{
    // get the current drawing
    let drawing = meta_drawing.property("value");

    // build the route
    let route = `/get_item_number_from_drawing/${drawing}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // set the item number
            meta_item_number.property("value", dataset);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region receiver numbers

function populate_receiver_numbers(report_id = -1)
{
    // get the input parameters
    let filter = rn_filter.property("value");
    if (report_id == -1) {
        report_id = meta_report_id.property("data-meta");
    }

    // handle null value
    if (filter == "") {
        filter = "__null";
    }

    // build the route
    let route = `/get_filtered_receiver_numbers/${report_id}/${filter}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(rn_list, dataset, "receiver_number");
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function assign_receiver_number_association()
{
    // get the input parameters
    let report_id = meta_report_id.property("data-meta");
    let receiver_number = rn_value.property("value");

    // build the route
    let route = `/assign_receiver_number_association/${report_id}/${receiver_number}/`;

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(rn_list, dataset, "receiver_number");
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function remove_receiver_number_association(pointer, data)
{
    // get the input arguments
    let receiver_number = data.item;
    let report_id = data.report_id;

    // build the route
    let route = `/remove_receiver_number_association/${report_id}/${receiver_number}/`;

    // query the database
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {
            
            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(rn_list, dataset, "receiver_number");
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region purchase orders

function populate_purchase_orders(report_id = -1)
{
    // get the input parameters
    let filter = po_filter.property("value");
    if (report_id == -1) {
        report_id = meta_report_id.property("data-meta");
    }

    // handle null value
    if (filter == "") {
        filter = "__null";
    }

    // build the route
    let route = `/get_filtered_purchase_orders/${report_id}/${filter}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(po_list, dataset, "purchase_order");
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function assign_purchase_order_association()
{
    // get the input parameters
    let report_id = meta_report_id.property("data-meta");
    let purchase_order = po_value.property("value");

    // build the route
    let route = `/assign_purchase_order_association/${report_id}/${purchase_order}/`;

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(po_list, dataset, "purchase_order");
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function remove_purchase_order_association(pointer, data)
{
    // get the input arguments
    let purchase_order = data.item;
    let report_id = data.report_id;

    // build the route
    let route = `/remove_purchase_order_association/${report_id}/${purchase_order}/`;

    // query the database
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_association_list(po_list, dataset, "purchase_order");
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region characteristic schema

// #endregion

// #region general methods

// populate an association list
function populate_association_list(list_container, dataset, direction)
{
    // remove the previous data
    list_container.selectAll("li").remove();

    // populate the list
    if (dataset.length > 0) {
        let list_items = list_container.selectAll("li")
            .data(dataset)
            .enter()
            .append("li")
            .append("div")
            .attr("class", "grid_container_item")
            .style("--grid-template-columns", "3fr 1fr");

        list_items.append("label")
            .style("--grid-column", "1")
            .style("--grid-row", "1")
            .text((x) => x.item);
        switch (direction) {
            case "receiver_number":
                list_items.append("button")
                    .style("--grid-column", "2")
                    .style("--grid-row", "1")
                    .attr("type", "button")
                    .text("Delete")
                    .on("click", (pointer, data) => { remove_receiver_number_association(pointer, data); });
                break;
            case "purchase_order":
                list_items.append("button")
                    .style("--grid-column", "2")
                    .style("--grid-row", "1")
                    .attr("type", "button")
                    .text("Delete")
                    .on("click", (pointer, data) => { remove_purchase_order_association(pointer, data); });
                break;
        }
    }
}

// #endregion
