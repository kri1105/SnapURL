function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector('.copy-btn');
        if (btn) {
            btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            setTimeout(() => {
                btn.innerHTML = '<i class="far fa-copy"></i> Copy';
            }, 2000);
        }
    });
}

// Auto-focus the input field on page load
document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('input[type="url"]');
    if (input) input.focus();

    // Add event listener for form submission
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', () => {
            // You could add loading indicators here if needed
        });
    }
});