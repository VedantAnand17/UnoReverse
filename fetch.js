// main.js
async function fetchNumber() {
    try {
        const response = await fetch('http://localhost:3001/get'); // Fetch the number from the server
        const data = await response.json();
        const randomNumber = data.number;

        // Set the data-percent attribute
        const percentageElement = document.getElementById('percentageElement');
        percentageElement.setAttribute('data-percent', randomNumber);
    } catch (error) {
        console.error('Error fetching number:', error);
    }
}

// Call the function when the page loads
fetchNumber();
