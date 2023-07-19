
// controls
const button_data_entry = d3.select("#data_entry_btn");
const input_part_id_filter = d3.select("#part_id_filter");
const select_part_id = d3.select("#part_id");
const select_part_revision = d3.select("#part_revision");
const input_job_number_filter = d3.select("#job_number_filter");
const select_job_number = d3.select("#job_number");
const input_purchase_order = d3.select("#purchase_order_filter");
const select_purchase_order = d3.select("#purchase_order");

// initialize the page
init();

// initialization function
async function init()
{
    // populate the part id selector
    await update_part_ids();

    // populate the part revision selector
    await update_part_revisions();

    // populate the associations
    await update_associations();

    // assign input events
    input_part_id_filter.on("change", update_part_ids);

    // assign select events
    select_part_id.on("change", async () => {
        await update_part_revisions();
        await update_associations();
    });
    select_part_revision.on("change", update_associations);

    // assign button events
    button_data_entry.on("click", get_inspection_record_document);
}

// generate excel document for data entry
async function generate_excel_document()
{
    await d3.json("/qa1_data_portal/generate_excel_document/", {
        method: "POST",
        body: JSON.stringify({
            part_id: select_part_id.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

        }
        else if (json.status == "log"){
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// update part ids
async function update_part_ids()
{
    await d3.json("/qa1_data_portal/update_part_ids/", {
        method: "POST",
        body: JSON.stringify({
            part_id_filter: input_part_id_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // reset the dropdown
            select_part_id.selectAll("option").remove();

            // logic gate
            if (json.response == null) {
                return;
            }

            // populate the dropdown
            select_part_id.selectAll("option")
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

// update part revisions
async function update_part_revisions()
{
    await d3.json("/qa1_data_portal/update_part_revisions/", {
        method: "POST",
        body: JSON.stringify({
            part_id: select_part_id.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // reset the dropdown
            select_part_revision.selectAll("option").remove();

            // logic gate
            if (json.response == null) {
                return;
            }

            // populate the dropdown
            select_part_revision.selectAll("option")
                .data(json.response)
                .join("option")
                .attr("value", (x) => x.revision)
                .text((x) => x.revision);
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// find matching job numbers & purchase orders
async function update_associations()
{
    await d3.json("/qa1_data_portal/get_associations/", {
        method: "POST",
        body: JSON.stringify({
            part_id: select_part_id.property("value"),
            part_revision: select_part_revision.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // reset the dropdowns
            select_job_number.selectAll("option").remove();
            select_purchase_order.selectAll("option").remove();

            // populate job numbers
            if (json.response.job_numbers != null) {
                select_job_number.attr("disabled", null);
                select_job_number.selectAll("option")
                    .data(json.response.job_numbers)
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
            else {
                select_job_number.attr("disabled", true);
                select_job_number.selectAll("option")
                    .data([{ id: -1, name: "n/a" }])
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }

            // populate purchase orders
            if (json.response.purchase_orders != null) {
                select_purchase_order.attr("disabled", null);
                select_purchase_order.selectAll("option")
                    .data(json.response.purchase_orders)
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
            else {
                select_purchase_order.attr("disabled", true);
                select_purchase_order.selectAll("option")
                    .data([{ id: -1, name: "n/a" }])
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.status == "alert") {
            alert(json.response);
        }
    });
}

// get the matching inspection record (excel document)
async function get_inspection_record_document()
{
    await d3.json("/qa1_data_portal/get_inspection_record/", {
        method: "POST",
        body: JSON.stringify({
            part_id: select_part_id.property("value"),
            part_revision: select_part_revision.property("value"),
            job_number: select_job_number.property("value"),
            purchase_order: select_purchase_order.property("value")
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
