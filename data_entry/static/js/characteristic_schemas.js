
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const main_schema_table = d3.select("#main_schema_table");
const schema_table_context_menu = document.getElementById("schema_context_menu");
const schema_table_scope = document.querySelector("#main_schema_table");

// inspection_reports
const sc_button_create = d3.select("#schemas_create_new_btn");
const sc_input_new_item_filter = d3.select("#schemas_item_filter");
const sc_select_new_item = d3.select("#schemas_item");
const sc_input_new_drawing_filter = d3.select("#schemas_drawing_filter");
const sc_select_new_drawing = d3.select("#schemas_drawing");
const sc_input_schema_filter = d3.select("#schemas_search_term");
const sc_ul_list = d3.select("#schemas_filtered_list");

// main schema table columns
const table_columns = [
    { display: "Name",                  key: "name",                    type: "input", datatype: "string"},
    { display: "Nominal",               key: "nominal",                 type: "input", datatype: "decimal"},
    { display: "USL",                   key: "usl",                     type: "input", datatype: "decimal"},
    { display: "LSL",                   key: "lsl",                     type: "input", datatype: "decimal"},
    { display: "Precision",             key: "precision",               type: "input", datatype: "integer"},
    { display: "Specification Type",    key: "specification_type_id",   type: "select", datatype: "integer"},
    { display: "Characteristic Type",   key: "characteristic_type_id",  type: "select", datatype: "integer"},
    { display: "Frequency Type",        key: "frequency_type_id",       type: "select", datatype: "integer"},
    { display: "Gauge Type",            key: "gauge_type_id",           type: "select", datatype: "integer"}
];

init();

// #region page initialization

function init()
{
    // populate selectors
    populate_generic_selectors();

    // characteristic table
    schema_table_scope.addEventListener("contextmenu", (e) => {
        if (e.target.tagName != "TH") {
            e.preventDefault();
            const { clientX: mouseX, clientY: mouseY } = e;
            schema_table_context_menu.style.top = `${mouseY}px`;
            schema_table_context_menu.style.left = `${mouseX}px`;
            schema_table_context_menu.classList.add("visible");

            // requery the database
            d3.select("#context_menu_1").on("click", () => {
                
                schema_table_context_menu.classList.remove("visible");
            });

            // lock the schema
            d3.select("#context_menu_2").on("click", () => {
                
                schema_table_context_menu.classList.remove("visible");
            });

            // save the schema
            d3.select("#context_menu_3").on("click", () => {
                schema_save();
                schema_table_context_menu.classList.remove("visible");
            });
        }
    });
    schema_table_scope.addEventListener("click", (e) => {
        if (e.target.offsetParent != schema_table_context_menu) {
            schema_table_context_menu.classList.remove("visible");
        }
    });

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
    sc_button_create.on("click", schema_create_new);
    sc_select_new_item.on("change", schemas_item_number_changed);
    sc_select_new_drawing.on("change", schemas_drawing_changed);
}

function populate_generic_selectors()
{
    // schemas
    update_new_schema_selectors();
}

// #endregion

// #region schemas

function schema_create_new()
{
    // query the flask server
    d3.json("/characteristic_schemas/create_new_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            part_id: 0
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

function schema_save()
{
    // confirm the identity parameter
    let part_id = ir_select_new_item.property("value");
    let schema_id = ir_select_char_schema.property("value");

    // query the flask server
    d3.json("/characteristic_schemas/save_current_characteristic_schema/", {
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

function schema_selected(data)
{
    // update the main display
    navbar_info.text(`${data.item} // ${data.drawing} // ${data.revision}`);

    // characteristic display
    get_selected_schema(data.part_id);
}

function update_filtered_schemas()
{
    // get the inputs
    let search_term = sc_input_schema_filter.property("value");

    // query the flask server
    d3.json("/characteristic_schemas/get_filtered_characteristic_schemas/", {
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
            sc_ul_list.selectAll("li").remove();

            // populate the inspection reports list
            let items = sc_ul_list.selectAll("li")
                .data(json.response)
                .enter()
                .append("li")
                .append("div")
                .attr("class", "list-item-dark")
                .style("--grid-template-columns", "1fr 1fr 1fr")
                .on("click", (_, d) => schema_selected(d));
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
                .text((x) => x.revision);
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

// #region schema view

function get_selected_schema(part_id)
{
    // query the flask server
    d3.json("/characteristic_schemas/get_current_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            part_id: part_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old columns
            main_schema_table.selectAll("thead").remove();

            // add the columns
            main_schema_table.append("thead")
                .selectAll("tr")
                .data(table_columns)
                .enter()
                .append("th")
                .attr("scope", "col")
                .text((x) => x.display);

            // clear the old rows
            main_schema_table.selectAll("tbody").remove();

            // add the rows
            let rows = main_schema_table.append("tbody")
                .selectAll("tr")
                .data(json.response.data)
                .enter()
                .append("tr");

            // create the cells
            let cells = rows.selectAll("td")
                .data((r) => {
                    return table_columns.map((c) => {
                        return {
                            column: c,
                            row: {
                                value: r[c.key],
                                precision: r.precision,
                                schema_id: r.schema_id
                            }
                        };
                    });
                })
                .enter()
                .append("td");

            // assign inputs
            cells.filter((x) => {
                    if (x.column.type == "input") {
                        return true;
                    }
                })
                .insert("input")
                .attr("class", "data-table-cell-dark")
                .property("value", (x) => {
                    if (x.column.datatype == "decimal") {
                        return x.row.value.toFixed(x.row.precision);
                    }
                    else {
                        return x.row.value;
                    }
                }).on("change", (e, x) => {
                    x.row.value = parseFloat(e.srcElement.value);
                    if (x.column.key == "precision") {
                        enforce_precision(x.row.value, x.row.schema_id);
                    }
                });

            // specification types
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "specification_type_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
                .selectAll("option")
                .data(json.response.specification_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "specification_type_id") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value)
                .on("change", (e, x) => {
                    x.row.value = parseInt(e.srcElement.value);
                });

            // characteristic types
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "characteristic_type_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
                .selectAll("option")
                .data(json.response.characteristic_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "characteristic_type_id") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value)
                .on("change", (e, x) => {
                    x.row.value = parseInt(e.srcElement.value);
                });

            // frequency types
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "frequency_type_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
                .selectAll("option")
                .data(json.response.frequency_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "frequency_type_id") {
                        return true;
                    }
                })
                .selectAll("select")
                .property("value", (x) => x.row.value)
                .on("change", (e, x) => {
                    x.row.value = parseInt(e.srcElement.value);
                });

            // gauge types
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "gauge_type_id") {
                        return true;
                    }
                })
                .insert("select")
                .attr("class", "data-table-cell-dark")
                .selectAll("option")
                .data(json.response.gauge_types)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
            cells.filter((x) => {
                    if (x.column.type == "select" && x.column.key == "gauge_type_id") {
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

function enforce_precision(precision, schema_id)
{
    main_schema_table.select("tbody").selectAll("td").selectAll("input")
        .property("value", (x) => {
            if (x.column.datatype == "decimal" && x.row.schema_id == schema_id) {
                return x.row.value.toFixed(precision);
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
            update_filtered_schemas();
        }
    }
}

//#endregion
