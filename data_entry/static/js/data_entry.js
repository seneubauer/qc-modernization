
// characteristics
const inpsection_report_identity = d3.select("#characteristics_inspection_report_identity");
const main_characteristic_table = d3.select("#main_char_table");

// inspection_reports
const ir_button_save = d3.select("#inspection_report_save_btn");
const ir_button_create = d3.select("#inspection_report_create_new_btn");
const ir_input_new_item_filter = d3.select("#inspection_report_item_filter");
const ir_select_new_item = d3.select("#inspection_report_item");
const ir_input_new_drawing_filter = d3.select("#inspection_report_drawing_filter");
const ir_select_new_drawing = d3.select("#inspection_report_drawing");
const ir_input_char_schema_filter = d3.select("#inspection_report_char_schema_filter");
const ir_select_char_schema = d3.select("#inspection_report_char_schema");
const ir_select_filter_part = d3.select("#inspection_report_filter_part");
const ir_select_filter_job_order = d3.select("#inspection_report_filter_job_order");
const ir_input_started_after = d3.select("#inspection_report_filter_start_after");
const ir_input_finished_before = d3.select("#inspection_report_filter_finished_before");
const ir_ul_list = d3.select("#inspection_report_filtered_list");

// characteristic display
const cd_button_apply = d3.select("#characteristic_display_apply");
const cd_select_display_type = d3.select("#characteristic_display_type");
const cd_input_name = d3.select("#characteristic_display_name");
const cd_select_frequency_type = d3.select("#characteristic_display_frequency_type");
const cd_select_check = d3.select("#characteristic_display_check");
const cd_select_revision = d3.select("#characteristic_display_revision");
const cd_select_part_index = d3.select("#characteristic_display_part_index");
const cd_select_has_deviations = d3.select("#characteristic_display_has_deviations");
const cd_select_inspector = d3.select("#characteristic_display_inspector");
const cd_select_gauge = d3.select("#characteristic_display_gauge");
const cd_select_gauge_type = d3.select("#characteristic_display_gauge_type");
const cd_select_specification_type = d3.select("#characteristic_display_specification_type");
const cd_select_characteristic_type = d3.select("#characteristic_display_characteristic_type");

// metadata
const md_label_identity = d3.select("#metadata_identity");
const md_button_save = d3.select("#metadata_save");
const md_select_disposition = d3.select("#metadata_disposition");
const md_select_material_type = d3.select("#metadata_material_type");
const md_select_inspector = d3.select("#metadata_inspector");
const md_select_job_order = d3.select("#metadata_job_order");
const md_select_supplier = d3.select("#metadata_supplier");
const md_input_full_inspect_interval = d3.select("#metadata_full_inspect_interval");
const md_input_released_quantity = d3.select("#metadata_released_qty");
const md_input_completed_quantity = d3.select("#metadata_completed_qty");

// receiver numbers
const rn_input_search_term = d3.select("#receiver_numbers_search_term");
const rn_select_selected = d3.select("#receiver_numbers_selected");
const rn_button_add = d3.select("#receiver_numbers_add");
const rn_ul_list = d3.select("#receiver_numbers_list");

// purchase orders
const po_input_search_term = d3.select("#purchase_orders_search_term");
const po_select_selected = d3.select("#purchase_orders_selected");
const po_button_add = d3.select("#purchase_orders_add");
const po_ul_list = d3.select("#purchase_orders_list");

// lot numbers
const ln_input_search_term = d3.select("#lot_numbers_search_term");
const ln_select_selected = d3.select("#lot_numbers_selected");
const ln_button_add = d3.select("#lot_numbers_add");
const ln_ul_list = d3.select("#lot_numbers_list");

// main characteristic table columns
const char_table_columns = [
    { display: "Part Index",            key: "part_index",          value_type: "number", type: "input",  show: [true, true, true] },
    { display: "Check",                 key: "check_id",            value_type: "static", type: "label",  show: [true, true, true] },
    { display: "Frequency",             key: "frequency_type",      value_type: "static", type: "label",  show: [false, true, true] },
    { display: "Revision",              key: "revision",            value_type: "static", type: "label",  show: [true, true, true] },
    { display: "Name",                  key: "name",                value_type: "static", type: "label",  show: [true, true, true] },
    { display: "Nominal",               key: "nominal",             value_type: "number", type: "label",  show: [true, false, true] },
    { display: "USL",                   key: "usl",                 value_type: "number", type: "label",  show: [true, false, true] },
    { display: "LSL",                   key: "lsl",                 value_type: "number", type: "label",  show: [true, false, true] },
    { display: "Measured",              key: "measured",            value_type: "number", type: "input",  show: [true, false, true] },
    { display: "Precision",             key: "precision",           value_type: "static", type: "label",  show: [false, true, true] },
    { display: "Inspector",             key: "employee_id",         value_type: "static", type: "select", show: [false, true, true] },
    { display: "Gauge",                 key: "gauge_id",            value_type: "static", type: "select", show: [true, false, true] },
    { display: "Gauge Type",            key: "gauge_type",          value_type: "static", type: "label",  show: [false, true, true] },
    { display: "Specification Type",    key: "specification_type",  value_type: "static", type: "label",  show: [false, true, true] },
    { display: "Characteristic Type",   key: "characteristic_type", value_type: "static", type: "label",  show: [false, true, true] }
];

init();

// #region page initialization

function init()
{
    // populate selectors
    populate_generic_selectors();

    // inspection reports
    ir_input_new_item_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_new_part_selectors();
        }
    });
    ir_input_new_drawing_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_new_part_selectors();
        }
    });
    ir_input_char_schema_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_characteristic_schema_selector();
        }
    });
    ir_input_started_after.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_inspection_reports();
        }
    });
    ir_input_finished_before.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_inspection_reports();
        }
    });
    ir_select_filter_part.on("change", update_filtered_inspection_reports);
    ir_select_filter_job_order.on("change", update_filtered_inspection_reports);
    ir_select_new_item.on("change", inspection_reports_item_number_changed);
    ir_select_new_drawing.on("change", inspection_reports_drawing_changed);
    ir_select_char_schema.on("change", update_characteristic_schema_selector);
    ir_input_started_after.property("value", "1970-01-01");
    ir_input_finished_before.property("value", "2100-01-01");

    // characteristic display
    cd_button_apply.on("click", () => get_filtered_characteristics());
    cd_button_apply.on("change", () => get_filtered_characteristics());

    // metadata
    md_button_save.on("click", metadata_save);
    md_input_full_inspect_interval.property("value", 0);
    md_input_released_quantity.property("value", 0);
    md_input_completed_quantity.property("value", 0);

    // receiver numbers
    rn_input_search_term.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_receiver_numbers(-1);
        }
    });
    rn_button_add.on("click", assign_receiver_number_association);

    // purchase orders
    po_input_search_term.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_purchase_orders(-1);
        }
    });
    po_button_add.on("click", assign_purchase_order_association);

    // lot numbers
    ln_input_search_term.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_lot_numbers(-1);
        }
    });
    ln_button_add.on("click", assign_lot_number_association);
}

function populate_generic_selectors()
{
    // inspection reports
    d3.json("/get_all_parts/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ir_select_filter_part.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            ir_select_filter_part.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return `${x.item}, ${x.drawing}, ${x.revision}`;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    d3.json("/get_all_job_orders/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ir_select_filter_job_order.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            ir_select_filter_job_order.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }
                });
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    update_new_part_selectors();
    update_characteristic_schema_selector();

    // characteristic display
    cd_select_display_type.selectAll("option")
        .data([
            { id: 0, name: "Data Entry" },
            { id: 1, name: "Metadata" },
            { id: 2, name: "All" }
        ])
        .enter()
        .append("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cd_select_has_deviations.selectAll("option")
        .data([
            { id: -1, name: "n/a" },
            { id: 0, name: "False" },
            { id: 1, name: "True" }
        ])
        .enter()
        .append("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);

    // metadata
    d3.json("/get_all_disposition_types/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            md_select_disposition.selectAll("option").remove();

            // populate the item numbers
            md_select_disposition.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    d3.json("/get_all_material_types/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            md_select_material_type.selectAll("option").remove();

            // populate the item numbers
            md_select_material_type.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    d3.json("/get_all_employees/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            md_select_inspector.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_inspector.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    d3.json("/get_all_job_orders/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            md_select_job_order.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_job_order.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
    d3.json("/get_all_suppliers/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            md_select_supplier.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_supplier.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });

    // receiver numbers
    d3.json("/get_all_receiver_numbers/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            rn_select_selected.selectAll("option").remove();

            // populate the item numbers
            rn_select_selected.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });

    // purchase orders
    d3.json("/get_all_purchase_orders/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            po_select_selected.selectAll("option").remove();

            // populate the item numbers
            po_select_selected.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });

    // lot numbers
    d3.json("/get_all_lot_numbers/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ln_select_selected.selectAll("option").remove();

            // populate the item numbers
            ln_select_selected.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region inspection reports

function inspection_report_selected(data)
{
    // update the main display
    inpsection_report_identity.text(`${data.item} // ${data.drawing} // ${data.revision}`);

    // characteristic display
    get_filtered_characteristics(data.inspection_id, data.part_id);
    update_filter_selectors(data.inspection_id, data.part_id);

    // metadata
    md_label_identity.text(`${data.item} // ${data.drawing} // ${data.revision}`);
    md_label_identity.attr("data-part_id", data.part_id);
    md_label_identity.attr("data-inspection_id", data.inspection_id);
    md_select_disposition.property("value", data.disposition_type_id);
    md_select_material_type.property("value", data.material_type_id);
    md_select_inspector.property("value", data.employee_id);
    md_select_job_order.property("value", data.job_order_id);
    md_select_supplier.property("value", data.supplier_id);
    md_input_full_inspect_interval.property("value", data.full_inspect_interval);
    md_input_released_quantity.property("value", data.released_qty);
    md_input_completed_quantity.property("value", data.completed_qty);

    // receiver numbers
    update_filtered_receiver_numbers(data.inspection_id);

    // purchase orders
    update_filtered_purchase_orders(data.inspection_id);

    // lot numbers
    update_filtered_lot_numbers(data.inspection_id);
}

function update_filtered_inspection_reports()
{
    // get the raw values
    let started_after = new Date(ir_input_started_after.property("value") + "T00:00:00");
    let finished_before = new Date(ir_input_finished_before.property("value") + "T00:00:00");
    let part_id = ir_select_filter_part.property("value");
    let job_order_id = ir_select_filter_job_order.property("value");

    // logic gates
    if (started_after instanceof Date && !isNaN(started_after)) {
        started_after = new Date(1970, 0, 1);
    }
    if (finished_before instanceof Date && !isNaN(finished_before)) {
        finished_before = new Date(2100, 0, 1);
    }
    if (part_id == undefined || part_id == "") {
        part_id = -1;
    }
    if (job_order_id == undefined || job_order_id == "") {
        job_order_id = -1;
    }

    // parse the dates
    let start_day = started_after.getDate();
    let start_month = started_after.getMonth() + 1;
    let start_year = started_after.getFullYear();
    let finish_day = finished_before.getDate();
    let finish_month = finished_before.getMonth() + 1;
    let finish_year = finished_before.getFullYear();

    // query the flask server
    d3.json("/data_entry/get_filtered_inspection_reports/", {
        method: "POST",
        body: JSON.stringify({
            part_id: part_id,
            job_order_id: job_order_id,
            start_day: start_day,
            start_month: start_month,
            start_year: start_year,
            finish_day: finish_day,
            finish_month: finish_month,
            finish_year: finish_year
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ir_ul_list.selectAll("li").remove();

            // populate the inspection reports list
            let items = ir_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "2fr 2fr 1fr 2fr")
                .on("click", (_, d) => inspection_report_selected(d));
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "center")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.item);
            items.append("label")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("text-align", "center")
                .text((x) => x.drawing);
            items.append("label")
                .style("--grid-column", "3")
                .style("--grid-row", "1")
                .style("text-align", "center")
                .text((x) => x.revision);
            items.append("label")
                .style("--grid-column", "4")
                .style("--grid-row", "1")
                .style("text-align", "center")
                .style("border-radius", "0px 6px 6px 0px")
                .text((x) => {
                    if (x.job_order == null) {
                        return "n/a";
                    }
                    else {
                        return x.job_order;
                    }
                });
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function inspection_reports_item_number_changed()
{
    ir_select_new_drawing.property("value", ir_select_new_item.property("value"));
}

function inspection_reports_drawing_changed()
{
    ir_select_new_item.property("value", ir_select_new_drawing.property("value"));
}

function update_new_part_selectors()
{
    // query the flask server
    d3.json("/data_entry/get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            item: ir_input_new_item_filter.property("value"),
            drawing: ir_input_new_drawing_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ir_select_new_item.selectAll("option").remove();
            ir_select_new_drawing.selectAll("option").remove();

            // populate the item numbers
            ir_select_new_item.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.item);
            ir_select_new_item.property("value", json.response[0].id)

            // populate the drawings
            ir_select_new_drawing.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.drawing);
            ir_select_new_drawing.property("value", json.response[0].id)
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function update_characteristic_schema_selector()
{
    // query the flask server
    d3.json("/data_entry/get_filtered_characteristic_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_char_schema_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ir_select_char_schema.selectAll("option").remove();

            // populate the characteristic schema
            ir_select_char_schema.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x)
                .text((x) => x);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region characteristic display

function update_filter_selectors(inspection_id, part_id)
{
    // query the flask server
    d3.json("/data_entry/get_filter_selector_lists/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            part_id: part_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // update the frequency types
            cd_select_frequency_type.selectAll("option").remove();
            json.response.frequency_types.unshift({ id: -1, name: "n/a" });
            cd_select_frequency_type.selectAll("option")
                .data(json.response.frequency_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the check ids
            cd_select_check.selectAll("option").remove();
            json.response.check_ids.unshift({ id: -1, value: "n/a" });
            cd_select_check.selectAll("option")
                .data(json.response.check_ids)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.value);

            // update the revisions
            cd_select_revision.selectAll("option").remove();
            json.response.revisions.unshift({ revision: "" });
            cd_select_revision.selectAll("option")
                .data(json.response.revisions)
                .enter()
                .append("option")
                .attr("value", (x) => x.revision)
                .text((x) => x.revision);

            // update the part indices
            cd_select_part_index.selectAll("option").remove();
            json.response.part_indices.unshift({ id: -1, value: "n/a" });
            cd_select_part_index.selectAll("option")
                .data(json.response.part_indices)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.value);

            // update the inspectors
            cd_select_inspector.selectAll("option").remove();
            json.response.inspectors.unshift({ id: -1, name: "n/a" });
            cd_select_inspector.selectAll("option")
                .data(json.response.inspectors)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauges
            cd_select_gauge.selectAll("option").remove();
            json.response.gauges.unshift({ id: -1, name: "n/a" });
            cd_select_gauge.selectAll("option")
                .data(json.response.gauges)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauge types
            cd_select_gauge_type.selectAll("option").remove();
            json.response.gauge_types.unshift({ id: -1, name: "n/a" });
            cd_select_gauge_type.selectAll("option")
                .data(json.response.gauge_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the specification types
            cd_select_specification_type.selectAll("option").remove();
            json.response.specification_types.unshift({ id: -1, name: "n/a" });
            cd_select_specification_type.selectAll("option")
                .data(json.response.specification_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the characteristic types
            cd_select_characteristic_type.selectAll("option").remove();
            json.response.characteristic_types.unshift({ id: -1, name: "n/a" });
            cd_select_characteristic_type.selectAll("option")
                .data(json.response.characteristic_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function get_filtered_characteristics(inspection_id = -1, part_id = -1)
{
    // confirm the identity parameters
    if (inspection_id == -1) {
        inspection_id = md_label_identity.attr("data-inspection_id");
        if (inspection_id == undefined) {
            return;
        }
    }
    if (part_id == -1) {
        part_id = md_label_identity.attr("data-part_id");
        if (part_id == undefined) {
            return;
        }
    }

    // display type
    display_type = cd_select_display_type.property("value");

    // ensure content format
    let val_check_id = cd_select_check.property("value");
    let val_part_index = cd_select_part_index.property("value");
    let val_frequency_type_id = cd_select_frequency_type.property("value");
    let val_revision = cd_select_revision.property("value");
    let val_name = cd_input_name.property("value");
    let val_has_deviations = cd_select_has_deviations.property("value");
    let val_inspector_id = cd_select_inspector.property("value");
    let val_gauge_id = cd_select_gauge.property("value");
    let val_gauge_type_id = cd_select_gauge_type.property("value");
    let val_specification_type_id = cd_select_specification_type.property("value");
    let val_characteristic_type_id = cd_select_characteristic_type.property("value");
    if (val_check_id == "") { val_check_id = -1; }
    if (val_part_index == "") { val_part_index = -1; }
    if (val_frequency_type_id == "") { val_frequency_type_id = -1; }
    if (val_inspector_id == "") { val_inspector_id = -1; }
    if (val_gauge_id == "") { val_gauge_id = -1; }
    if (val_gauge_type_id == "") { val_gauge_type_id = -1; }
    if (val_specification_type_id == "") { val_specification_type_id = -1; }
    if (val_characteristic_type_id == "") { val_characteristic_type_id = -1; }

    // query the flask server
    d3.json("/data_entry/get_filtered_inspection_report_part_characteristics/", {
        method: "POST",
        body: JSON.stringify({
            identity: {
                inspection_id: inspection_id,
                part_id: part_id
            },
            content: {
                check_id: val_check_id,
                part_index: val_part_index,
                frequency_type_id: val_frequency_type_id,
                revision: val_revision,
                name: val_name,
                has_deviations: val_has_deviations,
                inspector_id: val_inspector_id,
                gauge_id: val_gauge_id,
                gauge_type_id: val_gauge_type_id,
                specification_type_id: val_specification_type_id,
                characteristic_type_id: val_characteristic_type_id
            }
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old columns
            main_characteristic_table.selectAll("thead").remove();

            // add the columns
            main_characteristic_table.append("thead")
                .selectAll("tr")
                .data(char_table_columns)
                .enter()
                .append("th")
                .attr("scope", "col")
                .text((x) => x.display)
                .style("display", (x) => {
                    if (!x.show[display_type]) {
                        return "none";
                    }
                });

            // clear the old rows
            main_characteristic_table.selectAll("tbody").remove();

            // add the rows
            let rows = main_characteristic_table.append("tbody")
                .selectAll("tr")
                .data(json.response.characteristics)
                .enter()
                .append("tr");

            // create the cells
            let cells = rows.selectAll("td")
                .data((r) => {
                    return char_table_columns.map((c) => {
                        return {
                            column: c,
                            row: {
                                value: r[c.key],
                                has_deviations: r.has_deviations,
                                precision: r.precision
                            }
                        };
                    });
                })
                .enter()
                .append("td")
                .style("display", (x) => {
                    if (!x.column.show[display_type]) {
                        return "none";
                    }
                });

            // assign readonly values
            cells.filter((x) => {
                    if (x.column.type == "label") {
                        return true;
                    }
                })
                .insert("input")
                .attr("class", "table_label_light")
                .attr("readonly", true)
                .attr("value", (x) => {
                    if (x.column.value_type == "number") {
                        return x.row.value.toFixed(x.row.precision);
                    }
                    else if (x.column.value_type == "static" && x.column.key == "name") {
                        if (x.row.has_deviations) {
                            return `**${x.row.value}`;
                        }
                        else {
                            return x.row.value;
                        }
                    }
                    else {
                        return x.row.value;
                    }
                });

            // assign inputs
            cells.filter((x) => {
                    if (x.column.type == "input") {
                        return true;
                    }
                })
                .insert("input")
                .attr("class", "table_input_light")
                .attr("value", (x) => {
                    if (x.column.key == "measured") {
                        if (x.row.value != null) {
                            return x.row.value.toFixed(x.row.precision);
                        }
                        else {
                            return "";
                        }
                    }
                    else {
                        return x.row.value;
                    }
                });

            // gauges
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "gauge_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "table_select_light")
                .selectAll("option")
                .data(json.response.gauges)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "gauge_id") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value);

            // inspectors
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "employee_id") {
                        
                    }
                })
                .insert("select")
                .attr("class", "table_select_light")
                .selectAll("option")
                .data(json.response.inspectors)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "employee_id") {
                        
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value);

            // set the start cell class
            rows.selectAll("td")
                .filter((x) => {
                    let index = char_table_columns.slice().filter((c) => {
                        return c.show[display_type];
                    })[0].key;
                    return x.column.key == index;
                })
                .attr("class", "data_table_start_cell")
                .selectAll("*")
                .style("border-radius", "6px 0px 0px 6px");

            // set the end cell class
            rows.selectAll("td")
                .filter((x) => {
                    let index = char_table_columns.slice().filter((c) => {
                        return c.show[display_type];
                    }).reverse()[0].key;
                    return x.column.key == index;
                })
                .attr("class", "data_table_end_cell")
                .selectAll("*")
                .style("border-radius", "0px 6px 6px 0px");
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function submit_current_characteristics()
{
    
}

// #endregion characteristics

// #region metadata

function metadata_save()
{
    // get the identifications
    let part_id = md_label_identity.attr("data-part_id");
    let inspection_id = md_label_identity.attr("data-inspection_id");

    // logic gate
    if (inspection_id == undefined || part_id == undefined) {
        return;
    }

    if (!confirm("This will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input parameters
    let disposition_id = md_select_disposition.property("value");
    let material_type_id = md_select_material_type.property("value");
    let inspector_id = md_select_inspector.property("value");
    let job_order_id = md_select_job_order.property("value");
    let supplier_id = md_select_supplier.property("value");
    let full_inspect_interval = md_input_full_inspect_interval.property("value");
    let released_qty = md_input_released_quantity.property("value");
    let completed_qty = md_input_completed_quantity.property("value");

    // handle possible nulls
    if (supplier_id == -1) {
        supplier_id = null;
    }
    if (job_order_id == -1) {
        job_order_id = null;
    }
    if (inspector_id == -1) {
        inspector_id = null;
    }

    // build the form data object
    let data = {
        identity: {
            part_id: part_id,
            inspection_id: inspection_id
        },
        content: {
            disposition_id: disposition_id,
            material_type_id: material_type_id,
            employee_id: inspector_id,
            job_order_id: job_order_id,
            supplier_id: supplier_id,
            full_inspect_interval: full_inspect_interval,
            released_qty: released_qty,
            completed_qty: completed_qty
        }
    }

    // query the flask server
    d3.json("/data_entry/save_metadata/", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region receiver numbers

function update_filtered_receiver_numbers(inspection_id = -1)
{
    // get the input parameters
    let search_term = rn_input_search_term.property("value");
    if (inspection_id == -1) {
        inspection_id = md_label_identity.attr("data-inspection_id");
        if (inspection_id == undefined) {
            return;
        }
    }

    // query the flask server
    d3.json("/data_entry/get_filtered_receiver_numbers/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: search_term
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            rn_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = rn_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => remove_receiver_number_association(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function assign_receiver_number_association()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input parameters
    let search_term = rn_input_search_term.property("value");
    let inspection_id = md_label_identity.attr("data-inspection_id");
    let receiver_number_id = rn_select_selected.property("value");

    // logic gate
    if (inspection_id == undefined) {
        return;
    }

    // query the flask server
    d3.json("/data_entry/assign_receiver_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            receiver_number_id: receiver_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            rn_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = rn_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function remove_receiver_number_association(data)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input arguments
    let search_term = rn_input_search_term.property("value");
    let receiver_number_id = data.id;
    let inspection_id = data.inspection_id;

    // query the flask server
    d3.json("/data_entry/remove_receiver_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            receiver_number_id: receiver_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            rn_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = rn_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region purchase orders

function update_filtered_purchase_orders(inspection_id = -1)
{
    // get the input parameters
    let search_term = po_input_search_term.property("value");
    if (inspection_id == -1) {
        inspection_id = md_label_identity.attr("data-inspection_id");
        if (inspection_id == undefined) {
            return;
        }
    }

    // query the flask server
    d3.json("/data_entry/get_filtered_purchase_orders/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: search_term
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            po_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = po_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => remove_purchase_order_association(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function assign_purchase_order_association()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input parameters
    let search_term = po_input_search_term.property("value");
    let inspection_id = md_label_identity.attr("data-inspection_id");
    let purchase_order_id = po_select_selected.property("value");

    // logic gate
    if (inspection_id == undefined) {
        return;
    }

    // query the flask server
    d3.json("/data_entry/assign_purchase_order_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            purchase_order_id: purchase_order_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            po_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = po_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function remove_purchase_order_association(data)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input arguments
    let search_term = po_input_search_term.property("value");
    let purchase_order_id = data.id;
    let inspection_id = data.inspection_id;

    // query the flask server
    d3.json("/data_entry/remove_purchase_order_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            purchase_order_id: purchase_order_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            po_ul_list.selectAll("li").remove();

            // populate the receiver numbers
            let items = po_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region lot numbers

function update_filtered_lot_numbers(inspection_id = -1)
{
    // get the input parameters
    let search_term = ln_input_search_term.property("value");
    if (inspection_id == -1) {
        inspection_id = md_label_identity.attr("data-inspection_id");
        if (inspection_id == undefined) {
            return;
        }
    }

    // query the flask server
    d3.json("/data_entry/get_filtered_lot_numbers/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: search_term
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ln_ul_list.selectAll("li").remove();

            // populate the lot numbers
            let items = ln_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => remove_lot_number_association(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function assign_lot_number_association()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input parameters
    let search_term = ln_input_search_term.property("value");
    let inspection_id = md_label_identity.attr("data-inspection_id");
    let lot_number_id = ln_select_selected.property("value");

    // logic gate
    if (inspection_id == undefined) {
        return;
    }

    // query the flask server
    d3.json("/data_entry/assign_lot_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            lot_number_id: lot_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ln_ul_list.selectAll("li").remove();

            // populate the lot numbers
            let items = ln_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

function remove_lot_number_association(data)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the input arguments
    let search_term = ln_input_search_term.property("value");
    let lot_number_id = data.id;
    let inspection_id = data.inspection_id;

    // query the flask server
    d3.json("/data_entry/remove_lot_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            inspection_id: inspection_id,
            lot_number_id: lot_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            ln_ul_list.selectAll("li").remove();

            // populate the lot numbers
            let items = ln_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "grid_container_item")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .text("Delete")
                .on("click", (_, d) => console.log(d));
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
    });
}

// #endregion







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

function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "inspection_reports") {
        if (document.getElementById("inspection_reports_sidebar").style.width == open_width) {
            document.getElementById("inspection_reports_sidebar").style.width = close_width;
            document.getElementById("inspection_reports_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_reports_sidebar").style.width = open_width;
            document.getElementById("inspection_reports_btn").style.marginLeft = open_width;
            update_filtered_inspection_reports();
        }
    }
    else if (destination_arg == "characteristic_display") {
        if (document.getElementById("characteristic_display_sidebar").style.width == open_width) {
            document.getElementById("characteristic_display_sidebar").style.width = close_width;
            document.getElementById("characteristic_display_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("characteristic_display_sidebar").style.width = open_width;
            document.getElementById("characteristic_display_btn").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "metadata") {
        if (document.getElementById("metadata_sidebar").style.width == open_width) {
            document.getElementById("metadata_sidebar").style.width = close_width;
            document.getElementById("metadata_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("metadata_sidebar").style.width = open_width;
            document.getElementById("metadata_btn").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "receiver_numbers") {
        if (document.getElementById("receiver_numbers_sidebar").style.width == open_width) {
            document.getElementById("receiver_numbers_sidebar").style.width = close_width;
            document.getElementById("receiver_numbers_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("receiver_numbers_sidebar").style.width = open_width;
            document.getElementById("receiver_numbers_btn").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "purchase_orders") {
        if (document.getElementById("purchase_orders_sidebar").style.width == open_width) {
            document.getElementById("purchase_orders_sidebar").style.width = close_width;
            document.getElementById("purchase_orders_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("purchase_orders_sidebar").style.width = open_width;
            document.getElementById("purchase_orders_btn").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "lot_numbers") {
        if (document.getElementById("lot_numbers_sidebar").style.width == open_width) {
            document.getElementById("lot_numbers_sidebar").style.width = close_width;
            document.getElementById("lot_numbers_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("lot_numbers_sidebar").style.width = open_width;
            document.getElementById("lot_numbers_btn").style.marginLeft = open_width;
        }
    }
    else if (destination_arg == "deviations") {
        if (document.getElementById("deviations_sidebar").style.width == open_width) {
            document.getElementById("deviations_sidebar").style.width = close_width;
            document.getElementById("deviations_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("deviations_sidebar").style.width = open_width;
            document.getElementById("deviations_btn").style.marginLeft = open_width;
        }
    }
}

//#endregion
