
// navbar
const navbar_info = d3.select("#navbar_info");

// schema view
const vw_characteristics_table = d3.select("#schema_view_characteristics_table");
const vw_characteristics_table_contextmenu = d3.select("#schema_view_characteristics_table_contextmenu");

// schemas panel
const sc_button_create = d3.select("#schemas_create_new_btn");
const sc_button_add_row = d3.select("#schemas_add_row_btn");
const sc_button_remove_row = d3.select("#schemas_remove_row_btn");
const sc_input_new_part_filter = d3.select("#schemas_part_filter");
const sc_select_new_part = d3.select("#schemas_part");
const sc_input_schema_filter = d3.select("#schemas_search_term");
const sc_select_is_locked = d3.select("#schemas_is_locked");
const sc_ul_list = d3.select("#schemas_filtered_list");
const sc_ul_list_contextmenu = d3.select("#schemas_filtered_list_contextmenu");

// enumerations
var specification_types = null;
var characteristic_types = null;
var frequency_types = null;
var gauge_types = null;

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

    // panels
    prepare_schema_panel();

    // schema view table
    setup_context_menus();
}

function retrieve_global_enumerations()
{
    // characteristic types
    d3.json("/get_all_characteristic_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            characteristic_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // frequency types
    d3.json("/get_all_frequency_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            frequency_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // specification types
    d3.json("/get_all_specification_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            specification_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // gauge types
    d3.json("/get_all_gauge_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            gauge_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function setup_context_menus()
{
    // open the schema characteristic view context menu
    vw_characteristics_table.on("contextmenu", (e) => {
        
        // extract data
        let row_data = e.target.__data__.row;

        // position and show the context menu
        vw_characteristics_table_contextmenu.style("position", "absolute")
            .style("left", `${e.pageX}px`)
            .style("top", `${e.pageY}px`)
            .style("display", "block");

        // reload schema
        vw_characteristics_table_contextmenu.select("#context_menu_0").on("click", () => {
            view_get_schema_characteristics(row_data.schema_id);
            vw_characteristics_table_contextmenu.style("display", "none");
        });

        // prevent the default behavior
        e.preventDefault();
    });
    vw_characteristics_table.on("click", () => {
        if (vw_characteristics_table_contextmenu.style("display") == "block") {
            vw_characteristics_table_contextmenu.style("display", "none");
        }
    });

    // open the schema list context menu
    sc_ul_list.on("contextmenu", (e) => {

        // extract the data
        let row_data = e.target.__data__;

        // position and show the context menu
        sc_ul_list_contextmenu.style("position", "absolute")
            .style("left", `${e.pageX}px`)
            .style("top", `${e.pageY}px`)
            .style("display", "block");

        // toggle locked status
        sc_ul_list_contextmenu.select("#context_menu_0").on("click", () => {
            schemas_toggle_lock(row_data.schema_id);
            sc_ul_list_contextmenu.style("display", "none");
        });

        // save schema
        sc_ul_list_contextmenu.select("#context_menu_1").on("click", () => {
            schemas_save(row_data.schema_id);
            sc_ul_list_contextmenu.style("display", "none");
        });

        // delete schema
        sc_ul_list_contextmenu.select("#context_menu_2").on("click", () => {
            schemas_delete(row_data.schema_id);
            sc_ul_list_contextmenu.style("display", "none");
        });

        // prevent the default behavior
        e.preventDefault();
    });
    sc_ul_list.on("click", () => {
        if (sc_ul_list_contextmenu.style("display") == "block") {
            sc_ul_list_contextmenu.style("display", "none");
        }
    });
}

function prepare_schema_panel()
{
    // input events
    sc_input_new_part_filter.on("change", schemas_update_part_id_selector);
    sc_input_schema_filter.on("change", schemas_update_filtered_schemas);

    // select events
    sc_select_is_locked.on("change", schemas_update_filtered_schemas);
    sc_button_create.on("click", schemas_create_new_schema);
    sc_button_add_row.on("click", schemas_add_row);
    sc_button_remove_row.on("click", schemas_remove_row);
}

function populate_generic_selectors()
{
    // schemas
    schemas_update_part_id_selector();
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
            is_locked: sc_select_is_locked.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // repopulate the schema view
            view_repopulate_schema_characteristics_table([json.response.schema_characteristics]);

            // repopulate the schema list
            schemas_repopulate_schema_list(json.response.schema_list);
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
    if (vw_characteristics_table.select("tbody").selectAll("tr").data().length == 0) {
        return;
    }

    // get the current data array
    let current_data = vw_characteristics_table.select("tbody").selectAll("tr").data();

    // query the flask server
    d3.json("/characteristic_schemas/add_row/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: current_data[0].schema_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // get the required information
            let new_data = json.response;

            // append new data to current data
            current_data.push({
                schema_id: new_data.schema_id,
                is_locked: current_data[0].is_locked,
                part_id: current_data[0].part_id,
                detail_id: new_data.id,
                name: new_data.name,
                nominal: new_data.nominal,
                usl: new_data.usl,
                lsl: new_data.lsl,
                precision: new_data.precision,
                specification_type_id: new_data.specification_type_id,
                characteristic_type_id: new_data.characteristic_type_id,
                frequency_type_id: new_data.frequency_type_id,
                gauge_type_id: new_data.gauge_type_id
            });

            // update the table
            view_repopulate_schema_characteristics_table(current_data);
        }
        else if (json.status == "log") {
            alert(json.response);
        }
        else if (json.status == "alert") {
            console.log(json.response);
        }
    });
}

function schemas_remove_row()
{
    // logic gate
    if (vw_characteristics_table.select("tbody").selectAll("tr").data().length == 0) {
        return;
    }
    else if (vw_characteristics_table.select("tbody").selectAll("tr").data().length == 1) {
        schemas_delete(vw_characteristics_table.select("tbody").selectAll("tr").data()[0].schema_id);
        return;
    }

    // request confirmation
    if (!confirm("This action will delete information from the database and cannot be reverted. Continue?")) {
        return;
    }

    // get the last row
    let last_row = vw_characteristics_table.select("tbody").selectAll("tr").data().slice(-1)[0];

    // query the flask server
    d3.json("/characteristic_schemas/remove_row/", {
        method: "POST",
        body: JSON.stringify({
            is_locked: last_row.is_locked,
            detail_id: last_row.detail_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            vw_characteristics_table.select("tbody").selectAll("tr:last-child").remove();
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_toggle_lock(schema_id)
{
    // query the flask server
    d3.json("/characteristic_schemas/toggle_lock_schema/", {
        method: "POST",
        body: JSON.stringify({
            search_term: sc_input_schema_filter.property("value"),
            is_locked: sc_select_is_locked.property("value"),
            schema_id: schema_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // convert current data to reflect locked status
            let current_data = vw_characteristics_table.select("tbody").selectAll("tr").data();
            current_data.forEach(element => {
                element.is_locked = json.response.is_locked;
            });

            // repopulate the schema view
            view_repopulate_schema_characteristics_table(current_data);

            // repopulate the schema list
            schemas_repopulate_schema_list(json.response.schema_list);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_save(schema_id)
{
    // request confirmation
    if (!confirm("This action will modify information in the database and cannot be reverted. Continue?")) {
        return;
    }

    // build the data object
    let data = [];
    vw_characteristics_table.select("tbody").selectAll("td").data().forEach(element => {
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
    d3.json("/characteristic_schemas/save_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id,
            data: data
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

function schemas_delete(schema_id)
{
    // request confirmation
    if (!confirm("This action will modify information in the database and cannot be reverted. Continue?")) {
        return;
    }

    d3.json("/characteristic_schemas/delete_characteristic_schema/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id,
            search_term: sc_input_schema_filter.property("value"),
            is_locked: sc_select_is_locked.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // repopulate the schema list
            schemas_repopulate_schema_list(json.response);

            // clear the characteristic table
            vw_characteristics_table.select("thead").remove();
            vw_characteristics_table.select("tbody").remove();
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_update_filtered_schemas()
{
    d3.json("/characteristic_schemas/get_filtered_characteristic_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: sc_input_schema_filter.property("value"),
            is_locked: sc_select_is_locked.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // populate the schema list
            schemas_repopulate_schema_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_schema_selected(data)
{
    // update the main display
    navbar_info.text(`${data.item} // ${data.drawing} // ${data.revision}`);

    // characteristic display
    view_get_schema_characteristics(data.schema_id);
}

function schemas_update_part_id_selector()
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
        if (json.status == "ok") {

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
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function schemas_repopulate_schema_list(data)
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
        .style("--grid-template-columns", "1fr 1fr 1fr");
    items.append("label")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px 0px 0px 6px")
        .attr("class", "list-item-label-dark")
        .text((x) => {
            if (x.is_locked) {
                return `**${x.item}`;
            }
            else {
                return x.item;
            }
        })
        .on("click", (_, d) => schemas_schema_selected(d));
    items.append("label")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("class", "list-item-label-dark")
        .text((x) => x.drawing)
        .on("click", (_, d) => schemas_schema_selected(d));
    items.append("label")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("class", "list-item-label-dark")
        .text((x) => x.revision)
        .on("click", (_, d) => schemas_schema_selected(d));
}

// #endregion

// #region view

function view_get_schema_characteristics(schema_id)
{
    // query the flask server
    d3.json("/characteristic_schemas/get_schema_characteristics/", {
        method: "POST",
        body: JSON.stringify({
            schema_id: schema_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // update the view table
            view_repopulate_schema_characteristics_table(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

function view_repopulate_schema_characteristics_table(data)
{
    // clear the old columns
    vw_characteristics_table.selectAll("thead").remove();

    // add the columns
    vw_characteristics_table.append("thead")
        .selectAll("tr")
        .data(table_columns)
        .join("th")
        .attr("scope", "col")
        .text((x) => x.display);

    // clear the old rows
    vw_characteristics_table.selectAll("tbody").remove();

    // add the rows
    let rows = vw_characteristics_table.append("tbody")
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

function enforce_precision(precision, detail_id)
{
    vw_characteristics_table.select("tbody").selectAll("td").selectAll("input")
        .property("value", (x) => {
            if (x.column.datatype == "decimal" && x.row.detail_id == detail_id) {
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
            document.getElementById("schemas_btn").style.marginRight = close_width;
        }
        else {
            document.getElementById("schemas_sidebar").style.width = open_width;
            document.getElementById("schemas_btn").style.marginRight = open_width;
            schemas_update_filtered_schemas();
        }
    }
}

//#endregion
