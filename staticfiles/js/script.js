$(document).ready(function() {
    setStatusColor()
});

function setStatusColor() {
    $(".job_status").each(function() {
        const status = $(this);
        const statusText = status.text().trim();
        
        // Remove existing classes to ensure only one class is added
        status.removeClass("bg-info bg-danger bg-warning bg-success");

        // Determine which class to add based on the status text
        if (statusText === "Unassigned") {
            status.addClass("bg-info");
        } else if (statusText === "Pending Start") {
            status.addClass("bg-danger");
        } else if (statusText === "In Progress") {
            status.addClass("bg-warning");
        } else if (statusText === "Completed") {
            status.addClass("bg-success");
        }
    });
}