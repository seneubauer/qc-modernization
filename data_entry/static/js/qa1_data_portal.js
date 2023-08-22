
// controls
const button_open_workbook = d3.select("#open_workbook_btn");
const button_close_workbook = d3.select("#close_workbook_btn");
const input_employee_id_filter = d3.select("#employee_id_filter");
const select_employee_id = d3.select("#employee_id");
const input_part_id_filter = d3.select("#part_id_filter");
const select_part_id = d3.select("#part_id");
const select_part_revision = d3.select("#part_revision");
const input_job_number_filter = d3.select("#job_number_filter");
const select_job_number = d3.select("#job_number");
const input_purchase_order = d3.select("#purchase_order_filter");
const select_purchase_order = d3.select("#purchase_order");
const select_receiver_number = d3.select("#receiver_number");
const check_existing_associations = d3.select("#use_existing_associations");

// initialize the page
init();

// initialization function
async function init()
{
    // populate the employee selector
    await update_employees();

    // populate the part id selector
    await update_part_ids();

    // populate the part revision selector
    await update_part_revisions();

    // populate the associations
    await update_associations();

    // populate the receiver numbers
    await update_receiver_numbers();

    // assign input events
    input_employee_id_filter.on("change", update_employees);
    input_part_id_filter.on("change", update_part_ids);

    // assign select events
    select_part_id.on("change", async () => {
        await update_part_revisions();
        await update_associations();
        await update_receiver_numbers();
    });
    select_part_revision.on("change", async () => {
        await update_associations();
        await update_receiver_numbers();
    });
    select_purchase_order.on("change", async () => {
        await update_receiver_numbers();
    });

    // assign toggle events
    check_existing_associations.on("change", async () => {
        await update_associations();
        await update_receiver_numbers();
    });

    // assign button events
    button_open_workbook.on("click", get_inspection_record_document);
    button_close_workbook.on("click", set_inspection_record_document);
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

// update employees
async function update_employees()
{
    await d3.json("/qa1_data_portal/update_employees/", {
        method: "POST",
        body: JSON.stringify({
            employee_id_filter: input_employee_id_filter.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {

        // reset the dropdown
        select_employee_id.selectAll("option").remove();

        // logic gate
        if (json.response == null) {
            return;
        }

        // populate the dropdown
        select_employee_id.selectAll("option")
            .data(json.response)
            .join("option")
            .attr("value", (x) => x.id)
            .text((x) => x.name);
    })
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
            part_revision: select_part_revision.property("value"),
            use_existing_associations: check_existing_associations.property("checked")
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
                json.response.job_numbers.unshift({ id: -1, name: "n/a" });
                input_job_number_filter.attr("disabled", null);
                select_job_number.attr("disabled", null);
                select_job_number.selectAll("option")
                    .data(json.response.job_numbers)
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
            else {
                input_job_number_filter.attr("disabled", true);
                select_job_number.attr("disabled", true);
                select_job_number.selectAll("option")
                    .data([{ id: -1, name: "n/a" }])
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }

            // populate purchase orders
            if (json.response.purchase_orders != null) {
                json.response.purchase_orders.unshift({ id: -1, name: "n/a" });
                input_purchase_order.attr("disabled", null);
                select_purchase_order.attr("disabled", null);
                select_purchase_order.selectAll("option")
                    .data(json.response.purchase_orders)
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
            else {
                input_purchase_order.attr("disabled", true);
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

// find associated receiver numbers
async function update_receiver_numbers()
{
    await d3.json("/qa1_data_portal/get_receiver_numbers/", {
        method: "POST",
        body: JSON.stringify({
            purchase_order: select_purchase_order.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {

            // reset the dropdown contents
            select_receiver_number.selectAll("option").remove();

            // populate the dropdown
            if (json.response != null) {
                select_receiver_number.attr("disabled", null);
                select_receiver_number.selectAll("option")
                    .data(json.response)
                    .join("option")
                    .attr("value", (x) => x.id)
                    .text((x) => x.name);
            }
            else {
                select_receiver_number.attr("disabled", true);
                select_receiver_number.selectAll("option")
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
            employee_id: select_employee_id.property("value"),
            part_id: select_part_id.property("value"),
            part_revision: select_part_revision.property("value"),
            job_number: select_job_number.property("value"),
            purchase_order: select_purchase_order.property("value"),
            receiver_number: select_receiver_number.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            if (json.response) {
                select_employee_id.attr("disabled", true);
                select_part_id.attr("disabled", true);
                select_part_revision.attr("disabled", true);
                select_job_number.attr("disabled", true);
                select_purchase_order.attr("disabled", true);
                select_receiver_number.attr("disabled", true);
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

// close the open inspection record (excel document)
async function set_inspection_record_document()
{
    await d3.json("/qa1_data_portal/set_inspection_record/", {
        method: "POST",
        body: JSON.stringify({
            part_id: select_part_id.property("value"),
            part_revision: select_part_revision.property("value"),
            job_number: select_job_number.property("value"),
            purchase_order: select_purchase_order.property("value"),
            receiver_number: select_receiver_number.property("value")
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((json) => {
        if (json.status == "ok") {
            if (json.response) {
                select_employee_id.attr("disabled", null);
                select_part_id.attr("disabled", null);
                select_part_revision.attr("disabled", null);
                select_job_number.attr("disabled", null);
                select_purchase_order.attr("disabled", null);
                select_receiver_number.attr("disabled", null);
            }
        }
        else if (json.status == "log") {
            console.log(json.response);
        }
        else if (json.response == "alert") {
            alert(json.response);
        }
    });
}