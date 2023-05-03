
// sidebar buttons
const sidebar_btn_charschema = d3.select("#sidebar_btn_charschema");
const sidebar_btn_existing = d3.select("#sidebar_btn_existing");
const sidebar_btn_metadata = d3.select("#sidebar_btn_metadata");
const sidebar_btn_receiver = d3.select("#sidebar_btn_receiver_numbers");
const sidebar_btn_purchase = d3.select("#sidebar_btn_purchase_orders");
const sidebar_btn_lots = d3.select("#sidebar_btn_lot_numbers");

// characteristics
const char_table = d3.select("#char_table");

// characteristic schema
const schema_commit = d3.select("#commit_schema_btn");
const schema_list = d3.select("#schema_list");
const schema_filter = d3.select("#cs_filter");
const schema_new = d3.select("#new_char_schema");
const schema_add = d3.select("#add_schema_row_btn");
const schema_remove = d3.select("#remove_schema_row_btn");
const schema_table = d3.select("#characteristic_schema_table");

// report controls
const ctl_new_report = d3.select("#new_report_btn");
const ctl_save_report = d3.select("#save_report_btn");
const ctl_item_number = d3.select("#select_new_item");
const ctl_drawing = d3.select("#select_new_drawing");
const ctl_revision = d3.select("#input_new_revision");
const ctl_display_type = d3.select("#select_display_type");

// existing inspection report controls
const eir_item_number = d3.select("#select_report_item_number");
const eir_drawing = d3.select("#select_report_drawing");
const eir_start_after = d3.select("#select_report_start");
const eir_finish_before = d3.select("#select_report_finish");
const eir_table = d3.select("#select_report_table");

// characteristic filter
const filter_name = d3.select("#charfilter_name");
const filter_gauge_id = d3.select("#charfilter_gauge_id");
const filter_gauge_type = d3.select("#charfilter_gauge_type");
const filter_spectype = d3.select("#charfilter_specification_type");
const filter_chartype = d3.select("#charfilter_characteristic_type");
const filter_inspector_id = d3.select("#charfilter_inspector");

// metadata controls
const meta_save = d3.select("#save_metadata");
const meta_details = d3.select("#metadata_part_details");
const meta_report_id = d3.select("#metadata_report_id");
const meta_part_id = d3.select("#metadata_part_id");
const meta_track_inspector_id = d3.select("#metadata_inspector_track");
const meta_inspector_id = d3.select("#metadata_inspector_id");
const meta_disposition = d3.select("#metadata_disposition");
const meta_track_job_order = d3.select("#metadata_joborder_track");
const meta_job_order = d3.select("#metadata_job_order");
const meta_material_type = d3.select("#metadata_material_type");
const meta_track_supplier = d3.select("#metadata_supplier_track");
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

// lot number controls
const ln_filter = d3.select("#ln_filter");
const ln_value = d3.select("#ln_value");
const ln_list = d3.select("#ln_list");
const ln_button = d3.select("#ln_button");

// inspection report identification
const inspection_report_ident = d3.select("#current_report_ident");













// characteristic table columns
const char_table_columns = [
    { key: "name", data_entry: true, metadata: true, all: true, display: "Name", ctl_type: "label" },
    { key: "nominal", data_entry: true, metadata: false, all: true, display: "Nominal", ctl_type: "label" },
    { key: "usl", data_entry: true, metadata: false, all: true, display: "USL", ctl_type: "label" },
    { key: "lsl", data_entry: true, metadata: false, all: true, display: "LSL", ctl_type: "label" },
    { key: "measured", data_entry: true, metadata: false, all: true, display: "Measured", ctl_type: "input" },
    { key: "employee_id", data_entry: true, metadata: false, all: true, display: "Inspector", ctl_type: "dropdown" },
    { key: "gauge_id", data_entry: true, metadata: false, all: true, display: "Gauge ID", ctl_type: "dropdown" },
    { key: "precision", data_entry: false, metadata: true, all: true, display: "Precision", ctl_type: "label" },
    { key: "spec_type_id", data_entry: false, metadata: true, all: true, display: "Specification Type", ctl_type: "label" },
    { key: "char_type_id", data_entry: false, metadata: true, all: true, display: "Characteristic Type", ctl_type: "label" },
    { key: "gauge_type_id", data_entry: false, metadata: true, all: true, display: "Gauge Type", ctl_type: "label" },
];

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

    // report controls
    ctl_new_report.on("click", create_new_inspection_report);
    ctl_save_report.on("click", submit_characteristics);
    ctl_display_type.on("change", retrieve_characteristics);
    ctl_item_number.on("change", report_item_number_changed);
    ctl_drawing.on("change", report_drawing_changed);

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

    // metadata
    meta_save.on("click", save_metadata);

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

    // characteristic schema
    schema_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            populate_char_schema_list();
        }
    })
    schema_new.on("click", new_schema);
    schema_commit.on("click", commit_schema);
    schema_add.on("click", (x) => { add_schema_row([{ name: "DIM x", nominal: "1.000", usl: "1.005", lsl: "0.995", precision: 3, spec_type: "two_tailed", char_type: "diameter", gauge_type: "caliper" }])});
    schema_remove.on("click", remove_schema_row);

    // populate selectors
    populate_selectors();

    // set initial values
    eir_start_after.property("value", "1970-01-01");
    eir_finish_before.property("value", "2100-01-01");
    meta_start_date.property("value", "1970-01-01");
    meta_finish_date.property("value", "2100-01-01");

    // populate the list of characteristic schemas
    populate_char_schema_list();

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
    sidebar_btn_lots.property("disabled", is_disabled);

    // metadata
    meta_inspector_id.property("disabled", is_disabled);
    meta_disposition.property("disabled", is_disabled);
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

    // misc
    schema_commit.property("disabled", is_disabled);
}

// populate the generic selectors
function populate_selectors()
{
    // inspector id
    d3.json("/get_all_employees/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_inspector_id.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // disposition
    d3.json("/get_all_disposition_types/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_disposition.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // item number & drawing
    d3.json("/get_all_parts/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selectors
            ctl_item_number.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.item);
            ctl_drawing.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.drawing);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // job order
    d3.json("/get_all_job_orders/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_job_order.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // material types
    d3.json("/get_all_material_types/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_material_type.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // supplier
    d3.json("/get_all_suppliers/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            meta_supplier.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.item);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // receiver numbers
    d3.json("/get_all_receiver_numbers/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            rn_value.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // purchase orders
    d3.json("/get_all_purchase_orders/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            po_value.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });

    // lot numbers
    d3.json("/get_all_lot_numbers/").then((returned_object) => {
        if (returned_object.status == "ok_func") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the selector
            ln_value.selectAll("option")
                .data(dataset)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (returned_object.status == "ok_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "ok_log") {
            console.log(returned_object.response);
        }
        else if (returned_object.status == "err_alert") {
            alert(returned_object.response);
        }
        else if (returned_object.status == "err_log") {
            console.log(returned_object.response);
        }
    });
}

// #endregion

// #region characteristics

function get_filtered_characteristics()
{

}

function submit_current_characteristics()
{
    
}

// #endregion characteristics


// #region characteristic schemas

// #endregion characteristic schemas






// #region characteristic filter

// get the requested characteristics
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
        let route = `/get_inspection_report_filtered_characteristics/${report_id}/${name}/${gauge_id}/${gauge_type}/${spec_type}/${char_type}/${inspector_id}/`;

        // query the flask server
        d3.json(route).then((returned_object) => {
            if (returned_object.status == "ok") {

                // extract the requested data
                let dataset = returned_object.response.data_array;
                let gauge_ids = returned_object.response.gauge_ids;
                let inspector_ids = returned_object.response.inspectors;

                // get the column display schema
                let display_type = ctl_display_type.property("value");
                let key = "";
                switch (display_type) {
                    case "0":
                        key = "data_entry";
                        break;
                    case "1":
                        key = "metadata";
                        break;
                    case "2":
                        key = "all";
                        break;
                }

                // remove previous columns
                char_table.selectAll("thead").remove();

                // add the columns
                char_table.append("thead")
                    .selectAll("tr")
                    .data(char_table_columns)
                    .enter()
                    .append("th")
                    .text((x) => x.display)
                    .attr("scope", "col")
                    .style("display", (x) => {
                        if (!x[key]) {
                            return "none";
                        }
                    });

                // clear the old data
                char_table.selectAll("tbody").remove();

                // create the rows
                let rows = char_table.append("tbody")
                    .selectAll("tr")
                    .data(dataset)
                    .enter()
                    .append("tr");

                // assign cell contents
                let cells = rows.selectAll("td")
                    .data((r) => {
                        return char_table_columns.map((c) => {
                            return {
                                column: c,
                                row: {
                                    value: r[c.key],
                                    index: r.id,
                                    key: c.key,
                                    state: r.state,
                                    precision: r.precision,
                                    ctl_type: c.ctl_type
                                }
                            };
                        });
                    })
                    .enter()
                    .append("td")
                    .style("display", (x) => {
                        if (!x.column[key]) {
                            return "none";
                        }
                    });

                // assign label values to cells
                cells.filter((x) => {
                        if (x.row.ctl_type == "label") {
                            return true;
                        }
                    })
                    .insert("input")
                    .attr("class", "table_label_light")
                    .attr("readonly", true)
                    .attr("value", (x) => {
                        switch (x.column.key) {
                            case "nominal" || "usl" || "lsl":
                                return x.row.value.toFixed(x.row.precision);
                            default:
                                return x.row.value;
                        }
                    });

                // assign input controls to cells
                cells.filter((x) => {
                        if (x.row.ctl_type == "input") {
                            return true;
                        }
                    })
                    .insert("input")
                    .attr("class", "table_input_light")
                    .attr("value", (x) => x.row.value)
                    .attr("name", (x) => `${x.row.index}-${x.column.key}`);

                // gauge id dropdowns
                cells.filter((x) => {
                        if (x.row.ctl_type == "dropdown" && x.column.key == "gauge_id") {
                            return true;
                        }
                    })
                    .insert("select")
                    .attr("class", "table_select_light")
                    .selectAll("option")
                    .data(gauge_ids)
                    .enter()
                    .append("option")
                    .attr("value", (x) => x.item)
                    .text((x) => x.item);
                cells.filter((x) => {
                        if (x.row.ctl_type == "dropdown" && x.column.key == "gauge_id") {
                            return true;
                        }
                    })
                    .selectAll("select")
                    .property("value", (x) => x.row.value)
                    .attr("name", (x) => `${x.row.index}-${x.column.key}`);

                // inspector dropdowns
                cells.filter((x) => {
                        if (x.row.ctl_type == "dropdown" && x.column.key == "employee_id") {
                            return true;
                        }
                    })
                    .insert("select")
                    .attr("class", "table_select_light")
                    .selectAll("option")
                    .data(inspector_ids)
                    .enter()
                    .append("option")
                    .attr("value", (x) => x.item)
                    .text((x) => x.item);
                cells.filter((x) => {
                        if (x.row.ctl_type == "dropdown" && x.column.key == "employee_id") {
                            return true;
                        }
                    })
                    .selectAll("select")
                    .property("value", (x) => x.row.value)
                    .attr("name", (x) => `${x.row.index}-${x.column.key}`);

                // set the start cell class
                rows.selectAll("td")
                    .filter((x) => {
                        if (x.column.key == "name") {
                            return true;
                        }
                    })
                    .attr("class", "data_table_start_cell")
                    .selectAll("input")
                    .style("border-radius", "6px 0px 0px 6px");

                // set the end cell class
                rows.selectAll("td")
                    .filter((x) => {
                        let index = char_table_columns.slice().filter((c) => {
                            return c[key];
                        }).reverse()[0].key;
                        if (x.column.key == index) {
                            return true;
                        }
                    })
                    .attr("class", "data_table_end_cell")
                    .selectAll("*")
                    .style("border-radius", "0px 6px 6px 0px");
            }
            else if (returned_object.status == "ok_alt") {
                char_table.selectAll("tbody").remove();
                console.log(returned_object.response);
            }
            else {
                console.log(returned_object.response);
            }
        });
    }
}

// submit new values to be written
function submit_characteristics()
{
    let report_id = meta_report_id.property("data-meta");
    let my_form = document.querySelector("#characteristics_form_id");
    let form_data = new FormData(my_form);

    // handle null report id
    if (report_id == "") {
        report_id = -1;
    }

    if (char_table.select("tbody").selectAll("tr").data().length > 0) {
        fetch(`/commit_characteristic_data/${report_id}/`, {
            method: "POST",
            body: form_data
        }).then((response) => {
            if (response.ok) {
                return response.json();
            }
            else {
                throw new Error("Server response wasn't cool");
            }
        }).then((json) => {
            if (json.status == "ok") {
                alert(`Records Affected: ${json.response.rows_affected}`);
            }
            else if (json.status == "ok_alt") {
                alert(json.response);
            }
            else {
                alert(json.response);
            }
        });
    }
    else {
        alert("No data to be sent")
    }
}

// #endregion

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
                .insert("input")
                .attr("class", "table_input_dark")
                .style("cursor", "pointer")
                .attr("readonly", true)
                .attr("value", (x) => x.value);

            // set the start cell class
            rows.selectAll("td")
                .filter((x) => {
                    if (x.col == "drawing") {
                        return true;
                    }
                })
                .attr("class", "data_table_start_cell")
                .selectAll("input")
                .style("border-radius", "6px 0px 0px 6px");

            // set the end cell class
            rows.selectAll("td")
                .filter((x) => {
                    if (x.col == "day_finished") {
                        return true;
                    }
                })
                .attr("class", "data_table_end_cell")
                .selectAll("input")
                .style("border-radius", "0px 6px 6px 0px");
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
    meta_report_id.text(data.report_id);
    meta_part_id.text(data.part_id);
    meta_details.text(`${data.item} // ${data.drawing} // ${data.revision}`)
    meta_report_id.property("data-meta", data.report_id);
    meta_part_id.property("data-meta", data.part_id);
    meta_inspector_id.property("value", data.employee_id);
    meta_disposition.property("value", data.disposition);
    meta_details.property("data-item", data.item);
    meta_details.property("data-drawing", data.drawing);
    meta_details.property("data-revision", data.revision);
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

    // update the current report identification label
    inspection_report_ident.text(`Current Report: ${data.report_id} // ${data.item} // ${data.drawing} // ${data.revision}`)

    // populate the characteristic table with the current settings
    retrieve_characteristics();
}

// #endregion

// #region metadata

function save_metadata()
{
    if (!confirm("This will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the identifications
    let part_id = meta_part_id.property("data-meta");
    let report_id = meta_report_id.property("data-meta");

    // get the values that can be null
    let track_inspector = meta_track_inspector_id.property("value");
    let track_job_order = meta_track_job_order.property("value");
    let track_supplier = meta_track_supplier.property("value");
    let inspector_id = meta_inspector_id.property("value");
    let job_order = meta_job_order.property("value");
    let supplier = meta_supplier.property("value");
    if (track_inspector == "0") {
        inspector_id = null;
    }
    if (track_job_order == "0") {
        job_order = null;
    }
    if (track_supplier == "0") {
        supplier = null;
    }

    // get the not null values
    let disposition = meta_disposition.property("value");
    let material_type = meta_material_type.property("value");
    let start_date = new Date(meta_start_date.property("value") + "T00:00:00");
    let finish_date = new Date(meta_finish_date.property("value") + "T00:00:00");
    let full_inspect_type = meta_full_inspect_type.property("value");
    let full_inspect_qty = meta_full_inspect_qty.property("value");
    let released_type = meta_released_type.property("value");
    let released_qty = meta_released_qty.property("value");
    let completed_type = meta_completed_type.property("value");
    let completed_qty = meta_completed_qty.property("value");

    // parse the date parameters
    let start_date_py = null;
    if (!isNaN(start_date)) {
        start_date_py = `${String(start_date.getFullYear()).padStart(4, "0")}/${String(start_date.getMonth() + 1).padStart(2, "0")}/${String(start_date.getDate()).padStart(2, "0")}`;
    }
    let finish_date_py = null;
    if (!isNaN(finish_date)) {
        finish_date_py = `${String(finish_date.getFullYear()).padStart(2, "0")}/${String(finish_date.getMonth() + 1).padStart(2, "0")}/${String(finish_date.getDate()).padStart(2, "0")}`;
    }

    // build the form data object
    let data = {
        ident: {
            part_id: part_id,
            report_id: report_id
        },
        info: {
            employee_id: inspector_id,
            job_order_id: job_order,
            supplier_id: supplier,
            disposition: disposition,
            material_type_id: material_type,
            day_started: start_date_py,
            day_finished: finish_date_py,
            full_inspect_qty_type: full_inspect_type,
            full_inspect_qty: full_inspect_qty,
            released_qty_type: released_type,
            released_qty: released_qty,
            completed_qty_type: completed_type,
            completed_qty: completed_qty
        }
    }

    // set the POST request
    fetch("/save_inspection_report_metadata/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then((response) => {
        if (response.ok) {
            return response.json();
        }
        else {
            throw new Error("Server response wasn't cool");
        }
    }).then((json) => {
        if (json.status == "ok") {
            alert(json.response);
        }
        else if (json.status == "ok_alt") {
            alert(json.response);
        }
        else {
            console.log(json.response);
        }
    })
}

// #endregion

// #region receiver numbers

// populate the receiver number list
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
        else if (returned_object.status == "ok_alt") {
            console.log(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// assign a new receiver number association
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

// remove the selected receiver number association
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

// populate the purchase orders list
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
        else if (returned_object.status == "ok_alt") {
            console.log(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// assign a new purchase order association
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

// remove the selected purchase order association
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

// #region characteristic schemas

// populate the characteristic schema list
function populate_char_schema_list()
{
    // get the input parameters
    let filter = schema_filter.property("value");
    
    // handle null value
    if (filter == "") {
        filter = "__null";
    }

    // build the route
    let route = `/get_filtered_char_schemas/${filter}/`;

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // populate the list
            populate_item_list(schema_list, dataset);
        }
        else if (returned_object.status == "ok_alt") {
            console.log(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

// create a new characteristic schema
function new_schema()
{
    let dataset = []

    // get existing details
    let item = meta_details.property("data-item");
    let drawing = meta_details.property("data-drawing");
    let revision = meta_details.property("data-revision");

    // get the current data
    let current_data = schema_list.selectAll("li").data();

    if (item != undefined && drawing != undefined && revision != undefined) {
        let temp = `schema_${item}_${drawing}_${revision.toLowerCase()}`;
        if (!current_data.includes(temp)) {
            dataset = [temp]
        }
        else {
            alert("A characteristic schema for this report already exists.");
            return;
        }
    }
    else {
        dataset = ["schema_itemnumber_drawing_revision"]
    }

    if (current_data.length > 0) {
        dataset = current_data.concat(dataset);
    }

    // repopulate the list
    populate_item_list(schema_list, dataset);

    // save the new file
    save_schema_csv(dataset.slice(-1), false);
}

// load the selected schema file
function load_schema_csv(file_name)
{
    if (confirm("This will reset the schema table. Continue?")) {

        // build the route
        let route = `/load_schema_from_csv/${file_name}/`;

        // query the flask server
        d3.json(route).then((returned_object) => {
            if (returned_object.status == "ok") {

                // extract the requested data
                let dataset = returned_object.response;

                // remove the previous rows
                schema_table.select("tbody").selectAll("tr").remove();

                // repopulate the table
                add_schema_row(dataset);
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

// save the current characteristic schema to the selected name
function save_schema_csv(file_name, request_permission)
{
    if (request_permission) {
        if (!confirm("This will overwrite the existing file if it already exists. Continue?")) {
            return;
        }
    }

    let my_form = document.querySelector("#characteristic_schema_form_id");
    let form_data = new FormData(my_form);
    fetch(`/save_schema_csv/${file_name}/`, {
        method: "POST",
        body: form_data
    }).then((response) => {
        if (response.ok) {
            return response.json();
        }
        else {
            throw new Error("Server response wasn't cool");
        }
    }).then((json) => {
        if (json.status == "ok") {
            alert(json.response);
        }
        else if (json.status == "ok_alt") {
            if (request_permission) { alert(json.response); }
        }
        else {
            console.log(json.response);
        }
    });
}

// delete a schema file and list entry
function delete_schema_csv(file_name, id)
{
    if (confirm("This will permanently delete the schema file. Continue?")) {

        // build the route
        let route = `/delete_schema/${file_name}/`;

        // query the flask server
        d3.json(route).then((returned_object) => {
            if (returned_object.status == "ok") {
                schema_list.select("#div-id-" + id).remove();
                alert(returned_object.response);
            }
            else if (returned_object.status == "ok_alt") {
                schema_list.select("#div-id-" + id).remove();
                alert(returned_object.response);
            }
            else {
                console.log(returned_object.response);
            }
        });
    }
}

// send the current characteristic schema to the current inspection report
function commit_schema()
{
    // if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
    //     return;
    // }

    // get the identifications
    let part_id = meta_part_id.property("data-meta");
    let report_id = meta_report_id.property("data-meta");

    let table_data = schema_table.select("tbody").selectAll("tr").data();

    let char_obj = {};
    let gauge_type_obj = {};
    table_data.forEach((x) => {
        char_obj["name"] = x.name;
        char_obj["nominal"] = x.nominal;
        char_obj["usl"] = x.usl;
        char_obj["lsl"] = x.lsl;
        char_obj["precision"] = x.precision;
        char_obj["specification_type_id"] = x.spec_type;
        char_obj["characteristic_type_id"] = x.char_type;
        gauge_type_obj["id"] = x.gauge_type;
    });

    let data = {
        ident: {
            part_id: part_id,
            report_id: report_id
        },
        info: {

        }
    }


    // if (confirm("This action cannot be reverted. Continue?")) {

    //     // get the data
    //     let my_form = document.querySelector("#characteristic_schema_form_id");
    //     let form_data = new FormData(my_form);

    //     // build the route
    //     let item = meta_details.property("data-item");
    //     let drawing = meta_details.property("data-drawing");
    //     let revision = meta_details.property("data-revision");
    //     let route = `/commit_new_characteristic_schema/${item}/${drawing}/${revision}/`;

    //     // send the POST
    //     fetch(route, {
    //         method: "POST",
    //         body: form_data
    //     }).then((response) => {
    //         if (response.ok) {
    //             return response.json();
    //         }
    //         else {
    //             throw new Error("Server response wasn't cool");
    //         }
    //     }).then((json) => {
    //         if (json.status == "ok") {
    //             console.log(json.response);
    //         }
    //         else if (json.status == "ok_alt") {
    //             alert(json.response);
    //         }
    //         else {
    //             console.log(json.response);
    //         }
    //     });
    // }
}

// add a new row to the current characteristic schema
function add_schema_row(dataset)
{
    let current_data = schema_table.selectAll("tbody").selectAll("tr").data();
    if (current_data.length > 0) {
        dataset = current_data.concat(dataset);
    }
    schema_table.select("tbody").selectAll("tr").remove();

    let rows = schema_table.select("tbody")
        .selectAll("tr")
        .data(dataset)
        .enter()
        .append("tr");

    let cells = rows.selectAll("td")
        .data((r, i) => {
            return ["name", "nominal", "usl", "lsl", "precision", "spec_type", "char_type", "gauge_type"].map((c) => {
                return { col: c, value: r[c], index: i };
            });
        })
        .enter()
        .append("td");

    // numerical inputs
    cells.filter((x) => {
            if (x.col == "nominal" || x.col == "usl" || x.col == "lsl" || x.col == "precision") {
                return true;
            }
        })
        .insert("input")
        .attr("class", "table_input_dark")
        .attr("type", "number")
        .attr("name", (x) => `${x.index}-${x.col}`)
        .attr("value", (x) => x.value);

    // text inputs
    cells.filter((x) => {
            if (x.col == "name") {
                return true;
            }
        })
        .insert("input")
        .attr("class", "table_input_dark")
        .attr("type", "text")
        .attr("value", (x) => x.value)
        .attr("name", (x) => `${x.index}-${x.col}`)
        .style("border-radius", "6px 0px 0px 6px");

    // specification types
    d3.json("/get_schema_type_lists/").then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;
            let spec_types_list = dataset.spec_types;
            let char_types_list = dataset.char_types;
            let gauge_types_list = dataset.gauge_types;

            // populate the specification types
            cells.filter((x) => {
                    if (x.col == "spec_type") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "table_select_dark")
                .attr("name", (x) => `${x.index}-${x.col}`)
                .selectAll("option")
                .data(spec_types_list)
                .enter()
                .append("option")
                .attr("value", (x) => x.item)
                .text((x) => x.item);
            cells.filter((x) => {
                    if (x.col == "spec_type") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.value);

            // populate the characteristic types
            cells.filter((x) => {
                    if (x.col == "char_type") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "table_select_dark")
                .attr("name", (x) => `${x.index}-${x.col}`)
                .selectAll("option")
                .data(char_types_list)
                .enter()
                .append("option")
                .attr("value", (x) => x.item)
                .text((x) => x.item);
            cells.filter((x) => {
                    if (x.col == "char_type") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.value);

            // populate the gauge types
            cells.filter((x) => {
                    if (x.col == "gauge_type") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "table_select_dark")
                .attr("name", (x) => `${x.index}-${x.col}`)
                .selectAll("option")
                .data(gauge_types_list)
                .enter()
                .append("option")
                .attr("value", (x) => x.item)
                .text((x) => x.item);
            cells.filter((x) => {
                    if (x.col == "gauge_type") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.value)
                .style("border-radius", "0px 6px 6px 0px");
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });

    // set the start/end cell rounded corners
    rows.selectAll("td").filter((x) => {
            if (x.col == "name") {
                return true;
            }
        })
        .attr("class", "data_table_start_cell");
    rows.selectAll("td").filter((x) => {
            if (x.col == "gauge_type") {
                return true;
            }
        })
        .attr("class", "data_table_end_cell");
}

// remove the last row from the current characteristic schema
function remove_schema_row()
{
    schema_table.select("tbody").select("tr:last-child").remove();
}

// #endregion

// #region report controls

function report_item_number_changed()
{
    // get the current item number
    let item_number = ctl_item_number.property("value");

    // build the route
    let route = `/get_drawing_from_item_number/${item_number}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // set the drawing
            ctl_drawing.property("value", dataset.drawing);

            // set the revision(s)
            ctl_revision.selectAll("option").remove();
            ctl_revision.selectAll("option")
                .data(dataset.revisions)
                .enter()
                .append("option")
                .attr("value", (x) => x)
                .text((x) => x);
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function report_drawing_changed()
{
    // get the current drawing
    let drawing = ctl_drawing.property("value");

    // build the route
    let route = `/get_item_number_from_drawing/${drawing}/`

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // set the item number
            ctl_item_number.property("value", dataset.item_number);

            // set the revision(s)
            ctl_revision.selectAll("option").remove();
            ctl_revision.selectAll("option")
                .data(dataset.revisions)
                .enter()
                .append("option")
                .attr("value", (x) => x)
                .text((x) => x);
        }
        else if (returned_object.status == "ok_alt") {
            alert(returned_object.response);
        }
        else {
            console.log(returned_object.response);
        }
    });
}

function create_new_inspection_report()
{
    // get the new values
    let item = ctl_item_number.property("value");
    let drawing = ctl_drawing.property("value");
    let revision = ctl_revision.property("value");

    // handle null values
    if (revision == "") {
        revision = "__null";
    }

    // build the route
    let route = `/create_new_inspection_report/${item}/${drawing}/${revision}/`;

    // query the flask server
    d3.json(route).then((returned_object) => {
        if (returned_object.status == "ok") {

            // extract the requested data
            let dataset = returned_object.response;

            // notify the user
            alert(dataset);
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

// populate an item list
function populate_item_list(list_container, dataset)
{
    // remove previous data
    list_container.selectAll("li").remove();

    // populate the list
    let items = list_container.selectAll("li")
        .data(dataset)
        .enter()
        .append("li")
        .append("div")
        .attr("id", (x) => "div-id-" + x)
        .attr("class", "grid_container_item")
        .style("--grid-template-columns", "3fr 1fr 1fr 1fr");

    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px 0px 0px 6px")
        .style("text-align", "left")
        .attr("class", "table_input_dark")
        .attr("id", (x) => `input-${x}`)
        .attr("value", (x) => x);
    
    items.append("button")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .style("border-radius", "0px")
        .attr("type", "button")
        .text("Load")
        .on("click", (pointer, data) => { load_schema_csv(d3.select("#input-" + data).property("value")); })

    items.append("button")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .style("border-radius", "0px")
        .attr("type", "button")
        .text("Save")
        .on("click", (pointer, data) => { save_schema_csv(d3.select("#input-" + data).property("value"), true); })

    items.append("button")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("type", "button")
        .text("Delete")
        .on("click", (pointer, data) => { delete_schema_csv(d3.select("#input-" + data).property("value"), data); })
}

// #endregion

// #region sidebar control

// toggle the open/close state for the sidebar buttons
function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "controls") {
        if (document.getElementById("inspection_report_controls_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_controls_sidebar").style.width = close_width;
            document.getElementById("inspection_report_controls").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_controls_sidebar").style.width = open_width;
            document.getElementById("inspection_report_controls").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "existing") {
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
    else if (destination_arg == "lots") {
        if (document.getElementById("inspection_report_lot_numbers_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_lot_numbers_sidebar").style.width = close_width;
            document.getElementById("inspection_report_lot_numbers").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_lot_numbers_sidebar").style.width = open_width;
            document.getElementById("inspection_report_lot_numbers").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "char_filter") {
        if (document.getElementById("inspection_report_char_filter_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_char_filter_sidebar").style.width = close_width;
            document.getElementById("inspection_report_char_filter").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_char_filter_sidebar").style.width = open_width;
            document.getElementById("inspection_report_char_filter").style.marginLeft = open_width;
        }
    }
}

//#endregion