function toggle_options(destination_arg, open_width)
{
    let close_width = "0px";
    if (destination_arg == "controls") {
        if (document.getElementById("inspection_report_controls_sidebar").style.width == open_width) {
            document.getElementById("inspection_report_controls_sidebar").style.width = close_width;
            document.getElementById("inspection_report_controls").style.marginLeft = close_width;
        }
        else {
            document.getElementById("inspection_report_controls_sidebar").style.width = open_width;
            document.getElementById("inspection_report_controls").style.marginLeft = open_width;
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