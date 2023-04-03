

// existing inspection report controls
let eir_item_number = d3.select("#select_report_item_number");
let eir_drawing = d3.select("#select_report_drawing");
let eir_start_after = d3.select("#select_report_start");
let eir_finish_before = d3.select("#select_report_finish");




init();

function init()
{
    // set the initial dates for date selectors
    eir_start_after.property("value", "1970-01-01");
    eir_finish_before.property("value", "2100-01-01");
}

// toggle the open/close state for the sidebar buttons
function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "existing") {
        if (document.getElementById("inspection_report_existing_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_existing_sidebar").style.width = close_width;
            document.getElementById("inspection_report_existing").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_existing_sidebar").style.width = open_width;
            document.getElementById("inspection_report_existing").style.marginLeft = open_width;
            get_inspection_reports();
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
}

function get_inspection_reports()
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
    route = `/get_all_inspection_reports/<${item_number}/${drawing}/${start_day}/${start_month}/${start_year}/${finish_day}/${finish_month}/${finish_year}/`;

    // run the server request
    d3.json(route).then((returned_object) => {

    });
}

function inspection_report_selected(row_html)
{
    let cells = row_html.getElementsByTagName("td");

    let item_number = cells[0].innerHTML;
    let drawing = cells[1].innerHTML;
    let revision = cells[2].innerHTML;
    let start_date = cells[3].innerHTML;
    let finish_date = cells[4].innerHTML;
}