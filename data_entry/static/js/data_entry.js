
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const main_characteristic_table = d3.select("#main_char_table");
const char_table_context_menu = document.getElementById("char_context_menu");
const char_table_scope = document.querySelector("#main_char_table");

// inspection_reports
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
const md_ul_quantities = d3.select("#metadata_quantity_list");

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

// deviations
const dv_button_save = d3.select("#deviations_save");
const dv_button_add = d3.select("#deviations_add");
const dv_button_remove = d3.select("#deviations_remove");
const dv_input_notes = d3.select("#deviations_notes");
const dv_ul_list = d3.select("#deviations_list");

// main characteristic table columns
const char_table_columns = [
    { display: "Part Index",            key: "part_index",          value_type: "number", type: "input",  show: [true, true, true] },
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

    // characteristic table
    char_table_scope.addEventListener("contextmenu", (e) => {
        if (e.target.tagName != "TH") {
            e.preventDefault();
            const { clientX: mouseX, clientY: mouseY } = e;
            char_table_context_menu.style.top = `${mouseY}px`;
            char_table_context_menu.style.left = `${mouseX}px`;
            char_table_context_menu.classList.add("visible");

            // tunnel to physical part
            d3.select("#context_menu_0").on("click", () => {
                cd_select_part_index.property("value", e.target.__data__.row.part_index);
                get_filtered_characteristics();
                char_table_context_menu.classList.remove("visible");
            });

            // requery the database
            d3.select("#context_menu_1").on("click", () => {
                get_filtered_characteristics();
                char_table_context_menu.classList.remove("visible");
            });

            // view the associated deviations
            d3.select("#context_menu_2").on("click", () => {
                if (e.target.__data__.row.has_deviations) {
                    populate_deviations(e.target.__data__.row.characteristic_id);
                    toggle_options("deviations", "1000px");
                }
                char_table_context_menu.classList.remove("visible");
            });

            // save the characteristics
            d3.select("#context_menu_3").on("click", () => {
                submit_current_characteristics();
                char_table_context_menu.classList.remove("visible");
            });
        }
    });
    char_table_scope.addEventListener("click", (e) => {
        if (e.target.offsetParent != char_table_context_menu) {
            char_table_context_menu.classList.remove("visible");
        }
    });

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
    ir_button_create.on("click", inspection_report_create_new);
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

    // deviations
    dv_button_save.on("click", deviations_save);
    dv_button_add.on("click", deviations_add);
    dv_button_remove.on("click", deviations_remove);
}

function populate_generic_selectors()
{
    // inspection reports
    d3.json("/data_entry/get_all_item_drawing_combinations/", {
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
                .attr("data-item", (x) => {
                    if (x.id > 0) {
                        return x.item;
                    }
                    else {
                        return "";
                    }
                })
                .attr("data-drawing", (x) => {
                    if (x.id > 0) {
                        return x.drawing;
                    }
                    else {
                        return "";
                    }
                })
                .text((x) => {
                    if (x.id > 0) {
                        return `${x.item}, ${x.drawing}`;
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

function inspection_report_create_new()
{
    // confirm the identity parameter
    let part_id = ir_select_new_item.property("value");
    let schema_id = ir_select_char_schema.property("value");

    // query the flask server
    d3.json("/data_entry/create_new_inspection_report/", {
        method: "POST",
        body: JSON.stringify({
            part_id: part_id,
            schema_id: schema_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {
            update_filtered_inspection_reports();
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

function inspection_report_selected(data)
{
    // update the main display
    navbar_info.text(`${data.item} // ${data.drawing}`);

    // characteristic display
    get_filtered_characteristics(data.inspection_id, data.item, data.drawing);
    update_filter_selectors(data.inspection_id, data.item, data.drawing);

    // metadata
    populate_metadata(data);

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
    let part_item = ir_select_filter_part.attr("data-item");
    let part_drawing = ir_select_filter_part.attr("data-drawing");
    let job_order_id = ir_select_filter_job_order.property("value");

    // logic gates
    if (started_after instanceof Date && !isNaN(started_after)) {
        started_after = new Date(1970, 0, 1);
    }
    if (finished_before instanceof Date && !isNaN(finished_before)) {
        finished_before = new Date(2100, 0, 1);
    }
    if (part_item == undefined) {
        part_item = "";
    }
    if (part_drawing == undefined) {
        part_drawing = "";
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
            item: part_item,
            drawing: part_drawing,
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
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "1fr 1fr 1fr")
                .on("click", (_, d) => inspection_report_selected(d));
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("class", "list-item-label-dark")
                .text((x) => x.item);
            items.append("label")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .attr("class", "list-item-label-dark")
                .text((x) => x.drawing);
            items.append("label")
                .style("--grid-column", "3")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("class", "list-item-label-dark")
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

function update_filter_selectors(inspection_id, item, drawing)
{
    // query the flask server
    d3.json("/data_entry/get_filter_selector_lists/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            item: item,
            drawing: drawing
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

function get_filtered_characteristics(inspection_id = -1, item = "", drawing = "")
{
    // confirm the identity parameters
    if (inspection_id == -1) {
        inspection_id = md_label_identity.attr("data-inspection_id");
        if (inspection_id == undefined) {
            return;
        }
    }
    if (item == "") {
        item = md_label_identity.attr("data-item");
        if (item == undefined) {
            return;
        }
    }
    if (drawing == "") {
        drawing = md_label_identity.attr("data-drawing");
        if (drawing == undefined) {
            return;
        }
    }

    // display type
    display_type = cd_select_display_type.property("value");

    // ensure content format
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
                item: item,
                drawing: drawing
            },
            content: {
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
                .append("tr")
                .on("click", (_, x) => populate_deviations(x.characteristic_id));

            // create the cells
            let cells = rows.selectAll("td")
                .data((r) => {
                    return char_table_columns.map((c) => {
                        return {
                            column: c,
                            row: {
                                value: r[c.key],
                                has_deviations: r.has_deviations,
                                precision: r.precision,
                                characteristic_id: r.characteristic_id,
                                part_index: r.part_index,
                                check_id: r.check_id
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
                .attr("class", "data-table-cell-dark")
                .attr("readonly", true)
                .property("value", (x) => {
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
                    else if (x.column.value_type == "static" && x.column.key == "check_id") {
                        return x.row.value - (json.response.check_min - 1);
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
                .attr("class", "data-table-cell-dark")
                .property("value", (x) => {
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
                }).on("change", (e, x) => {
                    x.row.value = parseFloat(e.srcElement.value);
                });

            // gauges
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "gauge_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
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
                .property("value", (x) => x.row.value)
                .on("change", (e, x) => {
                    x.row.value = parseInt(e.srcElement.value);
                });

            // inspectors
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "employee_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
                .selectAll("option")
                .data(json.response.inspectors)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "employee_id") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value)
                .on("change", (e, x) => {
                    x.row.value = parseInt(e.srcElement.value);
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

function submit_current_characteristics()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reversed. Continue?")) {
        return;
    }

    // extract the modified data
    let checks_data = [];
    let characteristics_data = [];
    main_characteristic_table.selectAll("tbody").selectAll("td").data().forEach(element => {
        switch (element.column.key) {
            case "part_index" || "employee_id":
                if (element.column.type == "input" || element.column.type == "select") {
                    if (checks_data.some((e) => e.check_id == element.row.check_id)) {
                        checks_data.filter((e) => e.check_id == element.row.check_id)[0]
                            .contents.push({
                                key: element.column.key,
                                value: element.row.value
                            });
                    }
                    else {
                        checks_data.push({
                            check_id: element.row.check_id,
                            contents: [{
                                key: element.column.key,
                                value: element.row.value
                            }]
                        });
                    }
                }
                break;
            case "measured" || "gauge_id":
                if (element.column.type == "input" || element.column.type == "select") {
                    if (characteristics_data.some((e) => e.characteristic_id == element.row.characteristic_id)) {
                        characteristics_data.filter((e) => e.characteristic_id == element.row.characteristic_id)[0]
                            .contents.push({
                                key: element.column.key,
                                value: element.row.value
                            });
                    }
                    else {
                        characteristics_data.push({
                            characteristic_id: element.row.characteristic_id,
                            contents: [{
                                key: element.column.key,
                                value: element.row.value
                            }]
                        });
                    }
                }
                break;
        }
    });

    // query the flask server
    d3.json("/data_entry/commit_characteristic_values/", {
        method: "POST",
        body: JSON.stringify({
            checks: checks_data,
            characteristics: characteristics_data
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {
            alert(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
    });
}

// #endregion characteristics

// #region metadata

function populate_metadata(data)
{
    // populate the static values
    md_label_identity.text(`${data.item} // ${data.drawing}`);
    md_label_identity.attr("data-item", data.item);
    md_label_identity.attr("data-drawing", data.drawing);
    md_label_identity.attr("data-part_id", data.part_id);
    md_label_identity.attr("data-inspection_id", data.inspection_id);
    md_select_disposition.property("value", data.disposition_type_id);
    md_select_material_type.property("value", data.material_type_id);
    md_select_inspector.property("value", data.employee_id);
    md_select_job_order.property("value", data.job_order_id);
    md_select_supplier.property("value", data.supplier_id);

    // query the flask server
    d3.json("/data_entry/get_matching_revisions/", {
        method: "POST",
        body: JSON.stringify({
            item: data.item,
            drawing: data.drawing
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // remove the old entries
            md_ul_quantities.selectAll("li").remove();

            // repopulate the revisions list
            let items = md_ul_quantities.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "1fr 2fr 2fr 2fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("class", "list-item-label-dark")
                .text((x) => x.revision)
            items.append("input")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .attr("type", "number")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.full_inspect_interval)
                .on("change", (e, x) => {
                    x.full_inspect_interval = parseInt(e.srcElement.value);
                });
            items.append("input")
                .style("--grid-column", "3")
                .style("--grid-row", "1")
                .attr("type", "number")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.released_qty)
                .on("change", (e, x) => {
                    x.released_qty = parseInt(e.srcElement.value);
                });
            items.append("input")
                .style("--grid-column", "4")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("type", "number")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.completed_qty)
                .on("change", (e, x) => {
                    x.completed_qty = parseInt(e.srcElement.value);
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

function metadata_save()
{
    // get the identifications
    let item = md_label_identity.attr("data-item");
    let drawing = md_label_identity.attr("data-drawing");
    let inspection_id = md_label_identity.attr("data-inspection_id");

    // logic gate
    if (inspection_id == undefined || item == undefined || drawing == undefined) {
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
            item: item,
            drawing: drawing,
            inspection_id: inspection_id
        },
        content: {
            disposition_id: disposition_id,
            material_type_id: material_type_id,
            employee_id: inspector_id,
            job_order_id: job_order_id,
            supplier_id: supplier_id
        },
        sub_data: md_ul_quantities.selectAll("li").data()
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
            alert(json.response);
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
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("class", "list-item-label-dark")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("class", "list-item-button-dark")
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
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("class", "list-item-label-dark")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("class", "list-item-button-dark")
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
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "3fr 1fr");
            items.append("label")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("text-align", "left")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("class", "list-item-label-dark")
                .text((x) => x.name);
            items.append("button")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("class", "list-item-button-dark")
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

// #region deviations

function deviations_save()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // create the data object
    let data = [];
    dv_ul_list.selectAll("li").data().forEach(element => {
        data.push({
            deviation_id: element.id,
            content: {
                nominal: element.nominal,
                usl: element.usl,
                lsl: element.lsl,
                precision: element.precision,
                date_implemented: element.date_implemented,
                notes: element.notes,
                deviation_type_id: element.deviation_type_id,
                employee_id: element.employee_id    
            }
        });
    });

    // query the flask server
    d3.json("/data_entry/save_deviations/", {
        method: "POST",
        body: JSON.stringify({
            data: data
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {
            console.log(json.response);
        }
        else if (json.status == "ok_alert") {
            alert(json.response);
        }
        else if (json.status == "ok_log") {
            console.log(json.response);
        }
        else if (json.status == "err_alert") {
            alert(json.response);
        }
        else if (json.status == "err_log") {
            console.log(json.response);
        }
    });
}

function deviations_add()
{

}

function deviations_remove()
{

}

function deviation_selected(data)
{
    dv_input_notes.property("value", data.notes);
}

function populate_deviations(characteristic_id)
{
    // reset the deviations display
    dv_ul_list.selectAll("li").remove();
    dv_input_notes.property("value", "");

    // query the flask server
    d3.json("/data_entry/get_matching_deviations/", {
        method: "POST",
        body: JSON.stringify({
            characteristic_id: characteristic_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // populate the notes section
            dv_input_notes.property("value", json.response.main[0].notes);

            // repopulate the deviations list
            let items = dv_ul_list.selectAll("li")
                .data(json.response.main)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "2fr 2fr 2fr 1fr 2fr 2fr 2fr")
                .on("click", (_, d) => deviation_selected(d));
            let nominal = items.append("input")
                .style("--grid-column", "1")
                .style("--grid-row", "1")
                .style("border-radius", "6px 0px 0px 6px")
                .attr("type", "number")
                .attr("step", "any")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.nominal.toFixed(x.precision))
                .on("change", (e, x) => {
                    x.nominal = parseFloat(e.srcElement.value);
                });
            let usl = items.append("input")
                .style("--grid-column", "2")
                .style("--grid-row", "1")
                .attr("type", "number")
                .attr("step", "any")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.usl.toFixed(x.precision))
                .on("change", (e, x) => {
                    x.usl = parseFloat(e.srcElement.value);
                });
            let lsl = items.append("input")
                .style("--grid-column", "3")
                .style("--grid-row", "1")
                .attr("type", "number")
                .attr("step", "any")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.lsl.toFixed(x.precision))
                .on("change", (e, x) => {
                    x.lsl = parseFloat(e.srcElement.value);
                });
            items.append("input")
                .style("--grid-column", "4")
                .style("--grid-row", "1")
                .attr("type", "number")
                .attr("step", "1")
                .attr("max", "6")
                .attr("min", "0")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.precision)
                .on("change", (e, x) => {
                    x.precision = parseInt(e.srcElement.value);
                    nominal.property("value", x.nominal.toFixed(x.precision));
                    usl.property("value", x.usl.toFixed(x.precision));
                    lsl.property("value", x.lsl.toFixed(x.precision));
                });
            items.append("input")
                .style("--grid-column", "5")
                .style("--grid-row", "1")
                .attr("type", "date")
                .attr("class", "list-item-input-dark")
                .property("value", (x) => x.date_implemented)
                .on("change", (e, x) => {
                    x.date_implemented = e.srcElement.value;
                });
            let deviations = items.append("select")
                .style("--grid-column", "6")
                .style("--grid-row", "1")
                .attr("class", "list-item-select-dark");
            let employees = items.append("select")
                .style("--grid-column", "7")
                .style("--grid-row", "1")
                .style("border-radius", "0px 6px 6px 0px")
                .attr("class", "list-item-select-dark");

            // populate the deviations select
            deviations.selectAll("option")
                .data(json.response.deviations)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // set the deviations select value
            deviations.property("value", (x) => x.deviation_type_id)
                .on("change", (e, x) => {
                    x.deviation_type_id = parseInt(e.srcElement.value);
                });

            // populate the employees select
            employees.selectAll("option")
                .data(json.response.employees)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // set the employees select value
            employees.property("value", (x) => x.employee_id)
                .on("change", (e, x) => {
                    x.employee_id = parseInt(e.srcElement.value);
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
