
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const vw_measurements_table = d3.select("#measurements_table");
const vw_measurements_table_contextmenu = d3.select("#measurements_table_contextmenu");

// inspection_reports
const ir_button_new = d3.select("#inspection_reports_new");
const ir_button_refresh = d3.select("#inspection_reports_refresh");
const ir_input_filter_part = d3.select("#inspection_reports_part_filter");
const ir_select_part = d3.select("#inspection_reports_part");
const ir_input_filter_schema = d3.select("#inspection_reports_schema_filter");
const ir_select_schema = d3.select("#inspection_reports_schema");
const ir_input_filter_employee = d3.select("#inspection_reports_employee_filter");
const ir_select_employee = d3.select("#inspection_reports_employee");
const ir_input_list_filter_part = d3.select("#inspection_reports_list_filter_part");
const ir_input_list_filter_job_order = d3.select("#inspection_reports_list_filter_job_order");
const ir_input_started_after = d3.select("#inspection_reports_list_filter_start_after");
const ir_input_finished_before = d3.select("#inspection_reports_list_filter_finished_before");
const ir_ul_list = d3.select("#inspection_reports_filtered_list");
const ir_ul_list_contextmenu = d3.select("#inspection_reports_list_contextmenu");

// measurement sets
const ms_button_create_new_set = d3.select("#measurement_sets_add");
const ms_button_refresh_list = d3.select("#measurement_sets_refresh_list");
const ms_button_save_edits = d3.select("#measurement_sets_save");
const ms_input_schema_filter = d3.select("#measurement_sets_schema_filter");
const ms_select_schema = d3.select("#measurement_sets_schema");
const ms_input_employee_filter = d3.select("#measurement_sets_employee_filter");
const ms_select_employee = d3.select("#measurement_sets_employee");
const ms_input_display_filter = d3.select("#measurement_sets_display_filter");
const ms_ul_list = d3.select("#measurement_sets_list");
const ms_ul_list_contextmenu = d3.select("#measurement_sets_list_contextmenu");

// measurements
const mt_button_update_display = d3.select("#measurements_apply_filter");
const mt_button_save_characteristics = d3.select("#measurements_save_changes");
const mt_select_display_type = d3.select("#measurements_display_type");
const mt_select_measurement_type = d3.select("#measurements_measurement_type");
const mt_input_name = d3.select("#measurements_dimension_name");
const mt_select_frequency_type = d3.select("#measurements_frequency_type");
const mt_select_has_deviations = d3.select("#measurements_has_deviations");
const mt_select_inspector = d3.select("#measurements_inspector");
const mt_select_gauge = d3.select("#measurements_gauge");
const mt_select_gauge_type = d3.select("#measurements_gauge_type");
const mt_select_specification_type = d3.select("#measurements_specification_type");
const mt_select_dimension_type = d3.select("#measurements_dimension_type");
const mt_select_part_index = d3.select("#measurements_part_index");
const mt_select_revision = d3.select("#measurements_revision");

// metadata
const md_button_save = d3.select("#metadata_save");
const md_select_disposition = d3.select("#metadata_disposition");
const md_select_material_type = d3.select("#metadata_material_type");
const md_select_inspector = d3.select("#metadata_inspector");
const md_select_job_order = d3.select("#metadata_job_order");
const md_select_supplier = d3.select("#metadata_supplier");
const md_ul_list = d3.select("#metadata_quantity_list");

// receiver numbers
const rn_input_selected_search_term = d3.select("#receiver_numbers_selected_search_term");
const rn_select_selected = d3.select("#receiver_numbers_selected");
const rn_input_search_term = d3.select("#receiver_numbers_search_term");
const rn_button_add = d3.select("#receiver_numbers_add");
const rn_ul_list = d3.select("#receiver_numbers_list");

// purchase orders
const po_input_selected_search_term = d3.select("#purchase_orders_selected_search_term");
const po_select_selected = d3.select("#purchase_orders_selected");
const po_input_search_term = d3.select("#purchase_orders_search_term");
const po_button_add = d3.select("#purchase_orders_add");
const po_ul_list = d3.select("#purchase_orders_list");

// lot numbers
const ln_input_selected_search_term = d3.select("#lot_numbers_selected_search_term");
const ln_select_selected = d3.select("#lot_numbers_selected");
const ln_input_search_term = d3.select("#lot_numbers_search_term");
const ln_button_add = d3.select("#lot_numbers_add");
const ln_ul_list = d3.select("#lot_numbers_list");

// deviations
const dv_button_save = d3.select("#deviations_save_deviation");
const dv_button_add = d3.select("#deviations_add_deviation");
const dv_label_current = d3.select("#deviations_current_characteristic");
const dv_input_notes = d3.select("#deviations_notes");
const dv_ul_list = d3.select("#deviations_list");
const dv_ul_list_contextmenu = d3.select("#deviations_list_contextmenu");

// enumerations
var glist_employees = null;
var glist_gauge_ids = null;
var glist_deviations = null;
var glist_measurement_types = null;

// open panel
var open_panel = null;

// individual columns
const col_part_index =  { display: "Part Index",            key: "part_index",          type: "label",  datatype: "integer" };
const col_freqtype =    { display: "Frequency",             key: "frequency_type",      type: "label",  datatype: "integer" };
const col_revision =    { display: "Revision",              key: "revision",            type: "label",  datatype: "string" };
const col_name =        { display: "Name",                  key: "name",                type: "label",  datatype: "string" };
const col_nominal =     { display: "Nominal",               key: "nominal",             type: "label",  datatype: "decimal" };
const col_usl =         { display: "USL",                   key: "usl",                 type: "label",  datatype: "decimal" };
const col_lsl =         { display: "LSL",                   key: "lsl",                 type: "label",  datatype: "decimal" };
const col_measured =    { display: "Measured",              key: "measured",            type: "input",  datatype: "decimal" };
const col_gauge =       { display: "Gauge",                 key: "gauge_id",            type: "select", datatype: "integer" };
const col_gaugtype =    { display: "Gauge Type",            key: "gauge_type",          type: "label",  datatype: "integer" };
const col_spectype =    { display: "Specification Type",    key: "specification_type",  type: "label",  datatype: "integer" };
const col_dimetype =    { display: "Dimension Type",        key: "dimension_type",      type: "label",  datatype: "integer" };
const col_meastype =    { display: "Measurement Type",      key: "measurement_type",    type: "label",  datatype: "integer" };
const col_timestamp =   { display: "Timestamp",             key: "timestamp",           type: "label",  datatype: "string"  };

// main characteristic table columns
const main_table_columns = [
    [
        { col: col_name,        width: "125px" },
        { col: col_nominal,     width: "125px" },
        { col: col_usl,         width: "125px" },
        { col: col_lsl,         width: "125px" },
        { col: col_measured,    width: "50%" },
        { col: col_gauge,       width: "50%" }
    ],
    [
        { col: col_name,        width: "125px" },
        { col: col_freqtype,    width: "20%" },
        { col: col_gaugtype,    width: "20%" },
        { col: col_spectype,    width: "20%" },
        { col: col_dimetype,    width: "20%" },
        { col: col_meastype,    width: "20%" }
    ],
    [
        { col: col_part_index,  width: "100px" },
        { col: col_timestamp,   width: "150px" },
        { col: col_revision,    width: "100px" },
        { col: col_name,        width: "125px" },
        { col: col_nominal,     width: "125px" },
        { col: col_usl,         width: "125px" },
        { col: col_lsl,         width: "125px" },
        { col: col_measured,    width: "50%" },
        { col: col_gauge,       width: "50%" }
    ],
    [
        { col: col_part_index,  width: "100px" },
        { col: col_revision,    width: "100px" },
        { col: col_name,        width: "125px" },
        { col: col_freqtype,    width: "20%" },
        { col: col_gaugtype,    width: "20%" },
        { col: col_spectype,    width: "20%" },
        { col: col_dimetype,    width: "20%" },
        { col: col_meastype,    width: "20%" }
    ]
];

init();

// #region page initialization

async function init()
{
    // retrieve lists
    retrieve_global_enumerations();

    set_disabled_state(true);

    // panels
    await inspection_reports_prepare_panel();

    // close context menus
    d3.select("body").on("click", () => {
        if (ir_ul_list_contextmenu.style("display") == "block") {
            ir_ul_list_contextmenu.style("display", "none");
        }
        if (ms_ul_list_contextmenu.style("display") == "block") {
            ms_ul_list_contextmenu.style("display", "none");
        }
        if (vw_measurements_table_contextmenu.style("display") == "block") {
            vw_measurements_table_contextmenu.style("display", "none");
        }
        if (dv_ul_list_contextmenu.style("display") == "block") {
            dv_ul_list_contextmenu.style("display", "none");
        }
    });
}

function set_disabled_state(state)
{
    document.getElementById("measurement_sets_button").disabled = state;
    document.getElementById("measurements_button").disabled = state;
    document.getElementById("metadata_button").disabled = state;
    document.getElementById("receiver_numbers_button").disabled = state;
    document.getElementById("purchase_orders_button").disabled = state;
    document.getElementById("lot_numbers_button").disabled = state;
    document.getElementById("deviations_button").disabled = state;
}

function retrieve_global_enumerations()
{
    // employees
    d3.json("/get_all_employees/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_employees = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // gauges
    d3.json("/get_all_gauges/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_gauge_ids = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // deviation types
    d3.json("/get_all_deviation_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_deviations = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // measurement types
    d3.json("/get_all_measurement_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_measurement_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region inspection reports

async function inspection_reports_prepare_panel()
{
    // clear out the filters
    ir_input_filter_part.property("value", "");
    ir_input_filter_schema.property("value", "");
    ir_input_filter_employee.property("value", "");

    // populate the selectors
    await inspection_reports_update_part_selector();
    await inspection_reports_update_schema_selector();
    await inspection_reports_update_employee_selector();

    // set default values
    ir_input_started_after.property("value", "1970-01-01");
    ir_input_finished_before.property("value", "2100-01-01");

    // set up static input events
    ir_input_filter_part.on("change", async () => {
        await inspection_reports_update_part_selector();
        await inspection_reports_update_schema_selector();
    });
    ir_input_filter_schema.on("change", inspection_reports_update_schema_selector)
    ir_input_filter_employee.on("change", inspection_reports_update_employee_selector);
    ir_input_list_filter_part.on("change", inspection_reports_update_filtered_reports);
    ir_input_list_filter_job_order.on("change", inspection_reports_update_filtered_reports);
    ir_input_started_after.on("change", inspection_reports_update_filtered_reports);
    ir_input_finished_before.on("change", inspection_reports_update_filtered_reports);

    // set up static select events
    ir_select_part.on("change", inspection_reports_update_schema_selector);

    // set up static button events
    ir_button_new.on("click", inspection_reports_create_new_report);
    ir_button_refresh.on("click", inspection_reports_refresh_list);

    // populate the inspection report list
    await inspection_reports_update_filtered_reports();
}

async function inspection_reports_create_new_report()
{
    await d3.json("/inspection_reports/inspection_reports_create_new_report/", {
        method: "POST",
        body: JSON.stringify({
            part_id: ir_select_part.property("value"),
            schema_id: ir_select_schema.property("value"),
            employee_id: ir_select_employee.property("value"),
            part_search_term: ir_input_list_filter_part.property("value"),
            job_order_search_term: ir_input_list_filter_job_order.property("value"),
            started_after: ir_input_started_after.property("value"),
            finished_before: ir_input_finished_before.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            inspection_reports_repopulate_report_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_reports_refresh_list()
{
    // perform the unselect action
    await inspection_reports_report_unselected();

    // requery for the list of inspection reports
    await inspection_reports_update_filtered_reports();
}

async function inspection_reports_delete(inspection_id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/inspection_reports_delete/", {
        method: "POST",
        body: JSON.stringify({
            part_search_term: ir_input_list_filter_part.property("value"),
            job_order_search_term: ir_input_list_filter_job_order.property("value"),
            started_after: ir_input_started_after.property("value"),
            finished_before: ir_input_finished_before.property("value"),
            inspection_id: inspection_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the characteristic table
            vw_measurements_table.select("thead").selectAll("th").remove();
            vw_measurements_table.select("tbody").selectAll("td").remove();

            // repopulate the inspection report list
            inspection_reports_repopulate_report_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_reports_update_filtered_reports()
{
    await d3.json("/inspection_reports/inspection_reports_get_filtered_reports/", {
        method: "POST",
        body: JSON.stringify({
            part_search_term: ir_input_list_filter_part.property("value"),
            job_order_search_term: ir_input_list_filter_job_order.property("value"),
            started_after: ir_input_started_after.property("value"),
            finished_before: ir_input_finished_before.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // repopulate the inspection report list
            inspection_reports_repopulate_report_list(json.response);

            // set the unselected status
            navbar_info.text("");

            // lock the panels
            set_disabled_state(true);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_reports_repopulate_report_list(data)
{
    // clear the old entries
    ir_ul_list.selectAll("li").remove();

    // populate the inspection reports list
    let items = ir_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "1fr 1fr 1fr")
        .on("click", (e, x) => inspection_reports_report_clicked(e, x))
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            ir_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // delete inspection report
            ir_ul_list_contextmenu.select("#context_menu_0").on("click", async () => {
                await inspection_reports_delete(x.inspection_id);
                ir_ul_list_contextmenu.style("display", "none");
            });

            // prevent default behavior
            e.preventDefault();
        });
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

async function inspection_reports_report_clicked(event, data)
{
    // check if the item is already selected
    let is_selected = event.srcElement.parentNode.classList.contains("list-item-dark-selected");

    // reset/set the selected class
    for (let i = 0; i < ir_ul_list.node().childNodes.length; i++) {
        let current_node = ir_ul_list.node().childNodes[i].children[0];
        current_node.classList.remove("list-item-dark-selected");
    }

    // filter actions
    if (!is_selected) {
        await inspection_reports_report_selected(event, data);
    }
    else {
        await inspection_reports_report_unselected();
    }
}

async function inspection_reports_report_selected(event, data)
{
    // set the visual flags
    event.srcElement.parentNode.classList.add("list-item-dark-selected");
    navbar_info.text(`${data.item} // ${data.drawing}`);

    // unlock the panels
    set_disabled_state(false);

    // prepare the measurement sets
    await measurement_sets_prepare_panel(data.inspection_id, data.item, data.drawing);

    // populate the measurements
    await measurements_prepare_panel(data.inspection_id, data.item, data.drawing);    

    // populate the metadata
    await metadata_prepare_panel(data.inspection_id, data.item, data.drawing);

    // populate the receiver numbers
    await receiver_numbers_prepare_panel(data.inspection_id);

    // populate the purchase orders
    await purchase_orders_prepare_panel(data.inspection_id);

    // populate the lot numbers
    await lot_numbers_prepare_panel(data.inspection_id);
}

async function inspection_reports_report_unselected()
{
    // set the visual flags
    navbar_info.text("");

    // lock the panels
    set_disabled_state(true);

    // depopulate the measurement sets
    ms_button_create_new_set.on("click", null);
    ms_button_refresh_list.on("click", null);
    ms_input_schema_filter.on("change", null);
    ms_input_employee_filter.on("change", null);
    ms_input_schema_filter.property("value", "");
    ms_input_employee_filter.property("value", "");
    ms_input_display_filter.property("value", "");
    ms_select_schema.selectAll("option").remove();
    ms_select_employee.selectAll("option").remove();
    ms_ul_list.selectAll("li").remove();

    // depopulate the measurements
    vw_measurements_table.selectAll("thead").remove();
    vw_measurements_table.selectAll("tbody").remove();
}

async function inspection_reports_update_part_selector()
{
    await d3.json("/inspection_reports/inspection_reports_get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_filter_part.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ir_select_part.selectAll("option").remove();

            // populate the item numbers
            ir_select_part.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.part_name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_reports_update_schema_selector()
{
    await d3.json("/inspection_reports/inspection_reports_get_filtered_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_filter_part.property("value"),
            part_id: ir_select_part.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // account for possibly null returns
            if (json.response == null) {
                json.response = [
                    { schema_id: -1, name: "n/a" }
                ];
            }

            // clear the old entries
            ir_select_schema.selectAll("option").remove();

            // populate the item numbers
            ir_select_schema.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.schema_id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_reports_update_employee_selector()
{
    await d3.json("/inspection_reports/inspection_reports_get_filtered_employees/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_filter_employee.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ir_select_employee.selectAll("option").remove();

            // populate the item numbers
            ir_select_employee.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
                ir_select_employee.property("value", json.response[0].id)
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region measurement sets

async function measurement_sets_prepare_panel(inspection_id, item, drawing)
{
    // clear out filters
    ms_input_schema_filter.property("value", "");
    ms_input_employee_filter.property("value", "");

    // populate the selectors
    await measurement_sets_update_set_schemas(inspection_id);
    await measurement_sets_update_employees();

    // set up static input events
    ms_input_schema_filter.on("change", () => measurement_sets_update_set_schemas(inspection_id));
    ms_input_employee_filter.on("change", measurement_sets_update_employees);

    // set up static button events
    ms_button_create_new_set.on("click", () => measurement_sets_create_new_set(inspection_id, item, drawing));
    ms_button_refresh_list.on("click", () => measurement_sets_refresh_list(inspection_id, item, drawing));
    ms_button_save_edits.on("click", measurement_sets_save_edits);

    // populate the measurement set list
    await measurement_sets_update_filtered_sets(inspection_id);
}

async function measurement_sets_create_new_set(inspection_id, item, drawing)
{
    // create a new set and repopulate the list display
    await d3.json("/inspection_reports/measurement_sets_add_set/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            schema_id: ms_select_schema.property("value"),
            employee_id: ms_select_employee.property("value"),
            search_term: ms_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            measurement_sets_repopulate_set_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // refresh the measurement filter options
    await measurements_get_filter_parameter_data(inspection_id, item, drawing);

    // refresh the displayed measurements
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function measurement_sets_save_edits()
{
    await d3.json("/inspection_reports/measurement_sets_save_edits/", {
        method: "POST",
        body: JSON.stringify({
            data: ms_ul_list.selectAll("li").data()
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

async function measurement_sets_refresh_list(inspection_id, item, drawing)
{
    await measurement_sets_update_filtered_sets(inspection_id);
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function measurement_sets_delete_set(measurement_set_id, inspection_id, item, drawing)
{
    // delete the selected set and repopulate the list display
    await d3.json("/inspection_reports/measurement_sets_delete_set/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            measurement_set_id: measurement_set_id,
            search_term: ms_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            measurement_sets_repopulate_set_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    
    // refresh the measurement filter options
    await measurements_get_filter_parameter_data(inspection_id, item, drawing);

    // refresh the displayed measurements
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function measurement_sets_update_filtered_sets(inspection_id)
{
    await d3.json("/inspection_reports/measurement_sets_get_filtered_sets/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: ms_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            measurement_sets_repopulate_set_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function measurement_sets_repopulate_set_list(data)
{
    // add the display state value to incoming data
    for (let i = 0; i < data.length; i++) {
        data[i]["display_state"] = 1;
    }

    // clear the old entries
    ms_ul_list.selectAll("li").remove();

    // populate the inspection reports list
    let items = ms_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(2, minmax(0, 5fr)) repeat(2, minmax(0, 3fr)) repeat(2, minmax(0, 4fr))");
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .attr("type", "datetime-local")
        .attr("step", "any")
        .attr("class", "list-item-label-dark")
        .property("value", (x) => x.timestamp)
        .on("change", (e, x) => {
            x.timestamp = e.srcElement.value;
        })
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            ms_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // delete the set
            ms_ul_list_contextmenu.select("#context_menu_0").on("click", () => {
                measurement_sets_delete_set(x.measurement_set_id, x.inspection_id, x.item, x.drawing);
                ms_ul_list_contextmenu.style("display", "none");
            });

            // prevent the default behavior
            e.preventDefault();
        });
    let employee_select = items.append("select");
    employee_select.selectAll("option")
        .data(glist_employees)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    employee_select
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark")
        .property("value", (x) => x.employee_id)
        .on("change", (e, x) => {
            x.employee_id == e.srcElement.value;
        });
    items.append("input")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "1")
        .attr("class", "list-item-label-dark")
        .property("value", (x) => x.part_index)
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.part_index = e.srcElement.value;
        });
    items.append("input")
        .style("--grid-column", "4")
        .style("--grid-row", "1")
        .attr("type", "text")
        .attr("disabled", true)
        .attr("class", "list-item-label-dark")
        .property("value", (x) => x.revision);
    let measurement_type_select = items.append("select");
    measurement_type_select.selectAll("option")
        .data(glist_measurement_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    measurement_type_select
        .style("--grid-column", "5")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark")
        .property("value", (x) => x.measurement_type_id)
        .on("change", (e, x) => {
            x.measurement_type_id == e.srcElement.value;
        });
    items.append("input")
        .style("--grid-column", "6")
        .style("--grid-row", "1")
        .attr("type", "checkbox")
        .attr("class", "list-item-switch-dark")
        .property("checked", (x) => x.display_state)
        .on("change", (e, x) => {
            x.display_state = e.srcElement.checked;
            measurements_get_filtered_measurements(x.inspection_id, x.item, x.drawing);
        });
}

async function measurement_sets_update_set_schemas(inspection_id)
{
    await d3.json("/inspection_reports/measurement_sets_get_filtered_set_schemas/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: ms_input_schema_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ms_select_schema.selectAll("option").remove();

            // repopulate the selector
            ms_select_schema.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.schema_id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function measurement_sets_update_employees()
{
    await d3.json("/get_filtered_employees/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ms_input_employee_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ms_select_employee.selectAll("option").remove();

            // repopulate the selector
            ms_select_employee.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// #endregion

// #region measurements

async function measurements_prepare_panel(inspection_id, item, drawing)
{
    // clear out filters
    ms_input_schema_filter.property("value", "");
    ms_input_employee_filter.property("value", "");

    // populate the selectors
    await measurements_get_filter_parameter_data(inspection_id, item, drawing);

    // set up static button events
    mt_button_update_display.on("click", () => measurements_get_filtered_measurements(inspection_id, item, drawing));
    mt_button_save_characteristics.on("click", measurements_save_edits);

    // populate the measurements table
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function measurements_get_filtered_measurements(inspection_id, item, drawing)
{
    // get the list of measurement sets
    let measurement_sets = [];
    ms_ul_list.selectAll("li").data().forEach((e) => {
        measurement_sets.push({
            measurement_set_id: e.measurement_set_id,
            display_state: e.display_state
        });
    });

    // logic gate
    if (measurement_sets.length == 0) {
        return;
    }

    // query the database
    await d3.json("/inspection_reports/measurements_get_filtered_measurements/", {
        method: "POST",
        body: JSON.stringify({
            identity: {
                inspection_id: inspection_id,
                item: item,
                drawing: drawing
            },
            content: {
                has_deviations: mt_select_has_deviations.property("value"),
                measurement_type_id: mt_select_measurement_type.property("value"),
                employee_id: mt_select_inspector.property("value"),
                part_index: mt_select_part_index.property("value"),
                revision: mt_select_revision.property("value"),
                name: mt_input_name.property("value"),
                frequency_type_id: mt_select_frequency_type.property("value"),
                gauge_id: mt_select_gauge.property("value"),
                gauge_type_id: mt_select_gauge_type.property("value"),
                specification_type_id: mt_select_specification_type.property("value"),
                dimension_type_id: mt_select_dimension_type.property("value"),
                measurement_sets: measurement_sets
            }
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // the table must always be reset
        vw_measurements_table.selectAll("thead").remove();
        vw_measurements_table.selectAll("tbody").remove();

        if (json.status == "ok") {

            // repopulate the characteristic table
            measurements_repopulate_table(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function measurements_save_edits()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reversed. Continue?")) {
        return;
    }

    // query the flask server
    d3.json("/inspection_reports/measurements_save_measurements/", {
        method: "POST",
        body: JSON.stringify({
            data: vw_measurements_table.select("tbody").selectAll("td").data()
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
    });
}

async function measurements_tunnel_to_physical_part(inspection_id, part_id, part_index)
{
    await d3.json("/inspection_reports/measurements_tunnel_to_physical_part/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            part_id: part_id,
            part_index: part_index
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // the table must always be reset
        vw_measurements_table.selectAll("thead").remove();
        vw_measurements_table.selectAll("tbody").remove();

        if (json.status == "ok") {

            // repopulate the characteristic table
            measurements_repopulate_table(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function measurements_view_deviations(measurement_id, part_index, revision, name, inspection_id, item, drawing)
{
    // close any panel that is already open
    if (open_panel != null && open_panel != "deviations") {
        await toggle_options(open_panel, "0px");
    }

    // prepare the deviations panel
    await deviations_prepare_panel(measurement_id, part_index, revision, name, inspection_id, item, drawing);

    // open the deviations panel
    if (open_panel != "deviations")
        await toggle_options("deviations", "1000px");
}

async function measurements_get_filter_parameter_data(inspection_id, item, drawing)
{
    await d3.json("/inspection_reports/measurements_get_filter_parameter_data/", {
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
        if (json.status == "ok") {

            // update the measurement types
            mt_select_measurement_type.selectAll("option").remove();
            json.response.measurement_types.unshift({ id: -1, name: "n/a" });
            mt_select_measurement_type.selectAll("option")
                .data(json.response.measurement_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the part index
            mt_select_part_index.selectAll("option").remove();
            json.response.part_indices.unshift({ id: -1, name: "n/a" });
            mt_select_part_index.selectAll("option")
                .data(json.response.part_indices)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the revision
            mt_select_revision.selectAll("option").remove();
            json.response.revisions.unshift({ id: "", name: "n/a" });
            mt_select_revision.selectAll("option")
                .data(json.response.revisions)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the frequency types
            mt_select_frequency_type.selectAll("option").remove();
            json.response.frequency_types.unshift({ id: -1, name: "n/a" });
            mt_select_frequency_type.selectAll("option")
                .data(json.response.frequency_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the inspectors
            mt_select_inspector.selectAll("option").remove();
            json.response.inspectors.unshift({ id: -1, name: "n/a" });
            mt_select_inspector.selectAll("option")
                .data(json.response.inspectors)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauges
            mt_select_gauge.selectAll("option").remove();
            json.response.gauges.unshift({ id: -1, name: "n/a" });
            mt_select_gauge.selectAll("option")
                .data(json.response.gauges)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauge types
            mt_select_gauge_type.selectAll("option").remove();
            json.response.gauge_types.unshift({ id: -1, name: "n/a" });
            mt_select_gauge_type.selectAll("option")
                .data(json.response.gauge_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the specification types
            mt_select_specification_type.selectAll("option").remove();
            json.response.specification_types.unshift({ id: -1, name: "n/a" });
            mt_select_specification_type.selectAll("option")
                .data(json.response.specification_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the dimension types
            mt_select_dimension_type.selectAll("option").remove();
            json.response.dimension_types.unshift({ id: -1, name: "n/a" });
            mt_select_dimension_type.selectAll("option")
                .data(json.response.dimension_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function measurements_repopulate_table(data)
{
    // get the current display type
    let display_type = mt_select_display_type.property("value");

    // table schema
    let table_schema = main_table_columns[display_type];

    // clear the old columns
    vw_measurements_table.selectAll("thead").remove();

    // add the columns
    vw_measurements_table.append("thead")
        .selectAll("tr")
        .data(table_schema)
        .join("th")
        .attr("scope", "col")
        .style("width", (x) => x.width)
        .text((x) => x.col.display);

    // clear the old rows
    vw_measurements_table.selectAll("tbody").remove();

    // add the rows
    let rows = vw_measurements_table.append("tbody")
        .selectAll("tr")
        .data(data)
        .join("tr")
        .on("click", (_, x) => deviations_prepare_panel(x.measurement_id, x.part_index, x.revision, x.name, x.inspection_id, x.item, x.drawing))
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            vw_measurements_table_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // tunnel to physical part
            vw_measurements_table_contextmenu.select("#context_menu_0").on("click", () => {
                measurements_tunnel_to_physical_part(x.inspection_id, x.part_id, x.part_index);
                vw_measurements_table_contextmenu.style("display", "none");
            });

            // view deviations
            vw_measurements_table_contextmenu.select("#context_menu_1").on("click", () => {
                measurements_view_deviations(x.measurement_id, x.part_index, x.revision, x.name, x.inspection_id, x.item, x.drawing);
                vw_measurements_table_contextmenu.style("display", "none");
            });

            // prevent the default behavior
            e.preventDefault();
        });

    // create the cells
    let cells = rows.selectAll("td")
        .data((r) => {
            return table_schema.map((c) => {
                return {
                    column: c.col,
                    row: {
                        value: r[c.col.key],
                        has_deviations: r.has_deviations,
                        precision: r.precision,
                        measurement_id: r.measurement_id,
                        part_index: r.part_index,
                        measurement_set_id: r.measurement_set_id,
                        gauge_type_id: r.gauge_type_id,
                        part_id: r.part_id,
                        inspection_id: r.inspection_id,
                        item: r.item,
                        drawing: r.drawing,
                        revision: r.revision,
                        name: r.name
                    }
                };
            });
        })
        .join("td");

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
            switch (x.column.datatype) {
                case "decimal":
                    return x.row.value.toFixed(x.row.precision);
                default:
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
        .attr("type", (x) => {
            switch (x.column.datatype) {
                case "string":
                    return "text";
                default:
                    return "number";
            }
        })
        .attr("step", "any")
        .property("value", (x) => {
            switch (x.row.value) {
                case null:
                    return "";
                default:
                    switch (x.column.datatype) {
                        case "decimal":
                            return x.row.value.toFixed(x.row.precision);
                        default:
                            return x.row.value;
                    }
            }
        }).on("change", (e, x) => {
            x.row.value = parseFloat(e.srcElement.value);
            if (x.column.datatype == "decimal") {
                e.srcElement.value = x.row.value.toFixed(x.row.precision);
            }
        });

    // gauges
    cells.filter((x) => {
            if (x.column.key == "gauge_id") {
                return true;
            }
        })
        .insert("select")
        .attr("class", "data-table-cell-dark")
        .selectAll("option")
        .data((x) => {
            return glist_gauge_ids.filter((e) => { 
                return e.gauge_type_id == x.row.gauge_type_id
            });
        })
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.key == "gauge_id") {
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
            if (x.column.key == "employee_id") {
                return true;
            }
        })
        .insert("select")
        .attr("class", "data-table-cell-dark")
        .selectAll("option")
        .data(glist_employees)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    cells.filter((x) => {
            if (x.column.key == "employee_id") {
                return true;
            }
        })
        .selectAll("select")
        .property("value", (x) => x.row.value)
        .on("change", (e, x) => {
            x.row.value = parseInt(e.srcElement.value);
        });
}

// #endregion

// #region metadata

async function metadata_prepare_panel(inspection_id, item, drawing)
{
    // populate the selectors
    await d3.json("/get_all_disposition_types/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            md_select_disposition.selectAll("option").remove();

            // populate the item numbers
            md_select_disposition.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await d3.json("/get_all_material_types/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            md_select_material_type.selectAll("option").remove();

            // populate the item numbers
            md_select_material_type.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await d3.json("/get_all_employees/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            md_select_inspector.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_inspector.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await d3.json("/get_all_job_orders/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            md_select_job_order.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_job_order.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await d3.json("/get_all_suppliers/", {
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            md_select_supplier.selectAll("option").remove();

            // add to the dataset
            json.response.unshift({ id: -1 });

            // populate the item numbers
            md_select_supplier.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => {
                    if (x.id > 0) {
                        return x.name;
                    }
                    else {
                        return "n/a";
                    }});
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await d3.json("/inspection_reports/metadata_get_parameters/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            md_select_disposition.property("value", json.response.disposition_id);
            md_select_material_type.property("value", json.response.material_type_id);
            md_select_inspector.property("value", json.response.employee_id);
            md_select_job_order.property("value", json.response.job_order_id);
            md_select_supplier.property("value", json.response.supplier_id);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // set up static button events
    md_button_save.on("click", () => metadata_save(inspection_id));

    // populate the revisions list
    await metadata_get_matching_revisions(item, drawing)
}

async function metadata_save(inspection_id)
{
    // request confirmation
    if (!confirm("This will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/metadata_save/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            sub_data: md_ul_list.selectAll("li").data(),
            content: {
                disposition_id: md_select_disposition.property("value"),
                material_type_id: md_select_material_type.property("value"),
                employee_id: md_select_inspector.property("value"),
                job_order_id: md_select_job_order.property("value"),
                supplier_id: md_select_supplier.property("value")
            }
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

async function metadata_get_matching_revisions(item, drawing)
{
    await d3.json("/inspection_reports/metadata_get_matching_revisions/", {
        method: "POST",
        body: JSON.stringify({
            item: item,
            drawing: drawing
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            metadata_repopulate_revision_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function metadata_repopulate_revision_list(data)
{
    // remove the old entries
    md_ul_list.selectAll("li").remove();

    // repopulate the revisions list
    let items = md_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(4, minmax(0, 1fr))")
        .on("click", (e, x) => metadata_revision_clicked(e));
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
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.full_inspect_interval = parseInt(e.srcElement.value);
        });
    items.append("input")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.released_qty)
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
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
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.completed_qty = parseInt(e.srcElement.value);
        });
}

async function metadata_revision_clicked(event)
{
    // check if the item is already selected
    let is_selected = event.srcElement.parentNode.classList.contains("list-item-dark-selected");

    // reset/set the selected class
    for (let i = 0; i < md_ul_list.node().childNodes.length; i++) {
        let current_node = md_ul_list.node().childNodes[i].children[0];
        current_node.classList.remove("list-item-dark-selected");
    }

    // filter actions
    if (!is_selected) {
        event.srcElement.parentNode.classList.add("list-item-dark-selected");
    }
    else {
        event.srcElement.blur();
    }
}

// #endregion

// #region receiver numbers

async function receiver_numbers_prepare_panel(inspection_id)
{
    // clear the inputs
    rn_input_selected_search_term.property("value", "");
    rn_input_search_term.property("value", "");

    // populate the selector
    await receiver_numbers_update_filtered_selector();

    // set up static input events
    rn_input_selected_search_term.on("change", receiver_numbers_update_filtered_selector);
    rn_input_search_term.on("change", () => receiver_numbers_update_filtered_list(inspection_id));

    // set up static button events
    rn_button_add.on("click", () => receiver_numbers_assign_association(inspection_id));

    // populate the list
    await receiver_numbers_update_filtered_list(inspection_id);
}

async function receiver_numbers_assign_association(inspection_id)
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/reciever_numbers_assign_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rn_input_search_term.property("value"),
            inspection_id: inspection_id,
            receiver_number_id: rn_select_selected.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            receiver_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function receiver_numbers_remove_association(inspection_id, id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/reciever_numbers_remove_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rn_input_search_term.property("value"),
            inspection_id: inspection_id,
            receiver_number_id: id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            receiver_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function receiver_numbers_update_filtered_selector()
{
    await d3.json("/inspection_reports/receiver_numbers_get_filtered_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rn_input_selected_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            rn_select_selected.selectAll("option").remove();

            // populate the selector
            rn_select_selected.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function receiver_numbers_update_filtered_list(inspection_id)
{
    await d3.json("/inspection_reports/receiver_numbers_get_filtered_associations/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: rn_input_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            receiver_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function receiver_numbers_repopulate_list(data)
{
    // clear the old entries
    rn_ul_list.selectAll("li").remove();

    // logic gate
    if (data.size == 0) {
        return;
    }

    // populate the list
    let items = rn_ul_list.selectAll("li")
        .data(data.data)
        .join("li")
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
        .on("click", (_, x) => receiver_numbers_remove_association(x.inspection_id, x.id));
}

// #endregion

// #region purchase orders

async function purchase_orders_prepare_panel(inspection_id)
{
    // clear the inputs
    po_input_selected_search_term.property("value", "");
    po_input_search_term.property("value", "");

    // populate the selector
    await purchase_orders_update_filtered_selector();

    // set up static input events
    po_input_selected_search_term.on("change", purchase_orders_update_filtered_selector);
    po_input_search_term.on("change", () => purchase_orders_update_filtered_list(inspection_id));

    // set up static button events
    po_button_add.on("click", () => purchase_orders_assign_association(inspection_id));

    // populate the list
    await purchase_orders_update_filtered_list(inspection_id);
}

async function purchase_orders_assign_association(inspection_id)
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/purchase_orders_assign_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: po_input_search_term.property("value"),
            inspection_id: inspection_id,
            purchase_order_id: po_select_selected.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            purchase_orders_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function purchase_orders_remove_association(inspection_id, id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/purchase_orders_remove_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: po_input_search_term.property("value"),
            inspection_id: inspection_id,
            purchase_order_id: id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            purchase_orders_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function purchase_orders_update_filtered_selector()
{
    await d3.json("/inspection_reports/purchase_orders_get_filtered_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: po_input_selected_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            po_select_selected.selectAll("option").remove();

            // populate the selector
            po_select_selected.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function purchase_orders_update_filtered_list(inspection_id)
{
    await d3.json("/inspection_reports/purchase_orders_get_filtered_associations/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: po_input_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            purchase_orders_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function purchase_orders_repopulate_list(data)
{
    // clear the old entries
    po_ul_list.selectAll("li").remove();

    // logic gate
    if (data.size == 0) {
        return;
    }

    // populate the list
    let items = po_ul_list.selectAll("li")
        .data(data.data)
        .join("li")
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
        .on("click", (_, x) => purchase_orders_remove_association(x.inspection_id, x.id));
}

// #endregion

// #region lot numbers

async function lot_numbers_prepare_panel(inspection_id)
{
    // clear the inputs
    ln_input_selected_search_term.property("value", "");
    ln_input_search_term.property("value", "");

    // populate the selector
    await lot_numbers_update_filtered_selector();

    // set up static input events
    ln_input_selected_search_term.on("change", lot_numbers_update_filtered_selector);
    ln_input_search_term.on("change", () => lot_numbers_update_filtered_list(inspection_id));

    // set up static button events
    ln_button_add.on("click", () => lot_numbers_assign_association(inspection_id));

    // populate the list
    await lot_numbers_update_filtered_list(inspection_id);
}

async function lot_numbers_assign_association(inspection_id)
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/lot_numbers_assign_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ln_input_search_term.property("value"),
            inspection_id: inspection_id,
            lot_number_id: ln_select_selected.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            lot_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function lot_numbers_remove_association(inspection_id, id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_reports/lot_numbers_remove_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ln_input_search_term.property("value"),
            inspection_id: inspection_id,
            lot_number_id: id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            lot_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function lot_numbers_update_filtered_selector()
{
    await d3.json("/inspection_reports/lot_numbers_get_filtered_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ln_input_selected_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ln_select_selected.selectAll("option").remove();

            // populate the selector
            ln_select_selected.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function lot_numbers_update_filtered_list(inspection_id)
{
    await d3.json("/inspection_reports/lot_numbers_get_filtered_associations/", {
        method: "POST",
        body: JSON.stringify({
            inspection_id: inspection_id,
            search_term: ln_input_search_term.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            lot_numbers_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function lot_numbers_repopulate_list(data)
{
    // clear the old entries
    ln_ul_list.selectAll("li").remove();

    // logic gate
    if (data.size == 0) {
        return;
    }

    // populate the list
    let items = ln_ul_list.selectAll("li")
        .data(data.data)
        .join("li")
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
        .on("click", (_, x) => lot_numbers_remove_association(x.inspection_id, x.id));
}

// #endregion

// #region deviations

async function deviations_prepare_panel(measurement_id, part_index, revision, name, inspection_id, item, drawing)
{
    // set the visual flag
    dv_label_current.text(`${part_index} // ${revision} // ${name}`);

    // clear inputs
    dv_input_notes.property("value", "");

    // clear the list
    dv_ul_list.selectAll("li").remove();

    // set up static button events
    dv_button_add.on("click", () => deviations_add(measurement_id, inspection_id, item, drawing));
    dv_button_save.on("click", () => deviations_save(measurement_id));

    // populate the list
    await deviations_get_measurement_deviations(measurement_id);
}

async function deviations_add(measurement_id, inspection_id, item, drawing)
{
    // add a new deviation
    await d3.json("/inspection_reports/deviations_add_deviation/", {
        method: "POST",
        body: JSON.stringify({
            measurement_id: measurement_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, measurement_id, inspection_id, item, drawing);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // requery for measurements
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function deviations_save(measurement_id)
{
    await d3.json("/inspection_reports/deviations_save/", {
        method: "POST",
        body: JSON.stringify({
            measurement_id: measurement_id,
            data: dv_ul_list.selectAll("li").data()
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

async function deviations_delete(measurement_id, deviation_id, inspection_id, item, drawing)
{
    await d3.json("/inspection_reports/deviations_delete_deviation/", {
        method: "POST",
        body: JSON.stringify({
            measurement_id: measurement_id,
            deviation_id: deviation_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // clear the old entries every time
        dv_ul_list.selectAll("li").remove();

        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, measurement_id, inspection_id, item, drawing);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // requery for measurements
    await measurements_get_filtered_measurements(inspection_id, item, drawing);
}

async function deviations_get_measurement_deviations(measurement_id)
{
    await d3.json("/inspection_reports/deviations_get_measurement_deviations/", {
        method: "POST",
        body: JSON.stringify({
            measurement_id: measurement_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, measurement_id, inspection_id, item, drawing);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function deviations_clicked(e, x)
{
    // check if the item is already selected
    let is_selected = e.srcElement.parentNode.classList.contains("list-item-dark-selected");

    // reset/set the selected class
    for (let i = 0; i < dv_ul_list.node().childNodes.length; i++) {
        let current_node = dv_ul_list.node().childNodes[i].children[0];
        current_node.classList.remove("list-item-dark-selected");
    }

    // filter actions
    if (!is_selected) {
        await deviations_selected(e, x);
    }
    else {
        await deviations_unselected(e);
    }
}

async function deviations_selected(e, x)
{
    // set the visual flags
    e.srcElement.parentNode.classList.add("list-item-dark-selected");

    // set the notes
    dv_input_notes.property("value", x.notes);
}

async function deviations_unselected(e)
{
    // remove focus
    e.srcElement.blur();

    // reset the notes
    dv_input_notes.property("value", "");
}

async function deviations_repopulate_deviations_list(data, measurement_id, inspection_id, item, drawing)
{
    // clear the old entries
    dv_ul_list.selectAll("li").remove();

    // repopulate the deviations list
    let items = dv_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(4, minmax(0, 2fr)) repeat(3, minmax(0, 3fr))")
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            dv_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // delete deviation
            dv_ul_list_contextmenu.select("#context_menu_0").on("click", () => {
                deviations_delete(measurement_id, x.id, inspection_id, item, drawing);
                dv_ul_list_contextmenu.style("display", "none");
            });

            // prevent default behavior
            e.preventDefault();
        })
        .on("click", (e, x) => deviations_clicked(e, x));
    let nominal = items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px 0px 0px 6px")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.nominal.toFixed(x.precision))
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.nominal = parseFloat(e.srcElement.value);
            e.srcElement.value = x.nominal.toFixed(x.precision);
        });
    let usl = items.append("input")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.usl.toFixed(x.precision))
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.usl = parseFloat(e.srcElement.value);
            e.srcElement.value = x.usl.toFixed(x.precision);
        });
    let lsl = items.append("input")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.lsl.toFixed(x.precision))
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.lsl = parseFloat(e.srcElement.value);
            e.srcElement.value = x.lsl.toFixed(x.precision);
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
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
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
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
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
        .data(glist_deviations)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);

    // set the deviations select value
    deviations.property("value", (x) => x.deviation_type_id)
        .on("change", (e, x) => {
            x.deviation_type_id = parseInt(e.srcElement.value);
        });

    // populate the employees select
    employees.selectAll("option")
        .data(glist_employees)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);

    // set the employees select value
    employees.property("value", (x) => x.employee_id)
        .on("change", (e, x) => {
            x.employee_id = parseInt(e.srcElement.value);
        });
}

// #endregion

// #region sidebar control

async function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "inspection_reports") {
        if (document.getElementById("inspection_reports_sidebar").style.width == open_width) {
            document.getElementById("inspection_reports_sidebar").style.width = close_width;
            document.getElementById("inspection_reports_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("inspection_reports_sidebar").style.width = open_width;
            document.getElementById("inspection_reports_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "measurement_sets") {
        if (document.getElementById("measurement_sets_sidebar").style.width == open_width) {
            document.getElementById("measurement_sets_sidebar").style.width = close_width;
            document.getElementById("measurement_sets_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("measurement_sets_sidebar").style.width = open_width;
            document.getElementById("measurement_sets_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "measurements") {
        if (document.getElementById("measurements_sidebar").style.width == open_width) {
            document.getElementById("measurements_sidebar").style.width = close_width;
            document.getElementById("measurements_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("measurements_sidebar").style.width = open_width;
            document.getElementById("measurements_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "metadata") {
        if (document.getElementById("metadata_sidebar").style.width == open_width) {
            document.getElementById("metadata_sidebar").style.width = close_width;
            document.getElementById("metadata_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("metadata_sidebar").style.width = open_width;
            document.getElementById("metadata_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "receiver_numbers") {
        if (document.getElementById("receiver_numbers_sidebar").style.width == open_width) {
            document.getElementById("receiver_numbers_sidebar").style.width = close_width;
            document.getElementById("receiver_numbers_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("receiver_numbers_sidebar").style.width = open_width;
            document.getElementById("receiver_numbers_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "purchase_orders") {
        if (document.getElementById("purchase_orders_sidebar").style.width == open_width) {
            document.getElementById("purchase_orders_sidebar").style.width = close_width;
            document.getElementById("purchase_orders_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("purchase_orders_sidebar").style.width = open_width;
            document.getElementById("purchase_orders_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "lot_numbers") {
        if (document.getElementById("lot_numbers_sidebar").style.width == open_width) {
            document.getElementById("lot_numbers_sidebar").style.width = close_width;
            document.getElementById("lot_numbers_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("lot_numbers_sidebar").style.width = open_width;
            document.getElementById("lot_numbers_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "deviations") {
        if (document.getElementById("deviations_sidebar").style.width == open_width) {
            document.getElementById("deviations_sidebar").style.width = close_width;
            document.getElementById("deviations_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("deviations_sidebar").style.width = open_width;
            document.getElementById("deviations_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
}

//#endregion
