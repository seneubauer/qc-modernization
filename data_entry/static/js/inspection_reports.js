
// navbar
const navbar_info = d3.select("#navbar_info");

// characteristics
const vw_features_table = d3.select("#measurements_table");
const vw_features_table_contextmenu = d3.select("#measurements_table_contextmenu");

// inspection records
const ir_button_new = d3.select("#inspection_records_new");
const ir_button_refresh = d3.select("#inspection_records_refresh");
const ir_input_part_new = d3.select("#inspection_records_part_filter_new");
const ir_select_part_new = d3.select("#inspection_records_part_new");
const ir_input_schema_new = d3.select("#inspection_records_schema_filter_new");
const ir_select_schema_new = d3.select("#inspection_records_schema_new");
const ir_input_employee_new = d3.select("#inspection_records_employee_filter_new");
const ir_select_employee_new = d3.select("#inspection_records_employee_new");
const ir_input_part_list = d3.select("#inspection_records_part_list");
const ir_input_started_after_list = d3.select("#inspection_records_started_after_list");
const ir_input_finished_before_list = d3.select("#inspection_records_finished_before_list");
const ir_input_material_type_list = d3.select("#inspection_records_material_type_list");
const ir_input_employee_list = d3.select("#inspection_records_employee_list");
const ir_input_disposition_list = d3.select("#inspection_records_disposition_list");
const ir_input_receiver_number_list = d3.select("#inspection_records_receiver_number_list");
const ir_input_purchase_order_list = d3.select("#inspection_records_purchase_order_list");
const ir_input_job_order_list = d3.select("#inspection_records_job_order_list");
const ir_input_lot_number_list = d3.select("#inspection_records_lot_number_list");
const ir_input_supplier_list = d3.select("#inspection_records_supplier_list");
const ir_ul_list = d3.select("#inspection_records_filtered_list");
const ir_ul_list_contextmenu = d3.select("#inspection_records_list_contextmenu");

// inspections
const in_button_create_new_set = d3.select("#inspections_add");
const in_button_refresh_list = d3.select("#inspections_refresh_list");
const in_button_save_edits = d3.select("#inspections_save");
const in_input_schema_filter = d3.select("#inspections_schema_filter");
const in_select_schema = d3.select("#inspections_schema");
const in_input_employee_filter = d3.select("#inspections_employee_filter");
const in_select_employee = d3.select("#inspections_employee");
const in_input_display_filter = d3.select("#inspections_display_filter");
const in_ul_list = d3.select("#inspections_list");
const in_ul_list_contextmenu = d3.select("#inspections_list_contextmenu");

// features
const ft_button_update_display = d3.select("#features_apply_filter");
const ft_button_save_characteristics = d3.select("#features_save_changes");
const ft_select_display_type = d3.select("#features_display_type");
const ft_select_inspection_type = d3.select("#features_inspection_type");
const ft_input_name = d3.select("#features_dimension_name");
const ft_select_frequency_type = d3.select("#features_frequency_type");
const ft_select_has_deviations = d3.select("#features_has_deviations");
const ft_select_inspector = d3.select("#features_inspector");
const ft_select_gauge = d3.select("#features_gauge");
const ft_select_gauge_type = d3.select("#features_gauge_type");
const ft_select_specification_type = d3.select("#features_specification_type");
const ft_select_dimension_type = d3.select("#features_dimension_type");
const ft_select_part_index = d3.select("#features_part_index");
const ft_select_revision = d3.select("#features_revision");

// manufactured
const mn_button_add_job_order = d3.select("#manufactured_job_order_add");
const mn_button_save_job_order = d3.select("#manufactured_job_order_save");
const mn_input_job_number_search = d3.select("#manufactured_job_order_search_term");
const mn_select_job_order = d3.select("#manufactured_job_order");
const mn_input_part_search = d3.select("#manufactured_part_search_term");
const mn_select_part = d3.select("#manufactured_part");
const mn_input_job_number_display_filter = d3.select("#manufactured_job_order_display_filter");
const mn_ul_list = d3.select("#manufactured_job_order_list");
const mn_ul_list_contextmenu = d3.select("#manufactured_job_order_list_contextmenu");

// received
const rc_button_add_purchase_order = d3.select("#received_purchase_order_add");
const rc_button_add_receiver_number = d3.select("#received_receiver_number_add");
const rc_button_save_received_quantities = d3.select("#received_save_received_quantities");
const rc_input_purchase_order_search = d3.select("#received_purchase_order_search_term");
const rc_select_purchase_order = d3.select("#received_purchase_order");
const rc_input_receiver_number_search = d3.select("#received_receiver_number_search_term");
const rc_select_receiver_number = d3.select("#received_receiver_number");
const rc_input_supplier_search = d3.select("#received_supplier_search_term");
const rc_select_supplier = d3.select("#received_supplier");
const rc_input_purchase_order_display_filter = d3.select("#received_purchase_order_display_filter");
const rc_input_receiver_number_display_filter = d3.select("#received_receiver_number_display_filter");
const rc_ul_purchase_order_list = d3.select("#received_purchase_order_list");
const rc_ul_receiver_number_list = d3.select("#received_receiver_number_list");
const rc_ul_receiver_number_list_contextmenu = d3.select("#received_receiver_number_list_context_menu");
const rc_ul_purchase_order_list_contextmenu = d3.select("#received_purchase_order_list_context_menu");

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
var glist_material_types = null;
var glist_inspection_types = null;
var glist_dispositions = null;

// open panel
var open_panel = null;

// feature table color code
var pass_static = "hsl(120, 50%, 35%)";
var pass_hover = "hsl(120, 50%, 30%)";
var pass_active = "hsl(120, 50%, 25%)";
var fail_static = "hsl(0, 50%, 35%)";
var fail_hover = "hsl(0, 50%, 30%)";
var fail_active = "hsl(0, 50%, 25%)";
var incomplete_static = "hsl(0, 0%, 45%)";
var incomplete_hover = "hsl(0, 0%, 40%)";
var incomplete_active = "hsl(0, 0%, 35%)";

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
    await inspection_records_prepare_panel();

    // close context menus
    d3.select("body").on("click", () => {
        if (ir_ul_list_contextmenu.style("display") == "block") {
            ir_ul_list_contextmenu.style("display", "none");
        }
        if (in_ul_list_contextmenu.style("display") == "block") {
            in_ul_list_contextmenu.style("display", "none");
        }
        if (vw_features_table_contextmenu.style("display") == "block") {
            vw_features_table_contextmenu.style("display", "none");
        }
        if (mn_ul_list_contextmenu.style("display") == "block") {
            mn_ul_list_contextmenu.style("display", "none");
        }
        if (rc_ul_purchase_order_list_contextmenu.style("display") == "block") {
            rc_ul_purchase_order_list_contextmenu.style("display", "none");
        }
        if (rc_ul_receiver_number_list_contextmenu.style("display") == "block") {
            rc_ul_receiver_number_list_contextmenu.style("display", "none");
        }
        if (dv_ul_list_contextmenu.style("display") == "block") {
            dv_ul_list_contextmenu.style("display", "none");
        }
    });
}

function set_disabled_state(state)
{
    document.getElementById("inspections_button").disabled = state;
    document.getElementById("features_button").disabled = state;
    document.getElementById("manufactured_button").disabled = state;
    document.getElementById("received_button").disabled = state;
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

    // material types
    d3.json("/get_all_material_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_material_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // measurement types
    d3.json("/get_all_inspection_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_inspection_types = json.response;
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // disposition types
    d3.json("/get_all_disposition_types/", {
        method: "GET"
    }).then((json) => {
        if (json.status == "ok") {
            glist_dispositions = json.response;
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

// #region inspection records

async function inspection_records_prepare_panel()
{
    // clear out the filters
    ir_input_part_new.property("value", "");
    ir_input_schema_new.property("value", "");
    ir_input_employee_new.property("value", "");
    ir_input_part_list.property("value", "");
    ir_input_material_type_list.property("value", "");
    ir_input_employee_list.property("value", "");
    ir_input_disposition_list.property("value", "");
    ir_input_receiver_number_list.property("value", "");
    ir_input_purchase_order_list.property("value", "");
    ir_input_job_order_list.property("value", "");
    ir_input_lot_number_list.property("value", "");
    ir_input_supplier_list.property("value", "");

    // populate the selectors
    await inspection_records_update_part_selector();
    await inspection_records_update_schema_selector();
    await inspection_records_update_employee_selector();

    // set default values
    ir_input_started_after_list.property("value", "1970-01-01");
    ir_input_finished_before_list.property("value", "2100-01-01");

    // set up static input events
    ir_input_part_new.on("change", async () => {
        await inspection_records_update_part_selector();
        await inspection_records_update_schema_selector();
    });
    ir_input_part_new.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_schema_new.on("change", inspection_records_update_schema_selector);
    ir_input_schema_new.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_employee_new.on("change", inspection_records_update_employee_selector);
    ir_input_employee_new.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_part_list.on("change", inspection_records_update_filtered_reports);
    ir_input_part_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_started_after_list.on("change", inspection_records_update_filtered_reports);
    ir_input_finished_before_list.on("change", inspection_records_update_filtered_reports);
    ir_input_material_type_list.on("change", inspection_records_update_filtered_reports);
    ir_input_material_type_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_employee_list.on("change", inspection_records_update_filtered_reports);
    ir_input_employee_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_disposition_list.on("change", inspection_records_update_filtered_reports);
    ir_input_disposition_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_receiver_number_list.on("change", inspection_records_update_filtered_reports);
    ir_input_receiver_number_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_purchase_order_list.on("change", inspection_records_update_filtered_reports);
    ir_input_purchase_order_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_job_order_list.on("change", inspection_records_update_filtered_reports);
    ir_input_job_order_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_lot_number_list.on("change", inspection_records_update_filtered_reports);
    ir_input_lot_number_list.on("click", (e, _) => { e.srcElement.select(); });
    ir_input_supplier_list.on("change", inspection_records_update_filtered_reports);
    ir_input_supplier_list.on("click", (e, _) => { e.srcElement.select(); });

    // set up static select events
    ir_select_part_new.on("change", inspection_records_update_schema_selector);

    // set up static button events
    ir_button_new.on("click", inspection_records_create_new_report);
    ir_button_refresh.on("click", inspection_records_refresh_list);

    // populate the inspection report list
    await inspection_records_update_filtered_reports();
}

async function inspection_records_create_new_report()
{
    await d3.json("/inspection_records/inspection_records/create_new_record/", {
        method: "POST",
        body: JSON.stringify({
            part_id: ir_select_part_new.property("value"),
            schema_id: ir_select_schema_new.property("value"),
            employee_id: ir_select_employee_new.property("value"),
            part_search_term: ir_input_part_list.property("value"),
            job_number_search_term: ir_input_job_order_list.property("value"),
            started_after: ir_input_started_after_list.property("value"),
            finished_before: ir_input_finished_before_list.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            inspection_records_repopulate_report_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_records_refresh_list()
{
    // perform the unselect action
    await inspection_records_report_unselected();

    // requery for the list of inspection reports
    await inspection_records_update_filtered_reports();
}

async function inspection_records_delete(inspection_record_id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/inspection_records/delete_record/", {
        method: "POST",
        body: JSON.stringify({
            part_search_term: ir_input_part_list.property("value"),
            job_number_search_term: ir_input_job_order_list.property("value"),
            started_after: ir_input_started_after_list.property("value"),
            finished_before: ir_input_finished_before_list.property("value"),
            inspection_record_id: inspection_record_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the characteristic table
            vw_features_table.select("thead").selectAll("th").remove();
            vw_features_table.select("tbody").selectAll("td").remove();

            // repopulate the inspection report list
            inspection_records_repopulate_report_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspection_records_update_filtered_reports()
{
    await d3.json("/inspection_records/inspection_records/get_filtered_records/", {
        method: "POST",
        body: JSON.stringify({
            part: ir_input_part_list.property("value"),
            started_after: ir_input_started_after_list.property("value"),
            finished_before: ir_input_finished_before_list.property("value"),
            material_type: ir_input_material_type_list.property("value"),
            employee: ir_input_employee_list.property("value"),
            disposition: ir_input_disposition_list.property("value"),
            receiver_number: ir_input_receiver_number_list.property("value"),
            purchase_order: ir_input_purchase_order_list.property("value"),
            job_number: ir_input_job_order_list.property("value"),
            lot_number: ir_input_lot_number_list.property("value"),
            supplier: ir_input_supplier_list.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // repopulate the inspection report list
            inspection_records_repopulate_report_list(json.response);

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

async function inspection_records_repopulate_report_list(data)
{
    // clear the old entries
    ir_ul_list.selectAll("li").remove();

    // logic gate
    if (data == null) {
        return;
    }

    // populate the inspection reports list
    let items = ir_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(5, minmax(0, 1fr))")
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            ir_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // delete inspection report
            ir_ul_list_contextmenu.select("#context_menu_0").on("click", async () => {
                await inspection_records_delete(x.inspection_record_id);
                ir_ul_list_contextmenu.style("display", "none");
            });

            // prevent default behavior
            e.preventDefault();
        });
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px 0px 0px 6px")
        .style("cursor", "pointer")
        .attr("type", "text")
        .attr("readonly", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.item)
        .on("click", (e, x) => inspection_records_report_clicked(e, x));
    items.append("input")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .style("cursor", "pointer")
        .attr("type", "text")
        .attr("readonly", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.drawing)
        .on("click", (e, x) => inspection_records_report_clicked(e, x));
    let material_types = items.append("select")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark");
    let employees = items.append("select")
        .style("--grid-column", "4")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark");
    let dispositions = items.append("select")
        .style("--grid-column", "5")
        .style("--grid-row", "1")
        .style("border-radius", "0px 6px 6px 0px")
        .attr("class", "list-item-select-dark");
    
    // populate the material type options & value
    material_types.selectAll("option")
        .data(glist_material_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    material_types.property("value", (x) => x.material_type_id)
        .on("change", (e, x) => {
            x.material_type_id = parseInt(e.srcElement.value);
        });

    // populate the employee options & value
    employees.selectAll("option")
        .data(glist_employees)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    employees.property("value", (x) => x.employee_id)
        .on("change", (e, x) => {
            x.employee_id = parseInt(e.srcElement.value);
        });

    // populate the disposition options & value
    dispositions.selectAll("option")
        .data(glist_dispositions)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    dispositions.property("value", (x) => x.disposition_id)
        .on("change", (e, x) => {
            x.disposition_id = parseInt(e.srcElement.value);
        });
}

async function inspection_records_report_clicked(event, data)
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
        await inspection_records_report_selected(event, data);
    }
    else {
        await inspection_records_report_unselected();
    }
}

async function inspection_records_report_selected(event, data)
{
    // set the visual flags
    event.srcElement.parentNode.classList.add("list-item-dark-selected");
    navbar_info.text(`${data.item} // ${data.drawing}`);

    // unlock the panels
    set_disabled_state(false);

    // prepare the measurement sets panel
    await inspections_prepare_panel(data.inspection_record_id, data.item, data.drawing);

    // populate the measurements panel
    await features_prepare_panel(data.inspection_record_id, data.item, data.drawing);    

    // populate the manufactured panel
    await manufactured_prepare_panel(data.inspection_record_id);

    // populate the received panel
    await received_prepare_panel(data.inspection_record_id);

    // populate the lot numbers panel
    await lot_numbers_prepare_panel(data.inspection_record_id);
}

async function inspection_records_report_unselected()
{
    // set the visual flags
    navbar_info.text("");

    // lock the panels
    set_disabled_state(true);

    // depopulate the measurement sets
    in_button_create_new_set.on("click", null);
    in_button_refresh_list.on("click", null);
    in_input_schema_filter.on("change", null);
    in_input_employee_filter.on("change", null);
    in_input_schema_filter.property("value", "");
    in_input_employee_filter.property("value", "");
    in_input_display_filter.property("value", "");
    in_select_schema.selectAll("option").remove();
    in_select_employee.selectAll("option").remove();
    in_ul_list.selectAll("li").remove();

    // depopulate the measurements
    vw_features_table.selectAll("thead").remove();
    vw_features_table.selectAll("tbody").remove();
}

async function inspection_records_update_part_selector()
{
    await d3.json("/inspection_records/inspection_records/get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_part_new.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ir_select_part_new.selectAll("option").remove();

            // populate the item numbers
            ir_select_part_new.selectAll("option")
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

async function inspection_records_update_schema_selector()
{
    await d3.json("/inspection_records/inspection_records/get_filtered_schemas/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_part_new.property("value"),
            part_id: ir_select_part_new.property("value")
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
            ir_select_schema_new.selectAll("option").remove();

            // populate the item numbers
            ir_select_schema_new.selectAll("option")
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

async function inspection_records_update_employee_selector()
{
    await d3.json("/inspection_records/inspection_records/get_filtered_employees/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ir_input_employee_new.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            ir_select_employee_new.selectAll("option").remove();

            // populate the item numbers
            ir_select_employee_new.selectAll("option")
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

// #region inspections

async function inspections_prepare_panel(inspection_record_id, item, drawing)
{
    // clear out filters
    in_input_schema_filter.property("value", "");
    in_input_employee_filter.property("value", "");

    // populate the selectors
    await inspections_update_set_schemas(inspection_record_id);
    await inspections_update_employees();

    // set up static input events
    in_input_schema_filter.on("change", () => inspections_update_set_schemas(inspection_record_id));
    in_input_employee_filter.on("change", inspections_update_employees);

    // set up static button events
    in_button_create_new_set.on("click", () => inspections_create_new_set(inspection_record_id, item, drawing));
    in_button_refresh_list.on("click", () => inspections_refresh_list(inspection_record_id, item, drawing));
    in_button_save_edits.on("click", inspections_save_edits);

    // populate the measurement set list
    await inspections_update_filtered_sets(inspection_record_id);
}

async function inspections_create_new_set(inspection_record_id, item, drawing)
{
    // create a new set and repopulate the list display
    await d3.json("/inspection_records/inspections/add_inspection/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            schema_id: in_select_schema.property("value"),
            employee_id: in_select_employee.property("value"),
            search_term: in_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            inspections_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // refresh the measurement filter options
    await features_get_filter_parameters(inspection_record_id, item, drawing);

    // refresh the displayed measurements
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function inspections_save_edits()
{
    await d3.json("/inspection_records/inspections/save_edits/", {
        method: "POST",
        body: JSON.stringify({
            data: in_ul_list.selectAll("li").data()
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

async function inspections_refresh_list(inspection_record_id, item, drawing)
{
    await inspections_update_filtered_sets(inspection_record_id);
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function inspections_delete_set(inspection_id, inspection_record_id, item, drawing)
{
    // delete the selected set and repopulate the list display
    await d3.json("/inspection_records/inspections/delete_inspection/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            inspection_id: inspection_id,
            search_term: in_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            inspections_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    
    // refresh the measurement filter options
    await features_get_filter_parameters(inspection_record_id, item, drawing);

    // refresh the displayed measurements
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function inspections_update_filtered_sets(inspection_record_id)
{
    await d3.json("/inspection_records/inspections/get_filtered_inspections/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            search_term: in_input_display_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            inspections_repopulate_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function inspections_repopulate_list(data)
{
    // add the display state value to incoming data
    for (let i = 0; i < data.length; i++) {
        data[i]["display_state"] = 0;
    }

    // clear the old entries
    in_ul_list.selectAll("li").remove();

    // logic gate
    if (data == null) {
        return;
    }

    // populate the inspection reports list
    let items = in_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(2, minmax(0, 5fr)) repeat(2, minmax(0, 3fr)) repeat(2, minmax(0, 4fr))")
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            in_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // delete the set
            in_ul_list_contextmenu.select("#context_menu_0").on("click", () => {
                inspections_delete_set(x.inspection_id, x.inspection_record_id, x.item, x.drawing);
                in_ul_list_contextmenu.style("display", "none");
            });

            // prevent the default behavior
            e.preventDefault();
        });
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .attr("type", "datetime-local")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.timestamp)
        .on("change", (e, x) => {
            x.timestamp = e.srcElement.value;
            e.srcElement.blur();
        });
    let employees = items.append("select")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark");
    items.append("input")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "1")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.part_index)
        .on("drag", (e, _) => e.preventDefault)
        .on("drop", (e, _) => e.preventDefault)
        .on("change", (e, x) => {
            x.part_index = e.srcElement.value;
            e.srcElement.blur();
        })
        .on("click", (e, _) => {
            e.srcElement.select();
        });
    items.append("input")
        .style("--grid-column", "4")
        .style("--grid-row", "1")
        .attr("type", "text")
        .attr("disabled", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.revision);
    let inspection_types = items.append("select")
        .style("--grid-column", "5")
        .style("--grid-row", "1")
        .attr("class", "list-item-select-dark");
    items.append("input")
        .style("--grid-column", "6")
        .style("--grid-row", "1")
        .attr("type", "checkbox")
        .attr("class", "list-item-switch-dark")
        .property("checked", (x) => x.display_state)
        .on("change", (e, x) => {
            x.display_state = e.srcElement.checked;
            features_get_filtered_features(x.inspection_record_id, x.item, x.drawing);
        });

    // populate the employee options & value
    employees.selectAll("option")
        .data(glist_employees)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    employees.property("value", (x) => x.employee_id)
        .on("change", (e, x) => {
            x.employee_id = parseInt(e.srcElement.value);
        });

    // populate the inspection type options and value
    inspection_types.selectAll("option")
        .data(glist_inspection_types)
        .join("option")
        .attr("value", (x) => x.id)
        .text((x) => x.name);
    inspection_types.property("value", (x) => x.inspection_type_id)
        .on("change", (e, x) => {
            x.inspection_type_id = parseInt(e.srcElement.value);
        });
}

async function inspections_update_set_schemas(inspection_record_id)
{
    await d3.json("/inspection_records/inspections/get_filtered_schemas/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            search_term: in_input_schema_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            in_select_schema.selectAll("option").remove();

            // repopulate the selector
            in_select_schema.selectAll("option")
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

async function inspections_update_employees()
{
    await d3.json("/get_filtered_employees/", {
        method: "POST",
        body: JSON.stringify({
            search_term: in_input_employee_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            in_select_employee.selectAll("option").remove();

            // repopulate the selector
            in_select_employee.selectAll("option")
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

// #region features

async function features_prepare_panel(inspection_record_id, item, drawing)
{
    // clear out filters
    in_input_schema_filter.property("value", "");
    in_input_employee_filter.property("value", "");

    // populate the selectors
    await features_get_filter_parameters(inspection_record_id, item, drawing);

    // set up static input events
    ft_input_name.on("click", (e, _) => { e.srcElement.select(); });

    // set up static button events
    ft_button_update_display.on("click", () => features_get_filtered_features(inspection_record_id, item, drawing));
    ft_button_save_characteristics.on("click", features_save_features);

    // populate the measurements table
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function features_get_filtered_features(inspection_record_id, item, drawing)
{
    // get the list of measurement sets
    let inspections = [];
    in_ul_list.selectAll("li").data().forEach((e) => {
        inspections.push({
            inspection_id: e.inspection_id,
            display_state: e.display_state
        });
    });

    // logic gate
    if (inspections.length == 0) {
        return;
    }

    // query the database
    await d3.json("/inspection_records/features/get_filtered_features/", {
        method: "POST",
        body: JSON.stringify({
            identity: {
                inspection_record_id: inspection_record_id,
                item: item,
                drawing: drawing
            },
            content: {
                has_deviations: ft_select_has_deviations.property("value"),
                inspection_type_id: ft_select_inspection_type.property("value"),
                employee_id: ft_select_inspector.property("value"),
                part_index: ft_select_part_index.property("value"),
                revision: ft_select_revision.property("value"),
                name: ft_input_name.property("value"),
                frequency_type_id: ft_select_frequency_type.property("value"),
                gauge_id: ft_select_gauge.property("value"),
                gauge_type_id: ft_select_gauge_type.property("value"),
                specification_type_id: ft_select_specification_type.property("value"),
                dimension_type_id: ft_select_dimension_type.property("value"),
                inspections: inspections
            }
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // the table must always be reset
        vw_features_table.selectAll("thead").remove();
        vw_features_table.selectAll("tbody").remove();

        if (json.status == "ok") {

            // repopulate the characteristic table
            features_repopulate_table(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function features_save_features()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reversed. Continue?")) {
        return;
    }

    // query the flask server
    d3.json("/inspection_records/features/save_features/", {
        method: "POST",
        body: JSON.stringify({
            data: vw_features_table.select("tbody").selectAll("td").data()
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

async function features_tunnel_to_physical_part(inspection_record_id, part_id, part_index)
{
    await d3.json("/inspection_records/features/tunnel_to_physical_part/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            part_id: part_id,
            part_index: part_index
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // the table must always be reset
        vw_features_table.selectAll("thead").remove();
        vw_features_table.selectAll("tbody").remove();

        if (json.status == "ok") {

            // repopulate the characteristic table
            features_repopulate_table(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function features_view_deviations(feature_id, part_index, revision, name, inspection_record_id, item, drawing)
{
    // close any panel that is already open
    if (open_panel != null && open_panel != "deviations") {
        await toggle_options(open_panel, "0px");
    }

    // prepare the deviations panel
    await deviations_prepare_panel(feature_id, part_index, revision, name, inspection_record_id, item, drawing);

    // open the deviations panel
    if (open_panel != "deviations")
        await toggle_options("deviations", "1000px");
}

async function features_get_filter_parameters(inspection_record_id, item, drawing)
{
    await d3.json("/inspection_reports/features/get_filter_parameters/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
            item: item,
            drawing: drawing
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // update the inspection types
            ft_select_inspection_type.selectAll("option").remove();
            json.response.inspection_types.unshift({ id: -1, name: "n/a" });
            ft_select_inspection_type.selectAll("option")
                .data(json.response.inspection_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the part index
            ft_select_part_index.selectAll("option").remove();
            json.response.part_indices.unshift({ id: -1, name: "n/a" });
            ft_select_part_index.selectAll("option")
                .data(json.response.part_indices)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the revision
            ft_select_revision.selectAll("option").remove();
            json.response.revisions.unshift({ id: "", name: "n/a" });
            ft_select_revision.selectAll("option")
                .data(json.response.revisions)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the frequency types
            ft_select_frequency_type.selectAll("option").remove();
            json.response.frequency_types.unshift({ id: -1, name: "n/a" });
            ft_select_frequency_type.selectAll("option")
                .data(json.response.frequency_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the inspectors
            ft_select_inspector.selectAll("option").remove();
            json.response.inspectors.unshift({ id: -1, name: "n/a" });
            ft_select_inspector.selectAll("option")
                .data(json.response.inspectors)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauges
            ft_select_gauge.selectAll("option").remove();
            json.response.gauges.unshift({ id: -1, name: "n/a" });
            ft_select_gauge.selectAll("option")
                .data(json.response.gauges)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the gauge types
            ft_select_gauge_type.selectAll("option").remove();
            json.response.gauge_types.unshift({ id: -1, name: "n/a" });
            ft_select_gauge_type.selectAll("option")
                .data(json.response.gauge_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the specification types
            ft_select_specification_type.selectAll("option").remove();
            json.response.specification_types.unshift({ id: -1, name: "n/a" });
            ft_select_specification_type.selectAll("option")
                .data(json.response.specification_types)
                .join("option")
                .attr("value", (x) => x.id)
                .text((x) => x.name);

            // update the dimension types
            ft_select_dimension_type.selectAll("option").remove();
            json.response.dimension_types.unshift({ id: -1, name: "n/a" });
            ft_select_dimension_type.selectAll("option")
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

async function features_repopulate_table(data)
{
    // get the current display type
    let display_type = ft_select_display_type.property("value");

    // table schema
    let table_schema = main_table_columns[display_type];

    // clear the old columns
    vw_features_table.selectAll("thead").remove();

    // clear the old rows
    vw_features_table.selectAll("tbody").remove();

    // logic gate
    if (data == null) {
        return;
    }

    // add the columns
    vw_features_table.append("thead")
        .selectAll("tr")
        .data(table_schema)
        .join("th")
        .attr("scope", "col")
        .style("width", (x) => x.width)
        .text((x) => x.col.display);    

    // add the rows
    let rows = vw_features_table.append("tbody")
        .selectAll("tr")
        .data(data)
        .join("tr")
        .on("mouseenter", (e, x) => {
            switch (x.state) {
                case "pass":
                    e.srcElement.style.backgroundColor = pass_hover;
                    break;
                case "fail":
                    e.srcElement.style.backgroundColor = fail_hover;
                    break;
                case "incomplete":
                    e.srcElement.style.backgroundColor = incomplete_hover;
                    break;
                default:
                    e.srcElement.style.backgroundColor = "inherit";
            }
        })
        .on("mouseleave", (e, x) => {
            switch (x.state) {
                case "pass":
                    e.srcElement.style.backgroundColor = pass_static;
                    break;
                case "fail":
                    e.srcElement.style.backgroundColor = fail_static;
                    break;
                case "incomplete":
                    e.srcElement.style.backgroundColor = incomplete_static;
                    break;
                default:
                    e.srcElement.style.backgroundColor = "inherit";
            }
        })
        .on("mousedown", (e, x) => {
            switch (x.state) {
                case "pass":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = pass_active;
                    break;
                case "fail":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = fail_active;
                    break;
                case "incomplete":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = incomplete_active;
                    break;
                default:
                    e.srcElement.parentElement.parentElement.style.backgroundColor = "inherit";
            }
        })
        .on("mouseup", (e, x) => {
            switch (x.state) {
                case "pass":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = pass_hover;
                    break;
                case "fail":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = fail_hover;
                    break;
                case "incomplete":
                    e.srcElement.parentElement.parentElement.style.backgroundColor = incomplete_hover;
                    break;
                default:
                    e.srcElement.parentElement.parentElement.style.backgroundColor = "inherit";
            }
        })
        .on("click", (_, x) => deviations_prepare_panel(x.feature_id, x.part_index, x.revision, x.name, x.inspection_record_id, x.item, x.drawing))
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            vw_features_table_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block");

            // tunnel to physical part
            vw_features_table_contextmenu.select("#context_menu_0").on("click", () => {
                features_tunnel_to_physical_part(x.inspection_record_id, x.part_id, x.part_index);
                vw_features_table_contextmenu.style("display", "none");
            });

            // view deviations
            vw_features_table_contextmenu.select("#context_menu_1").on("click", () => {
                features_view_deviations(x.feature_id, x.part_index, x.revision, x.name, x.inspection_record_id, x.item, x.drawing);
                vw_features_table_contextmenu.style("display", "none");
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
                        usl: r.usl,
                        lsl: r.lsl,
                        has_deviations: r.has_deviations,
                        precision: r.precision,
                        feature_id: r.feature_id,
                        part_index: r.part_index,
                        inspection_id: r.inspection_id,
                        gauge_type_id: r.gauge_type_id,
                        part_id: r.part_id,
                        inspection_record_id: r.inspection_record_id,
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
                    if (x.column.key == "name" && x.row.has_deviations) {
                        return `**${x.row.value}`;
                    }
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
        .style("cursor", "text")
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
            let row_data = d3.select(e.srcElement.parentElement.parentElement).data()[0];
            row_data.measured = x.row.value;
            if (x.column.datatype == "decimal" && !isNaN(x.row.value)) {
                e.srcElement.value = x.row.value.toFixed(x.row.precision);
            }
            features_apply_row_color(e.srcElement.parentElement.parentElement, row_data.measured, row_data.usl, row_data.lsl, row_data.precision);
            e.srcElement.blur();
        }).on("keydown", (e, _) => {
            if (e.keyCode == 13) {
                e.srcElement.blur();
            }
        }).on("click", (e, _) => {
            e.srcElement.select();
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

    // assign color codes
    await features_apply_color_code();
}

async function features_apply_color_code()
{
    vw_features_table.select("tbody").node().childNodes.forEach((row) => {
        let row_data = d3.select(row).data()[0];
        features_apply_row_color(row, row_data.measured, row_data.usl, row_data.lsl, row_data.precision);
    });
}

async function features_apply_row_color(r, input_measured, input_usl, input_lsl, precision)
{
    // logic gate
    if (isNaN(input_measured) || input_measured == null) {
        r.style.backgroundColor = incomplete_static;
        d3.select(r).data()[0].state = "incomplete";
        return;
    }

    // extract info
    let measured = Number(input_measured.toFixed(precision));
    let usl = Number(input_usl.toFixed(precision));
    let lsl = Number(input_lsl.toFixed(precision));

    // apply condition
    if (!(lsl <= measured && measured <= usl)) {
        r.style.backgroundColor = fail_static;
        d3.select(r).data()[0].state = "fail";
    }
    else {
        r.style.backgroundColor = pass_static;
        d3.select(r).data()[0].state = "pass";
    }
}

// #endregion

// #region manufactured

async function manufactured_prepare_panel(inspection_record_id)
{
    // clear the inputs
    mn_input_job_number_search.property("value", "");
    mn_input_part_search.property("value", "");
    mn_input_job_number_display_filter.property("value", "");

    // populate the new association selects
    await manufactured_get_filtered_job_orders();
    await manufactured_get_filtered_parts(inspection_record_id);

    // set up static button events
    mn_button_add_job_order.on("click", () => { manufactured_add_associated_job_order(inspection_record_id); });
    mn_button_save_job_order.on("click", manufactured_save_associated_job_order);

    // set up static input events
    mn_input_job_number_search.on("change", manufactured_get_filtered_job_orders);
    mn_input_part_search.on("change", () => { manufactured_get_filtered_parts(inspection_record_id); });
    mn_input_job_number_display_filter.on("change", () => { manufactured_get_associated_job_orders(inspection_record_id); });

    // populate the association list
    await manufactured_get_associated_job_orders(inspection_record_id);
}

async function manufactured_add_associated_job_order(inspection_record_id)
{
    await d3.json("/inspection_records/manufactured/add_associated_job_number/", {
        method: "POST",
        body: JSON.stringify({
            search_term: mn_input_job_number_display_filter.property("value"),
            inspection_record_id: inspection_record_id,
            part_id: mn_select_part.property("value"),
            job_number_id: mn_select_job_order.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            manufactured_repopulate_association_list(json.response, inspection_record_id);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function manufactured_save_associated_job_order()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/manufactured/save_associated_job_numbers/", {
        method: "POST",
        body: JSON.stringify({
            data: mn_ul_list.selectAll("li").data()
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

async function manufactured_delete_associated_job_order(inspection_record_id, job_number_id, part_id)
{
    // request confirmation
    if (!confirm("This action will delete from the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/manufactured/delete_associated_job_number/", {
        method: "POST",
        body: JSON.stringify({
            search_term: mn_input_job_number_display_filter.property("value"),
            inspection_record_id: inspection_record_id,
            part_id: part_id,
            job_number_id: job_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            manufactured_repopulate_association_list(json.response, inspection_record_id);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function manufactured_get_associated_job_orders(inspection_record_id)
{
    await d3.json("/inspection_records/manufactured/get_associated_job_numbers/", {
        method: "POST",
        body: JSON.stringify({
            search_term: mn_input_job_number_display_filter.property("value"),
            inspection_record_id: inspection_record_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // always reset the list
        mn_ul_list.selectAll("li").remove();

        // interpret the output
        if (json.status == "ok") {
            manufactured_repopulate_association_list(json.response, inspection_record_id);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function manufactured_repopulate_association_list(data, inspection_record_id)
{
    // clear the old entries
    mn_ul_list.selectAll("li").remove();

    // logic gate
    if (data == null) {
        return;
    }

    // populate the inspection reports list
    let items = mn_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(1, minmax(0, 1fr)) repeat(4, minmax(0, 2fr))")
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            mn_ul_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block")
            
            // delete the job order
            mn_ul_list_contextmenu.select("#context_menu_0").on("click", async () => {
                manufactured_delete_associated_job_order(inspection_record_id, x.id, x.part_id);
                mn_ul_list_contextmenu.style("display", "none");
            });

            // prevent default behavior
            e.preventDefault();
        });
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px 0px 0px 6px")
        .attr("type", "text")
        .attr("disabled", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.revision);
    items.append("input")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .attr("type", "text")
        .attr("disabled", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.name);
    items.append("input")
        .style("--grid-column", "3")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.full_inspect_interval)
        .on("change", (e, x) => {
            x.full_inspect_interval = parseInt(e.srcElement.value);
            e.srcElement.blur();
        })
        .on("click", (e, _) => {
            e.srcElement.select();
        });
    items.append("input")
        .style("--grid-column", "4")
        .style("--grid-row", "1")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.released_qty)
        .on("change", (e, x) => {
            x.released_qty = parseInt(e.srcElement.value);
            e.srcElement.blur();
        })
        .on("click", (e, _) => {
            e.srcElement.select();
        });
    items.append("input")
        .style("--grid-column", "5")
        .style("--grid-row", "1")
        .style("border-radius", "0px 6px 6px 0px")
        .attr("type", "number")
        .attr("step", "any")
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.completed_qty)
        .on("change", (e, x) => {
            x.completed_qty = parseInt(e.srcElement.value);
            e.srcElement.blur();
        })
        .on("click", (e, _) => {
            e.srcElement.select();
        });
}

async function manufactured_get_filtered_job_orders()
{
    await d3.json("/inspection_records/manufactured/get_filtered_job_numbers/", {
        method: "POST",
        body: JSON.stringify({
            search_term: mn_input_job_number_search.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            mn_select_job_order.selectAll("option").remove();

            // add new entries
            mn_select_job_order.selectAll("option")
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

async function manufactured_get_filtered_parts(inspection_record_id)
{
    await d3.json("/inspection_records/manufactured/get_filtered_parts/", {
        method: "POST",
        body: JSON.stringify({
            search_term: mn_input_part_search.property("value"),
            inspection_record_id: inspection_record_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            mn_select_part.selectAll("option").remove();

            // add new entries
            mn_select_part.selectAll("option")
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

// #region received

async function received_prepare_panel(inspection_record_id)
{
    // clear the inputs
    rc_input_receiver_number_search.property("value", "");
    rc_input_receiver_number_display_filter.property("value", "");
    rc_input_purchase_order_search.property("value", "");
    rc_input_purchase_order_display_filter.property("value", "");
    rc_input_supplier_search.property("value", "");

    // populate the selects
    await received_get_filtered_receiver_number_options();
    await received_get_filtered_purchase_order_options();
    await received_get_filtered_supplier_options();

    // set up static input events
    rc_input_receiver_number_search.on("change", received_get_filtered_receiver_number_options);
    rc_input_receiver_number_display_filter.on("change", () => { received_get_filtered_child_associations(inspection_record_id); });
    rc_input_purchase_order_search.on("change", received_get_filtered_purchase_order_options);
    rc_input_purchase_order_display_filter.on("change", () => { received_get_filtered_purchase_order_associations(inspection_record_id); });
    rc_input_supplier_search.on("change", received_get_filtered_supplier_options);

    // set up static button events
    rc_button_add_purchase_order.on("click", () => { received_assign_purchase_order_association(inspection_record_id); });
    rc_button_save_received_quantities.on("click", received_save_received_quantities);

    // populate the association lists
    await received_get_filtered_purchase_order_associations(inspection_record_id);
}

async function received_assign_purchase_order_association(inspection_record_id)
{
    await d3.json("/inspection_records/received/assign_purchase_order_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_purchase_order_display_filter.property("value"),
            inspection_record_id: inspection_record_id,
            purchase_order_id: rc_select_purchase_order.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_purchase_order_association_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function received_assign_receiver_number_association(purchase_order_id)
{
    await d3.json("/inspection_records/received/assign_receiver_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_receiver_number_display_filter.property("value"),
            purchase_order_id: purchase_order_id,
            receiver_number_id: rc_select_receiver_number.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_child_association_lists(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function received_set_associated_supplier(purchase_order_id)
{
    await d3.json("/inspection_records/received/set_associated_supplier/", {
        method: "POST",
        body: JSON.stringify({
            purchase_order_id: purchase_order_id,
            supplier_id: rc_select_supplier.property("value")
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

async function received_save_received_quantities()
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/received/save_received_quantities/", {
        method: "POST",
        body: JSON.stringify({
            data: rc_ul_receiver_number_list.selectAll("li").data()
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

async function received_delete_associated_purchase_order(inspection_record_id, purchase_order_id)
{
    await d3.json("/inspection_records/received/remove_purchase_order_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_purchase_order_display_filter.property("value"),
            inspection_record_id: inspection_record_id,
            purchase_order_id: purchase_order_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_purchase_order_association_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
    await received_purchase_order_unselected();
}

async function received_delete_associated_receiver_number(purchase_order_id, receiver_number_id)
{
    await d3.json("/inspection_records/received/remove_receiver_number_association/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_receiver_number_display_filter.property("value"),
            purchase_order_id: purchase_order_id,
            receiver_number_id: receiver_number_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_child_association_lists(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function received_get_filtered_purchase_order_associations(inspection_record_id)
{
    await d3.json("/inspection_records/received/get_filtered_purchase_order_associations/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_purchase_order_search.property("value"),
            inspection_record_id: inspection_record_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_purchase_order_association_list(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function received_get_filtered_child_associations(purchase_order_id)
{
    await d3.json("/inspection_records/received/get_filtered_child_associations/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_receiver_number_search.property("value"),
            purchase_order_id: purchase_order_id,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            received_repopulate_child_association_lists(json.response);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

async function received_repopulate_purchase_order_association_list(data)
{
    // clear the old entries
    rc_ul_purchase_order_list.selectAll("li").remove();

    // logic gate
    if (data == null) {
        return;
    }

    // populate the inspection reports list
    let items = rc_ul_purchase_order_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "repeat(1, minmax(0, 1fr))")
        .on("contextmenu", (e, x) => {

            // position and show the context menu
            rc_ul_purchase_order_list_contextmenu
                .style("position", "absolute")
                .style("left", `${e.pageX}px`)
                .style("top", `${e.pageY}px`)
                .style("display", "block")

            // delete the job order
            rc_ul_purchase_order_list_contextmenu.select("#context_menu_0").on("click", () => {
                received_delete_associated_purchase_order(x.inspection_record_id, x.purchase_order_id);
                rc_ul_purchase_order_list_contextmenu.style("display", "none");
            });

            // prevent default behavior
            e.preventDefault();
        })
        .on("click", (e, x) => {
            received_purchase_order_clicked(e, x);
        });
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("border-radius", "6px")
        .attr("disabled", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.name);
}

async function received_repopulate_child_association_lists(data)
{
    // clear the old entries
    rc_ul_receiver_number_list.selectAll("li").remove();

    // assign the supplier
    rc_select_supplier.property("value", data.supplier_id);

    // populate the receiver numbers list
    if (data.receiver_numbers != null) {
        let items = rc_ul_receiver_number_list.selectAll("li")
            .data(data.receiver_numbers)
            .join("li")
            .append("div")
            .attr("class", "list-item-dark")
            .style("--grid-template-columns", "repeat(2, minmax(0, 1fr))")
            .on("contextmenu", (e, x) => {

                // position and show the context menu
                rc_ul_receiver_number_list_contextmenu
                    .style("position", "absolute")
                    .style("left", `${e.pageX}px`)
                    .style("top", `${e.pageY}px`)
                    .style("display", "block")
                
                // delete the job order
                rc_ul_receiver_number_list_contextmenu.select("#context_menu_0").on("click", () => {
                    received_delete_associated_receiver_number(x.purchase_order_id, x.id);
                    rc_ul_receiver_number_list_contextmenu.style("display", "none");
                });

                // prevent default behavior
                e.preventDefault();
            });
        items.append("input")
            .style("--grid-column", "1")
            .style("--grid-row", "1")
            .style("border-radius", "6px 0px 0px 6px")
            .attr("type", "text")
            .attr("disabled", true)
            .attr("class", "list-item-input-dark")
            .property("value", (x) => x.name);
        items.append("input")
            .style("--grid-column", "2")
            .style("--grid-row", "1")
            .style("border-radius", "0px 6px 6px 0px")
            .attr("type", "number")
            .attr("step", "any")
            .attr("class", "list-item-input-dark")
            .property("value", (x) => x.received_qty)
            .on("change", (e, x) => {
                x.received_qty = parseInt(e.srcElement.value);
                e.srcElement.blur();
            })
            .on("click", (e, _) => {
                e.srcElement.select();
            });
    }

    
}

async function received_get_filtered_purchase_order_options()
{
    await d3.json("/inspection_records/received/get_filtered_purchase_order_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_purchase_order_search.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            rc_select_purchase_order.selectAll("option").remove();

            // add new entries
            rc_select_purchase_order.selectAll("option")
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

async function received_get_filtered_receiver_number_options()
{
    await d3.json("/inspection_records/received/get_filtered_receiver_number_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_receiver_number_search.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            rc_select_receiver_number.selectAll("option").remove();

            // add new entries
            rc_select_receiver_number.selectAll("option")
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

async function received_get_filtered_supplier_options()
{
    await d3.json("/inspection_records/received/get_filtered_supplier_options/", {
        method: "POST",
        body: JSON.stringify({
            search_term: rc_input_supplier_search.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // clear the old entries
            rc_select_supplier.selectAll("option").remove();

            // add the null condition
            json.response.unshift({ id: -1, name: "n/a" });

            // add new entries
            rc_select_supplier.selectAll("option")
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

async function received_purchase_order_clicked(event, data)
{
    // check if the item is already selected
    let is_selected = event.srcElement.parentNode.classList.contains("list-item-dark-selected");

    // reset/set the selected class
    for (let i = 0; i < rc_ul_purchase_order_list.node().childNodes.length; i++) {
        let current_node = rc_ul_purchase_order_list.node().childNodes[i].children[0];
        current_node.classList.remove("list-item-dark-selected");
    }

    // filter actions
    if (!is_selected) {
        await received_purchase_order_selected(event, data);
    }
    else {
        await received_purchase_order_unselected();
    }
}

async function received_purchase_order_selected(event, data)
{
    // set the visual flags
    event.srcElement.parentNode.classList.add("list-item-dark-selected");

    // populate the supplier selector and receiver numbers
    received_get_filtered_child_associations(data.purchase_order_id);

    // set the events
    rc_select_supplier.on("change", () => { received_set_associated_supplier(data.purchase_order_id); });
    rc_button_add_receiver_number.on("click", () => { received_assign_receiver_number_association(data.purchase_order_id); });
}

async function received_purchase_order_unselected()
{
    // depopulate the supplier selector
    rc_select_supplier.property("value", -1);

    // depopulate the receiver numbers
    rc_ul_receiver_number_list.selectAll("li").remove();

    // unset the supplier event
    rc_select_supplier.on("change", null);
    rc_button_add_receiver_number.on("click", null);
}

// #endregion

// #region lot numbers

async function lot_numbers_prepare_panel(inspection_record_id)
{
    // clear the inputs
    ln_input_selected_search_term.property("value", "");
    ln_input_search_term.property("value", "");

    // populate the selector
    await lot_numbers_update_filtered_selector();

    // set up static input events
    ln_input_selected_search_term.on("change", lot_numbers_update_filtered_selector);
    ln_input_selected_search_term.on("click", (e, _) => { e.srcElement.select(); });
    ln_input_search_term.on("change", () => lot_numbers_update_filtered_list(inspection_record_id));
    ln_input_search_term.on("click", (e, _) => { e.srcElement.select(); });

    // set up static button events
    ln_button_add.on("click", () => lot_numbers_assign_association(inspection_record_id));

    // populate the list
    await lot_numbers_update_filtered_list(inspection_record_id);
}

async function lot_numbers_assign_association(inspection_record_id)
{
    // request confirmation
    if (!confirm("This action will write to the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/lot_numbers/assign_lot_number/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ln_input_search_term.property("value"),
            inspection_record_id: inspection_record_id,
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

async function lot_numbers_remove_association(inspection_record_id, id)
{
    // request confirmation
    if (!confirm("This action will remove records from the database and cannot be reverted. Continue?")) {
        return;
    }

    // query the flask server
    await d3.json("/inspection_records/lot_numbers/unassign_lot_number/", {
        method: "POST",
        body: JSON.stringify({
            search_term: ln_input_search_term.property("value"),
            inspection_record_id: inspection_record_id,
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
    await d3.json("/inspection_records/lot_numbers/get_filtered_options/", {
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

            // logic gate
            if (json.response == null) {
                return;
            }

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

async function lot_numbers_update_filtered_list(inspection_record_id)
{
    await d3.json("/inspection_records/lot_numbers/get_filtered_associations/", {
        method: "POST",
        body: JSON.stringify({
            inspection_record_id: inspection_record_id,
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
    if (data == null) {
        return;
    }

    // populate the list
    let items = ln_ul_list.selectAll("li")
        .data(data)
        .join("li")
        .append("div")
        .attr("class", "list-item-dark")
        .style("--grid-template-columns", "3fr 1fr");
    items.append("input")
        .style("--grid-column", "1")
        .style("--grid-row", "1")
        .style("text-align", "left")
        .style("border-radius", "6px 0px 0px 6px")
        .attr("type", "text")
        .attr("disabled", true)
        .attr("class", "list-item-input-dark")
        .property("value", (x) => x.name);
    items.append("button")
        .style("--grid-column", "2")
        .style("--grid-row", "1")
        .style("border-radius", "0px 6px 6px 0px")
        .attr("class", "list-item-button-dark")
        .text("Delete")
        .on("click", (_, x) => lot_numbers_remove_association(x.inspection_record_id, x.id));
}

// #endregion

// #region deviations

async function deviations_prepare_panel(feature_id, part_index, revision, name, inspection_record_id, item, drawing)
{
    // set the visual flag
    dv_label_current.text(`${part_index} // ${revision} // ${name}`);

    // clear inputs
    dv_input_notes.property("value", "");

    // clear the list
    dv_ul_list.selectAll("li").remove();

    // set up static input events
    dv_input_notes.on("click", (e, _) => { e.srcElement.select(); });

    // set up static button events
    dv_button_add.on("click", () => deviations_add(feature_id, inspection_record_id, item, drawing));
    dv_button_save.on("click", () => deviations_save(feature_id));

    // populate the list
    await deviations_get_measurement_deviations(feature_id, inspection_record_id, item, drawing);
}

async function deviations_add(feature_id, inspection_record_id, item, drawing)
{
    // add a new deviation
    await d3.json("/inspection_reports/deviations/add_deviation/", {
        method: "POST",
        body: JSON.stringify({
            feature_id: feature_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, feature_id, inspection_record_id, item, drawing);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // requery for measurements
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function deviations_save(feature_id)
{
    await d3.json("/inspection_records/deviations/save_deviations/", {
        method: "POST",
        body: JSON.stringify({
            feature_id: feature_id,
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

async function deviations_delete(feature_id, deviation_id, inspection_record_id, item, drawing)
{
    await d3.json("/inspection_reports/deviations/delete_deviation/", {
        method: "POST",
        body: JSON.stringify({
            feature_id: feature_id,
            deviation_id: deviation_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // clear the old entries every time
        dv_ul_list.selectAll("li").remove();

        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, feature_id, inspection_record_id, item, drawing);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });

    // requery for measurements
    await features_get_filtered_features(inspection_record_id, item, drawing);
}

async function deviations_get_measurement_deviations(feature_id, inspection_record_id, item, drawing)
{
    await d3.json("/inspection_reports/deviations/get_feature_deviations/", {
        method: "POST",
        body: JSON.stringify({
            feature_id: feature_id
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            deviations_repopulate_deviations_list(json.response, feature_id, inspection_record_id, item, drawing);
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

async function deviations_repopulate_deviations_list(data, feature_id, inspection_record_id, item, drawing)
{
    // clear the old entries
    dv_ul_list.selectAll("li").remove();

    // logic gate
    if (data == null) {
        return;
    }

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
                deviations_delete(feature_id, x.id, inspection_record_id, item, drawing);
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
    if (destination_arg == "inspection_records") {
        if (document.getElementById("inspection_records_sidebar").style.width == open_width) {
            document.getElementById("inspection_records_sidebar").style.width = close_width;
            document.getElementById("inspection_records_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("inspection_records_sidebar").style.width = open_width;
            document.getElementById("inspection_records_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "inspections") {
        if (document.getElementById("inspections_sidebar").style.width == open_width) {
            document.getElementById("inspections_sidebar").style.width = close_width;
            document.getElementById("inspections_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("inspections_sidebar").style.width = open_width;
            document.getElementById("inspections_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "features") {
        if (document.getElementById("features_sidebar").style.width == open_width) {
            document.getElementById("features_sidebar").style.width = close_width;
            document.getElementById("features_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("features_sidebar").style.width = open_width;
            document.getElementById("features_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "manufactured") {
        if (document.getElementById("manufactured_sidebar").style.width == open_width) {
            document.getElementById("manufactured_sidebar").style.width = close_width;
            document.getElementById("manufactured_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("manufactured_sidebar").style.width = open_width;
            document.getElementById("manufactured_btn").style.marginRight = open_width;
            open_panel = destination_arg;
        }
    }
    else if (destination_arg == "received") {
        if (document.getElementById("received_sidebar").style.width == open_width) {
            document.getElementById("received_sidebar").style.width = close_width;
            document.getElementById("received_btn").style.marginRight = close_width;
            open_panel = null;
        }
        else {
            document.getElementById("received_sidebar").style.width = open_width;
            document.getElementById("received_btn").style.marginRight = open_width;
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
