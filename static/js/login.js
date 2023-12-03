const users = [
    { "username": "adelin", "email": "user1@example.com", "password": "parola" },
    { "username": "user2", "email": "user2@example.com", "password": "password2" }
    // Add more user data as needed
];

document.getElementById('login').addEventListener('submit', function (e) {
    e.preventDefault();
    console.log("i am here");
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Find the user in the JSON data
    const user = users.find(u => (u.username === username || u.email === username) && u.password === password);

    if (user) {
        // Login successful, redirect or perform necessary actions
        alert('Login successful!');  
        window.location.href = 'index.html';
        sessionStorage.setItem('isLoggedIn', 'true');
        // Redirect or perform actions after successful login
    } else {
        // Login failed, display error message or take appropriate action
        alert('Invalid username/email or password. Please try again.');
    }
});