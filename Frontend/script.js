async function checkHealth() {

    const statusElement = document.getElementById("status");

    statusElement.textContent = "Checking backend...";

    try {

        const response = await fetch("/health");

        const data = await response.json();

        if (data.status === "healthy") {
            statusElement.textContent = "🟢 Backend is Healthy";
        } else {
            statusElement.textContent = "🔴 Backend is Unhealthy";
        }

    } catch (error) {

        statusElement.textContent = "🔴 Backend is not reachable";

    }
}