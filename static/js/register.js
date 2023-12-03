function updateUsersJSON() {
    // Get the existing users data from localStorage or initialize an empty array if it doesn't exist
    let usersData = JSON.parse(localStorage.getItem('users.json')) || [];
console.log("i am here");
    // Get form data
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Create user object
    const newUser = {
        "username": username,
        "email": email,
        "password": password
    };

    // Add the new user to the existing users data
    usersData.push(newUser);

    // Update localStorage with the modified users data
    localStorage.setItem('users.json', JSON.stringify(usersData));

    // Log the updated data for verification
    console.log(JSON.parse(localStorage.getItem('users.json')));
}