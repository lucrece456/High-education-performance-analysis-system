// Confirmation Dialogue for Module Deletion
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', () => {
        if (confirm('Are you sure you want to delete this module?')) {
            const moduleId = button.getAttribute('data-module-id');
            // Send AJAX request to delete module
            // Implement AJAX functionality as per your backend setup
        }
    });
});
