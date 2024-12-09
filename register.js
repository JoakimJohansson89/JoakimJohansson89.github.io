document.getElementById('register_btn').addEventListener('click', async () =>{
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        document.getElementById('message').innerText ="Passwords do not match"
    }

    // Send data to Flask backend
    const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });

    const result = await response.json();

    if (response.ok) {
        document.getElementById('message').innerText = result.message;
        document.getElementById('register_form').reset();
    } else {
        document.getElementById('message').innerText = result.error;
    }
});