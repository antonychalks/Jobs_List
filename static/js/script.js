$(document).ready(function() {
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");
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

  // Hide the add_task_form by default
  $("#add_task_form").hide();

  // Show the add_task_form when the "Add Task" button is clicked
  $("#add_task_button").on("click", function() {
      console.log("Opening Add Task");
      $("#add_task_form").show();
      $("#add_task_button").hide();
  });

  // Hide the add_task_form when the "Cancel" button is clicked
  $("#cancel_button").on("click", function() {
      console.log("Canceling Add Task");
      $("#add_task_form").hide();
      $("#add_task_button").show();
  });

  // Handle click event for edit button
  // Handle click event for edit button
  $(".edit-button").on("click", function() {
    console.log("Edit Task clicked");

    // Retrieve task details from the clicked edit button's data attributes
    var description = $(this).data("description");
    var tradesRequired = $(this).data("trades-required");
    var tradesmanAssigned = $(this).data("tradesman-assigned");
    var timeRequired = $(this).data("time-required");
    var isCompleted = $(this).data("is-completed");
    console.log("Trades Required:", tradesRequired);

    // Populate the add_task_form fields with task details
    $("#id_form-0-description").val(description);
    // For trades_required, set the checkboxes based on the received data
    setTradesCheckboxes(tradesRequired);
    $("#id_form-0-tradesman_assigned").val(tradesmanAssigned);
    $("#id_form-0-time_required").val(timeRequired);
    // Set the is_completed checkbox based on the data
    $("#id_form-0-is_completed").prop("checked", isCompleted === "True");

    // Show the add_task_form
    $("#add_task_form").show();
    $("#add_task_button").hide();
});

console.log("TRADES array:", TRADES);

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
                var checkboxId = "#id_form-0-trades_required_" + TRADES[tradeIndex][0];
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
                var checkboxId = "#id_form-0-trades_required_" + TRADES[tradeIndex][0];
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






  // Handle click event for delete button
  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          console.log("Delete button clicked");
          let taskId = e.target.getAttribute('data-task-id');
          deleteConfirm.href = `/tradesman/1/delete_task/${taskId}`;
          deleteModal.show();
      });
  }
});