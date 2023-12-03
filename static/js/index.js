function checkLoggedIn() {
    const isLoggedIn = sessionStorage.getItem('isLoggedIn');
    return isLoggedIn === 'true';
}

// Function to hide the anchor if user is logged in
function hideAnchorIfLoggedIn() {
    const isLoggedIn = checkLoggedIn();
    if (isLoggedIn) {
        const autentificareAnchor = document.getElementById('autentificare');
        autentificareAnchor.style.display = 'none';
    }
}

// Call hideAnchorIfLoggedIn() on page load
window.addEventListener('DOMContentLoaded', function () {
    hideAnchorIfLoggedIn();
});