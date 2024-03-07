const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const addTaskButton = $("#add_task_button");
const cancelButton = $("#cancel_button");
const editButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");
const editTaskForm = $("#edit_task_form")
const TRADES = [
    ["0", "Carpenter"],
    ["1", "Plumber"],
    ["2", "Electrician"],
    ["3", "Plasterer"],
    ["4", "Groundsworker"],
    ["5", "Decorator"],
    ["6", "Gas"],
    ["7", "Planner"]
];
$(document).ready(function() {

    // Hide the add_task_form by default
    $("#add_task_form").hide();
    $("#edit_task_form").hide();
});

// Function to handle when the add task button is clicked
addTaskButton.on("click", function() {
    console.log("Add Task button clicked");

    // Show the add task form
    $("#add_task_form").show();
    addTaskButton.hide();
    $("button[type='submit']").attr("name", "add_task");
    console.log("Submit button name attribute changed to add_task");
});

    // Function to handle when the cancel button is clicked
    cancelButton.on("click", function() {
        console.log("Cancel button clicked");

        // Hide the add task form and show the add task button
        $("#add_task_form").hide();
        addTaskButton.show();
    });

// Handle click event for edit button
$(".edit-button").on("click", function() {
    console.log("Edit Task button clicked");

    var taskId = $(this).data("task_id");
    var description = $(this).data("description");
    var tradesRequired = $(this).data("trades-required");
    var tradesmanAssigned = $(this).data("tradesman-assigned");
    var timeRequired = $(this).data("time-required");
    var isCompleted = $(this).data("is-completed");
    var slug = $(this).data("slug");
    console.log(taskId);
    console.log(slug);
    console.log("Trades Required:", tradesRequired);

    // Populate the add_task_form fields with task details
    $("#id_description").val(description);
    // For trades_required, set the checkboxes based on the received data
    setTradesCheckboxes(tradesRequired);
    $("#id_tradesman_assigned").val(tradesmanAssigned);
    $("#id_time_required").val(timeRequired);
    // Set the is_completed checkbox based on the data
    $("#id_is_completed").prop("checked", isCompleted === "True");

    // Change the submit button name to indicate editing the task
    $("button[type='submit']").attr("name", "edit_task");
    $("button[type='submit']").addClass( "btn-edit" );
    // Show the add_task_form
    $("#edit_task_form").show();
    addTaskButton.hide();
    editButtons.innerText = "Update";
    var url = `/tradesman/${slug}/edit_task/${taskId}/`;
    console.log("Edit URL:", url);
    editTaskForm.attr("action", `edit_task/${taskId}/`);
});

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let taskId = e.target.getAttribute("task_id");
        console.log(taskId)
        deleteConfirm.href = `delete_comment/${taskId}`;
        deleteModal.show();
    });
}

    // Function to set the checkboxes for trades_required
function setTradesCheckboxes(tradesRequired) {
    console.log("Setting trades checkboxes. Trades Required:", tradesRequired);
    // Reset checkboxes first
    $("input[name^='trades_required']").prop("checked", false);
    // Check if tradesRequired is a string
    if (typeof tradesRequired === 'string') {
        // Split the string into an array of trade codes
        var tradeCodes = tradesRequired.split(", ");
        console.log("Trade Codes:", tradeCodes);
        // Set checkboxes for each trade code
        tradeCodes.forEach(tradeCode => {
            // Find the trade in the TRADES array
            const tradeIndex = TRADES.findIndex(trade => trade[1] === tradeCode);
            if (tradeIndex !== -1) {
                // Construct the ID based on the index
                var checkboxId = "#id_trades_required_" + TRADES[tradeIndex][0];
                console.log("Setting checkbox for trade:", tradeCode, "ID:", checkboxId);
                $(checkboxId).prop("checked", true);
            } else {
                console.error("Trade code not found:", tradeCode);
            }
        });
    } else if (Array.isArray(tradesRequired)) {
        // If tradesRequired is already an array, set checkboxes for each trade code
        tradesRequired.forEach(tradeCode => {
            // Find the trade in the TRADES array
            const tradeIndex = TRADES.findIndex(trade => trade[1] === tradeCode);
            if (tradeIndex !== -1) {
                // Construct the ID based on the index
                var checkboxId = "#id_trades_required_" + TRADES[tradeIndex][0];
                console.log("Setting checkbox for trade:", tradeCode, "ID:", checkboxId);
                $(checkboxId).prop("checked", true);
            } else {
                console.error("Trade code not found:", tradeCode);
            }
        });
    } else {
        console.error("tradesRequired is not in a valid format:", tradesRequired);
    }
}


