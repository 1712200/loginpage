document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting
    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // No specific validation, any username and password will log in successfully
    if (username && password) {
        document.getElementById("message").style.color = "green";
        document.getElementById("message").textContent = "Login successful!";
    } else {
        document.getElementById("message").style.color = "red";
        document.getElementById("message").textContent = "Please enter both username and password.";
    }
});
