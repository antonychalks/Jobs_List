const addJobButton = $("#add_job_button");

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
    addJobButton.show();
});