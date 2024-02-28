$(document).ready(function() {
  // Hide the form by default
  $("#add_task_form").hide();

  // Show the form when the "Add Task" button is clicked
  $( "#add_task_button" ).on( "click", function() {
      console.log("Opening Add Task");
      $("#add_task_form").show();
      $("#add_task_button").hide();
  });

  // Hide the form when the "Cancel" button is clicked
  $( "#cancel_button" ).on( "click", function() {
      console.log("Canceling Add Task");
      $("#add_task_form").hide();
      $("#add_task_button").show();
  });
});
