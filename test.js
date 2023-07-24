document.addEventListener("DOMContentLoaded", function () {
    console.log("Hello world!");
    // Function to display the sensor data
    function displaySensorData(reading) {
        let sensorDiv = document.getElementById("pir_data");
        sensorDiv.innerHTML = "PIR data: " + reading;
    }

    // Establish a server-sent events connection
    let eventSource = new EventSource("http://192.168.1.104/");
    // Event listener for server-sent events
    eventSource.onmessage = function(event) {
        displaySensorData(event.reading);
    };
})
