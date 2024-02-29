const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

$(document).ready(function() {
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
  $("#edit-button").on("click", function() {
      console.log("Edit Task clicked");

      // Retrieve task details from the clicked edit button's data attributes
      var taskId = $(this).data("task-id");
      var description = $(this).data("description");
      var tradesRequired = $(this).data("trades-required");
      var tradesmanAssigned = $(this).data("tradesman-assigned");
      var timeRequired = $(this).data("time-required");
      var isCompleted = $(this).data("is-completed");

      // Populate the add_task_form fields with task details
      $("#add_task_form #id_description").val(description);
      $("#add_task_form #id_trades_required").val(tradesRequired);
      $("#add_task_form #id_tradesman_assigned").val(tradesmanAssigned);
      $("#add_task_form #id_time_required").val(timeRequired);
      // You can continue this pattern for other form fields

      // Show the add_task_form
      $("#add_task_form").show();
      $("#add_task_button").hide();
  });

    // Handle click event for delete button
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
          console.log("Delete button clicked");
          let taskId = e.target.getAttribute('id');
          deleteConfirm.href = `/tradesman/1/delete_task/${taskId}`;
          deleteModal.show();
      });
  }
});
