document.addEventListener('DOMContentLoaded', function () {
    // Function to handle login form submission
    function handleLogin(event) {
        event.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        // Validate credentials (simplified for demonstration)
        if (username === 'user' && password === 'password') {
            alert('Login successful');
        } else {
            alert('Invalid username or password');
        }
    }

    // Function to handle forgot password form submission
    function handleForgotPassword(event) {
        event.preventDefault();
        const email = document.getElementById('forgotEmail').value;

        // Send a password reset email (simplified for demonstration)
        alert(`Password reset email sent to ${email}`);
    }

    // Function to handle sign-up form submission
    function handleSignUp(event) {
        event.preventDefault();
        const newUsername = document.getElementById('signupUsername').value;
        const newPassword = document.getElementById('signupPassword').value;

        // Create a new user account (simplified for demonstration)
        alert(`Account created for ${newUsername}`);
    }

    // Add event listeners to forms
    document.getElementById('loginForm').addEventListener('submit', handleLogin);
    document.getElementById('forgotPasswordForm').addEventListener('submit', handleForgotPassword);
    document.getElementById('signupForm').addEventListener('submit', handleSignUp);
});
