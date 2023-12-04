const loginButton = document.getElementById("autentificare");

if (sessionStorage.length !== 0) {
    const userLogged = JSON.parse(sessionStorage.getItem('userLogged'));
    loginButton.href = "#";
    loginButton.innerHTML = userLogged;

    loginButton.addEventListener('click', function showLogoutButton() {
        const logoutButton = document.createElement("button");
        logoutButton.innerHTML = "Logout";
        logoutButton.style.backgroundColor = "white";
        logoutButton.style.color = "green";
        logoutButton.style.borderRadius = "5px";
        logoutButton.style.display = "block";
        
        loginButton.appendChild(logoutButton);
        console.log("Butonul de deconectare a fost creat");

        logoutButton.addEventListener('click', function logout() {
            sessionStorage.clear();
            window.location.reload();
        });
    });
} else {
    loginButton.innerHTML = "Autentificare <i class='fa fa-arrow-right ms-3'></i>";
    loginButton.href = "login.html";
}


console.log("In buton: ", loginButton.innerHTML);