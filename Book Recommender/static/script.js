// This JavaScript file can be used to add interactivity to your Flask application.
// You can add custom JavaScript functionality here.

// Example: Display an alert when the form is submitted
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        alert("Form submitted!");
    });
});

