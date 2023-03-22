// control definitions
let existing_report_button = d3.select("#existing_report_button");
let existing_report_table = d3.select("#existing_reports_table");
let existing_report_filter_type = d3.select("#existing_report_filter_type");
let existing_report_filter_term = d3.select("#existing_report_filter_term");
let existing_report_filter_apply = d3.select("#existing_report_filter_apply");
let existing_report_start_date = d3.select("#existing_report_start_date");
let existing_report_stop_date = d3.select("#existing_report_stop_date");
let existing_report_use_date = d3.select("#existing_report_use_date");

// add events
existing_report_button.on("click", update_existing_reports_panel);
existing_report_filter_apply.on("click", update_existing_reports_panel);

init();

// initialization function
function init()
{
    // set initial values
    existing_report_start_date.property("value", "2023-01-01");
    existing_report_stop_date.property("value", "2023-02-01");
    existing_report_use_date.property("checked", false);
}

// update the existing reports panel
function update_existing_reports_panel()
{
    // define the filter
    let filter_type = existing_report_filter_type.property("value");
    let filter_term = existing_report_filter_term.property("value");
    let start_date = new Date(existing_report_start_date.property("value") + "T00:00:00");
    let stop_date = new Date(existing_report_stop_date.property("value") + "T00:00:00");
    let use_date = existing_report_use_date.property("checked");
    let start_day = start_date.getDate();
    let start_month = start_date.getMonth() + 1;
    let start_year = start_date.getFullYear();
    let stop_day = stop_date.getDate();
    let stop_month = stop_date.getMonth() + 1;
    let stop_year = stop_date.getFullYear();

    // make sure the filter term is not null
    if (filter_term == "") { filter_term = "null"; }

    // define the route
    let route = `get_inspection_reports/${filter_type}/${filter_term}/${use_date}/${start_day}/${start_month}/${start_year}/${stop_day}/${stop_month}/${stop_year}/`;

    // query the database for inspection reports
    d3.json(route).then(function (returned_object) {
        if (returned_object.status == "ok") {

            // extract data from the returned object
            let dataset = returned_object.response;

            // remove previous data
            existing_report_table.selectAll("tbody").remove();

            // create the table rows & attach the row click event
            let rows = existing_report_table.append("tbody").selectAll("tr")
                .data(dataset)
                .enter()
                .append("tr")
                .on("click", (p, data) => inspection_report_selected(data.drawing));

            // assign the cell contents
            rows.selectAll("td")
                .data(function (row) {
                    return ["drawing", "item_number", "revision", "started", "finished"].map(function (column) {
                        return { column: column, value: row[column] };
                    });
                })
                .enter()
                .append("td")
                .text((x) => x.value);
        }
        else if (returned_object.status == "not_ok") {

            // remove previous data
            existing_report_table.selectAll("tbody").remove();

            // log the error message
            console.log(returned_object.response);
        }
    });
}

function inspection_report_selected(drawing)
{
    console.log(drawing);
}