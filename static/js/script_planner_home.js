const addJobButton = $("#add_job_button");
const cancelButton = $(".cancel_button");
const editJobForm = $("#edit_job_form")

$(document).ready(function() {

    // Hide the add_task_form by default
    $("#add_job_form").hide();
    $("#edit_job_form").hide();
});

// Function to handle when the add task button is clicked
addJobButton.on("click", function() {
    console.log("Add Job button clicked");

    // Show the add task form
    $("#add_job_form").show();
    addJobButton.hide();
    $("button[type='submit']").attr("name", "add_job");
    console.log("Submit button name attribute changed to add_job");
});

// Function to handle when the cancel button is clicked
cancelButton.on("click", function() {
    console.log("Cancel button clicked");

    // Hide the add task form and show the add task button
    $("#add_job_form").hide();
    $("#edit_job_form").hide();
    addJobButton.show();
});

// Handle click event for edit button
$(".edit-job-button").on("click", function() {
    console.log("Edit Job button clicked");

    var jobId = $(this).data("job_id");
    var customerName = $(this).data("customer_name");
    var phone = $(this).data("phone");
    var otherPhone = $(this).data("other_phone");
    var email = $(this).data("email");
    var street = $(this).data("street");
    var townCity = $(this).data("town_city");
    var county = $(this).data("county");
    var postcode = $(this).data("postcode");
    var jobDescription = $(this).data("job_description");


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
    var url = `/planners/edit_job/${jobId}/`;
    console.log("Edit URL:", url);
    editJobForm.attr("action", `edit_job/${jobId}/`);
});