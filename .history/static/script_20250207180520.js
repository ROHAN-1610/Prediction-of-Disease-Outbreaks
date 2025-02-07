// Dark Mode Toggle
const darkModeToggle = document.getElementById("dark-mode-toggle");
darkModeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    darkModeToggle.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});

// Function to show the selected form and hide others
function showForm(disease) {
    document.querySelectorAll(".prediction-form").forEach(form => {
        form.style.display = "none";
    });

    const selectedForm = document.getElementById(`${disease}-form`);
    if (selectedForm) {
        selectedForm.style.display = "flex";
    }
}

// Function to handle form submission and send data to Flask API
async function handlePrediction(event, disease) {
    event.preventDefault(); // Prevent page reload

    const form = event.target;
    const formData = new FormData(form);
    const inputData = {};

    formData.forEach((value, key) => {
        inputData[key] = parseFloat(value); // Convert input values to float
    });

    const resultElement = form.querySelector(".prediction-result");
    resultElement.textContent = "Processing...";

    try {
        const response = await fetch(`/predict_${disease}`, { // Flask API endpoint
            method: "POST",
            body: JSON.stringify(inputData),
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        resultElement.textContent = `Prediction: ${data.result}`;
    } catch (error) {
        resultElement.textContent = "Error in prediction. Please try again!";
    }
}

// Attach event listeners to each form
document.getElementById("diabetes-form").addEventListener("submit", (event) => handlePrediction(event, "diabetes"));
document.getElementById("heart-form").addEventListener("submit", (event) => handlePrediction(event, "heart"));
document.getElementById("parkinsons-form").addEventListener("submit", (event) => handlePrediction(event, "parkinsons"));
