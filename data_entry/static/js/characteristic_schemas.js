
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const main_schema_table = d3.select("#main_schema_table");
const schema_table_context_menu = document.getElementById("schema_context_menu");
const schema_table_scope = document.querySelector("#main_schema_table");

// inspection_reports
const sc_button_create = d3.select("#schemas_create_new_btn");
const sc_button_add_row = d3.select("#schemas_add_row_btn");
const sc_button_remove_row = d3.select("#schemas_remove_row_btn");
const sc_input_new_part_filter = d3.select("#schemas_part_filter");
const sc_select_new_part = d3.select("#schemas_part");
const sc_input_schema_filter = d3.select("#schemas_search_term");
const sc_select_locked_status = d3.select("#schemas_is_locked");
const sc_ul_list = d3.select("#schemas_filtered_list");

// enumerations
var specification_types = null;
var characteristic_types = null;
var frequency_types = null;
var gauge_types = null;
var current_schema_id = null;

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
    // retrieve lists
    retrieve_global_enumerations();

    // populate selectors
    populate_generic_selectors();

    // schema view table
    setup_context_menus();

    // panels
    prepare_schema_panel();

}

function retrieve_global_enumerations()
{
    // characteristic types
    d3.json("/get_all_characteristic_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok_func") {
            characteristic_types = json.response;
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

    // frequency types
    d3.json("/get_all_frequency_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok_func") {
            frequency_types = json.response;
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

    // specification types
    d3.json("/get_all_specification_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok_func") {
            specification_types = json.response;
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

    // gauge types
    d3.json("/get_all_gauge_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok_func") {
            gauge_types = json.response;
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

function setup_context_menus()
{
    schema_table_scope.addEventListener("contextmenu", (e) => {
        if (e.target.tagName != "TH") {
            e.preventDefault();
            const { clientX: mouseX, clientY: mouseY } = e;
            schema_table_context_menu.style.top = `${mouseY}px`;
            schema_table_context_menu.style.left = `${mouseX}px`;
            schema_table_context_menu.classList.add("visible");

            // requery the database
            d3.select("#context_menu_0").on("click", () => {
                let schema_id = main_schema_table.select("tbody").selectAll("tr").data()[0].schema_id;
                get_selected_schema(schema_id);
                schema_table_context_menu.classList.remove("visible");
            });

            // lock the schema
            d3.select("#context_menu_1").on("click", () => {
                schema_lock();
                schema_table_context_menu.classList.remove("visible");
            });

            // save the schema
            d3.select("#context_menu_2").on("click", () => {
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
}

function prepare_schema_panel()
{
    // input events
    sc_input_new_part_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            schemas_update_part_id_select();
        }
    });
    sc_input_schema_filter.on("keydown", (x) => {
        if (x.keyCode == 13) {
            update_filtered_schemas();
        }
    });

    // select events
    sc_select_locked_status.on("change", update_filtered_schemas);
    sc_button_create.on("click", schemas_create_new_schema);
    sc_button_add_row.on("click", schemas_add_row);
    sc_button_remove_row.on("click", schemas_remove_row);
}

function populate_generic_selectors()
{
    // schemas
    schemas_update_part_id_select();
}

// #endregion

// #region schemas

function schemas_create_new_schema()
{
    // query the flask server
    d3.json("/characteristic_schemas/create_new_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            part_id: sc_select_new_part.property("value"),
            search_term: sc_input_schema_filter.property("value"),
            locked_status: sc_select_locked_status.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_add_row()
{
    // logic gate
    if (main_schema_table.select("tbody").selectAll("tr").data().length == 0) {
        return;
    }

    // get the current data array
    let current_data = main_schema_table.select("tbody").selectAll("tr").data();

    // get the current part id
    let schema_id = current_data[0].schema_id;

    // create placeholder data
    let placeholder_data = {
        detail_id: -1,
        schema_id: schema_id,
        name: "DIM x",
        nominal: 0,
        usl: 0,
        lsl: 0,
        precision: 1,
        specification_type_id: 0,
        characteristic_type_id: 0,
        frequency_type_id: 0,
        gauge_type_id: 0
    };

    // query the flask server
    d3.json("/characteristic_schemas/add_row/", {
        method: "POST",
        body: JSON.stringify({
            locked_status: current_data[0].is_locked,
            data: placeholder_data
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // update the detail id
            placeholder_data.detail_id = json.response;

            // append placeholder data to current data
            current_data.push(placeholder_data);

            // update the table
            update_table(current_data);
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

function schemas_remove_row()
{
    // logic gate
    if (main_schema_table.select("tbody").selectAll("tr").data().length == 0) {
        return;
    }
    else if (main_schema_table.select("tbody").selectAll("tr").data().length == 1) {
        let schema_id = main_schema_table.select("tbody").selectAll("tr").data().slice(-1)[0].schema_id;
        delete_schema(schema_id);
        return;
    }

    // request confirmation
    if (!confirm("This action will delete information from the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the last row
    let last_row = main_schema_table.select("tbody").selectAll("tr").data().slice(-1)[0];

    // query the flask server
    d3.json("/characteristic_schemas/remove_row/", {
        method: "POST",
        body: JSON.stringify({
            locked_status: last_row.is_locked,
            detail_id: last_row.detail_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {
            main_schema_table.select("tbody").selectAll("tr:last-child").remove();
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
    get_selected_schema(data.schema_id);
}

function update_filtered_schemas()
{
    // get the inputs
    let search_term = sc_input_schema_filter.property("value");
    let locked_status = sc_select_locked_status.property("value");

    // query the flask server
    d3.json("/characteristic_schemas/get_filtered_characteristic_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: search_term,
            locked_status: locked_status
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {
            populate_schema_list(json.response);
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

function populate_schema_list(data)
{
    // clear the old entries
    sc_ul_list.selectAll("li").remove();

    // populate the inspection reports list
    let items = sc_ul_list.selectAll("li")
        .data(data)
        .enter()
        .append("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "2fr 2fr 1fr 2fr 1fr");
    items.append("label")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("text-align", "center")
        .style("border-radius", "6px 0px 0px 6px")
        .attr("class", "list-item-label-dark")
        .text((x) => x.item)
        .on("click", (_, d) => schema_selected(d));
    items.append("label")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .style("text-align", "center")
        .attr("class", "list-item-label-dark")
        .text((x) => x.drawing)
        .on("click", (_, d) => schema_selected(d));
    items.append("label")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .style("text-align", "center")
        .attr("class", "list-item-label-dark")
        .text((x) => x.revision)
        .on("click", (_, d) => schema_selected(d));
    items.append("label")
        .style("--grid-column", "4")
        .style("--grid-row", "1")
        .style("text-align", "center")
        .attr("class", "list-item-label-dark")
        .text((x) => {
            switch (x.is_locked) {
                case true:
                    return "Locked";
                case false:
                    return "Unlocked";
            }
        })
        .on("click", (_, d) => schema_selected(d));
    items.append("button")
        .style("--grid-column", "5")
        .style("--grid-row", "1")
        .style("text-align", "center")
        .style("border-radius", "0px 6px 6px 0px")
        .attr("class", "list-item-button-dark")
        .text("Delete")
        .on("click", (_, d) => delete_schema(d.schema_id));
}

function delete_schema(schema_id)
{
    // get the required parameters
    let locked_status = sc_select_locked_status.property("value");
    let search_term = sc_input_schema_filter.property("value");

    // query the flask server
    d3.json("/characteristic_schemas/delete_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id,
            search_term: search_term,
            locked_status: locked_status
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // repopulate the schema list
            populate_schema_list(json.response);

            // clear the characteristic table
            main_schema_table.select("thead").remove();
            main_schema_table.select("tbody").remove();
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

function schemas_update_part_id_select()
{
    d3.json("/characteristic_schemas/get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            search_term: sc_input_new_part_filter.property("value"),
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // clear the old entries
            sc_select_new_part.selectAll("option").remove();

            // populate the part selector
            sc_select_new_part.selectAll("option")
                .data(json.response)
                .enter()
                .append("option")
                .attr("value", (x) => x.id)
                .text((x) => x.part_name);
            sc_select_new_part.property("value", json.response[0].id)
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

// #region view

function get_selected_schema(schema_id)
{
    // query the flask server
    d3.json("/characteristic_schemas/get_current_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok_func") {

            // update the view table
            update_table(json.response);
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

function enforce_precision(precision, detail_id)
{
    main_schema_table.select("tbody").selectAll("td").selectAll("input")
        .property("value", (x) => {
            if (x.column.datatype == "decimal" && x.row.detail_id == detail_id) {
                return x.row.value.toFixed(precision);
            }
        });
}

function update_table(data)
{
    // clear the old columns
    main_schema_table.selectAll("thead").remove();

    // add the columns
    main_schema_table.append("thead")
        .selectAll("tr")
        .data(table_columns)
        .join("th")
        .attr("scope", "col")
        .text((x) => x.display);

    // clear the old rows
    main_schema_table.selectAll("tbody").remove();

    // add the rows
    let rows = main_schema_table.append("tbody")
        .selectAll("tr")
        .data(data)
        .join("tr");

    // create the cells
    let cells = rows.selectAll("td")
        .data((r) => {
            return table_columns.map((c) => {
                return {
                    column: c,
                    row: {
                        value: r[c.key],
                        precision: r.precision,
                        schema_id: r.schema_id,
                        is_locked: r.is_locked,
                        detail_id: r.detail_id
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
        .attr("type", (x) => {
            if (x.column.datatype == "string") {
                return "text";
            }
            else {
                return "number";
            }
        })
        .property("value", (x) => {
            if (x.column.datatype == "decimal") {
                return x.row.value.toFixed(x.row.precision);
            }
            else {
                return x.row.value;
            }
        })
        .property("disabled", (x) => x.row.is_locked)
        .on("change", (e, x) => {
            x.row.value = parseFloat(e.srcElement.value);
            if (x.column.key == "precision") {
                enforce_precision(x.row.value, x.row.detail_id);
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
        .data(specification_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.type == "select" && x.column.key == "specification_type_id") {
                return true;
            }
        })
        .selectAll("select")
        .property("value", (x) => x.row.value)
        .property("disabled", (x) => x.row.is_locked)
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
        .data(characteristic_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.type == "select" && x.column.key == "characteristic_type_id") {
                return true;
            }
        })
        .selectAll("select")
        .property("value", (x) => x.row.value)
        .property("disabled", (x) => x.row.is_locked)
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
        .data(frequency_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.type == "select" && x.column.key == "frequency_type_id") {
                return true;
            }
        })
        .selectAll("select")
        .property("value", (x) => x.row.value)
        .property("disabled", (x) => x.row.is_locked)
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
        .data(gauge_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.type == "select" && x.column.key == "gauge_type_id") {
                return true;
            }
        })
        .selectAll("select")
        .property("value", (x) => x.row.value)
        .property("disabled", (x) => x.row.is_locked)
        .on("change", (e, x) => {
            x.row.value = parseInt(e.srcElement.value);
        });
}

function schema_save()
{
    // request confirmation
    if (!confirm("This action will modify information in the database and cannot be reverted. Continue?")) {
        return;
    }

    // declare the table's data
    let table_data = main_schema_table.select("tbody").selectAll("td").data();

    // get required parameters
    let schema_id = table_data[0].row.schema_id;

    // build the data object
    let data = [];
    table_data.forEach(element => {
        if (data.some((e) => e.detail_id == element.row.detail_id)) {
            data.filter((e) => e.detail_id == element.row.detail_id)[0]
                .contents.push({
                    key: element.column.key,
                    value: element.row.value
                });
        }
        else {
            data.push({
                detail_id: element.row.detail_id,
                contents: [{
                    key: element.column.key,
                    value: element.row.value
                }]
            });
        }
    });

    // query the flask server
    d3.json("/characteristic_schemas/save_current_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id,
            data: data
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

function schema_lock()
{
    // request confirmation
    if (!confirm("This action will modify information in the database and cannot be reverted. Continue?")) {
        return;
    }

    // declare the table's data
    let table_data = main_schema_table.select("tbody").selectAll("td").data();

    // get required parameters
    let schema_id = table_data[0].row.schema_id;

    // query the flask server
    d3.json("/characteristic_schemas/lock_schema/", {
        method: "POST",
        body: JSON.stringify({
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

// #endregion

// #region sidebar control

function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "schemas") {
        if (document.getElementById("schemas_sidebar").style.width == open_width) {
            document.getElementById("schemas_sidebar").style.width = close_width;
            document.getElementById("schemas_btn").style.marginRight = close_width;
        }
        else {
            document.getElementById("schemas_sidebar").style.width = open_width;
            document.getElementById("schemas_btn").style.marginRight = open_width;
            update_filtered_schemas();
        }
    }
}

//#endregion
