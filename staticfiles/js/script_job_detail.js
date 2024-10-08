const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const addTaskButton = $("#add_task_button");
const cancelButton = $(".cancel_button");
const editTaskForm = $("#edit_task_form")
const addTaskForm = $("#add_task_form")
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



// Function to handle when the add task button is clicked
addTaskButton.on("click", function() {
    // Show the add task form
    $("#add_task_form").show();
    addTaskButton.hide();
    $("button[type='submit']").attr("name", "add_task");
    editTaskForm.hide();
});

// Function to handle when the cancel button is clicked
cancelButton.on("click", function() {
    // Hide the add task form and show the add task button
    addTaskForm.hide();
    editTaskForm.hide()
    addTaskButton.show();
});

// Handle click event for edit button
$(".edit-button").on("click", function() {
    const taskId = $(this).data("task_id");
    const description = $(this).data("description");
    const tradesRequired = $(this).data("trades-required");
    const tradesmanAssigned = $(this).data("tradesman-assigned");
    const timeRequired = $(this).data("time-required");
    const isCompleted = $(this).data("is-completed");

    // Populate the add_task_form fields with task details
    $("#id_description").val(description);

    // For trades_required, set the checkboxes based on the received data
    setTradesCheckboxes(tradesRequired);
    $("#id_tradesman_assigned").val(tradesmanAssigned);
    $("#id_time_required").val(timeRequired);

    // Set the is_completed checkbox based on the data
    $("#id_is_completed").prop("checked", isCompleted === "True");

    // Change the submit button name to indicate editing the task
    $("button[type='submit']").attr("name", "edit_task").addClass( "btn-edit" );

    // Show the add_task_form
    $("#edit_task_form").show();
    editTaskForm.attr("action", `edit_task/${taskId}/`);
    addTaskForm.hide();
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
$(".btn-delete").on("click", function() {
    let taskId = $(this).data("task_id");
    deleteConfirm.href = `delete_task/${taskId}`;
    deleteModal.show();
});


    // Function to set the checkboxes for trades_required
function setTradesCheckboxes(tradesRequired) {
    // Reset checkboxes first
    $("input[name^='trades_required']").prop("checked", false);
    // Check if tradesRequired is a string
    if (typeof tradesRequired === 'string') {
        // Split the string into an array of trade codes
        const tradeCodes = tradesRequired.split(", ");
        // Set checkboxes for each trade code
        tradeCodes.forEach(tradeCode => {
            // Find the trade in the TRADES array
            const tradeIndex = TRADES.findIndex(trade => trade[1] === tradeCode);
            if (tradeIndex !== -1) {
                // Construct the ID based on the index
                const checkboxId = "#id_trades_required_" + TRADES[tradeIndex][0];
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
                const checkboxId = "#id_trades_required_" + TRADES[tradeIndex][0];
                $(checkboxId).prop("checked", true);
            } else {
                console.error("Trade code not found:", tradeCode);
            }
        });
    } else {
        console.error("tradesRequired is not in a valid format:", tradesRequired);
    }
}


