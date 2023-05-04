
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const main_characteristic_table = d3.select("#main_char_table");
const char_table_context_menu = document.getElementById("char_context_menu");
const char_table_scope = document.querySelector("#main_char_table");

// inspection_reports
const sc_button_create = d3.select("#schemas_create_new_btn");
const sc_input_new_item_filter = d3.select("#schemas_item_filter");
const sc_select_new_item = d3.select("#schemas_item");
const sc_input_new_drawing_filter = d3.select("#schemas_drawing_filter");
const sc_select_new_drawing = d3.select("#schemas_drawing");
const sc_input_schema_filter = d3.select("#schemas_search_term");
const sc_ul_list = d3.select("#schemas_filtered_list");

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

    // // characteristic table
    // char_table_scope.addEventListener("contextmenu", (e) => {
    //     if (e.target.tagName != "TH") {
    //         e.preventDefault();
    //         const { clientX: mouseX, clientY: mouseY } = e;
    //         char_table_context_menu.style.top = `${mouseY}px`;
    //         char_table_context_menu.style.left = `${mouseX}px`;
    //         char_table_context_menu.classList.add("visible");

    //         // tunnel to physical part
    //         d3.select("#context_menu_0").on("click", () => {
    //             cd_select_part_index.property("value", e.target.__data__.row.part_index);
    //             get_filtered_characteristics();
    //             char_table_context_menu.classList.remove("visible");
    //         });

    //         // requery the database
    //         d3.select("#context_menu_1").on("click", () => {
    //             get_filtered_characteristics();
    //             char_table_context_menu.classList.remove("visible");
    //         });

    //         // view the associated deviations
    //         d3.select("#context_menu_2").on("click", () => {
    //             if (e.target.__data__.row.has_deviations) {
    //                 populate_deviations(e.target.__data__.row.characteristic_id);
    //                 toggle_options("deviations", "1000px");
    //             }
    //             char_table_context_menu.classList.remove("visible");
    //         });

    //         // save the characteristics
    //         d3.select("#context_menu_3").on("click", () => {
    //             submit_current_characteristics();
    //             char_table_context_menu.classList.remove("visible");
    //         });
    //     }
    // });
    // char_table_scope.addEventListener("click", (e) => {
    //     if (e.target.offsetParent != char_table_context_menu) {
    //         char_table_context_menu.classList.remove("visible");
    //     }
    // });

    // inspection reports
    sc_input_new_item_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_new_schema_selectors();
        }
    });
    sc_input_new_drawing_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_new_schema_selectors();
        }
    });
    sc_input_schema_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_schemas();
        }
    });
    sc_button_create.on("click", inspection_report_create_new);
    sc_select_new_item.on("change", schemas_item_number_changed);
    sc_select_new_drawing.on("change", schemas_drawing_changed);
    sc_select_char_schema.on("change", update_characteristic_schema_selector);
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
    update_new_schema_selectors();
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
            update_filtered_schemas();
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

function update_filtered_schemas()
{
    // get the inputs
    let search_term = sc_input_schema_filter.property("value");

    // query the flask server
    d3.json("/data_entry/get_filtered_characteristic_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term
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

function schemas_item_number_changed()
{
    sc_select_new_drawing.property("value", sc_select_new_item.property("value"));
}

function schemas_drawing_changed()
{
    sc_select_new_item.property("value", sc_select_new_drawing.property("value"));
}

function update_new_schema_selectors()
{
    // query the flask server
    d3.json("/data_entry/get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            item: sc_input_new_item_filter.property("value"),
            drawing: sc_input_new_drawing_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            sc_select_new_item.selectAll("option").remove();
            sc_select_new_drawing.selectAll("option").remove();

            // populate the item numbers
            sc_select_new_item.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.item);
            sc_select_new_item.property("value", json.response[0].id)

            // populate the drawings
            sc_select_new_drawing.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.drawing);
            sc_select_new_drawing.property("value", json.response[0].id)
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
    if (destination_arg == "schemas") {
        if (document.getElementById("schemas_sidebar").style.width == open_width) {
            document.getElementById("schemas_sidebar").style.width = close_width;
            document.getElementById("schemas_btn").style.marginLeft = close_width;
        }
        else {
            document.getElementById("schemas_sidebar").style.width = open_width;
            document.getElementById("schemas_btn").style.marginLeft = open_width;
        }
    }
}

//#endregion
