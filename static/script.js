function checkEmail() {
    const emailInput = document.getElementById('emailInput').value;
    const resultElement = document.getElementById('result');

    if (!emailInput.trim()) {
        resultElement.textContent = "Please enter an email!";
        resultElement.style.color = "red";
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: emailInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            resultElement.textContent = `This email is classified as: ${data.result}`;
            resultElement.style.color = data.result === "Spam" ? "red" : "green";
        })
        .catch((error) => {
            console.error('Error:', error);
            resultElement.textContent = "An error occurred!";
            resultElement.style.color = "red";
        });
}
