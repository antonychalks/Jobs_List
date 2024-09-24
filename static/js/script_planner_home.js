const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const addJobButton = $("#add_job_button");
const cancelButton = $(".cancel_button");
const editJobForm = $("#edit_job_form")



// Function to handle when the add task button is clicked
addJobButton.on("click", function() {
    // Show the add task form
    $("#add_job_form").show();
    addJobButton.hide();
    $("button[type='submit']").attr("name", "add_job");
});

// Function to handle when the cancel button is clicked
cancelButton.on("click", function() {
    // Hide the add task form and show the add task button
    $("#add_job_form").hide();
    $("#edit_job_form").hide();
    addJobButton.show();
});

// Handle click event for edit button
$(".edit-job-button").on("click", function() {
    const jobId = $(this).data("job_id");
    const slug = $(this).data("slug");
    const customerName = $(this).data("customer_name");
    const phone = $(this).data("phone");
    const otherPhone = $(this).data("other_phone");
    const email = $(this).data("email");
    const street = $(this).data("street");
    const townCity = $(this).data("town_city");
    const county = $(this).data("county");
    const postcode = $(this).data("postcode");
    const jobDescription = $(this).data("job_description");


    // Populate the add_task_form fields with task details
    $("#id_customer_name").val(customerName);
    $("#id_phone").val(phone);
    $("#id_other_phone").val(otherPhone);
    $("#id_email").val(email);
    $("#id_street").val(street);
    $("#id_town_city").val(townCity);
    $("#id_county").val(county);
    $("#id_postcode").val(postcode);
    $("#id_job_description").val(jobDescription);
    
    // Show the edit_job_form
    $("#edit_job_form").show();
    addJobButton.hide();
    editJobForm.attr("action", `/planners/${slug}/edit_job/${jobId}/`);
});

$(".btn-delete").on("click", function() {
    console.log("Delete button clicked.")
    let jobId = $(this).data("job_id");
    console.log(jobId)
    deleteConfirm.href = `delete_job/${jobId}`;
    console.log($("#deleteConfirm").href);
    deleteModal.show();
});
