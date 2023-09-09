// Fetch data from Flask server based on the username parameter
fetch(`/graph/${username}`)
    .then(response => response.json())
    .then(data => {
        // Extract date and streak values
        const dates = data.map(entry => entry.date);
        const streakValues = data.map(entry => entry.streak);

        // Create a chart on the canvas element
        const ctx = document.getElementById('streaksChart').getContext('2d');
        const streaksChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Streaks',
                    data: streakValues,
                    borderColor: 'blue',
                    backgroundColor: 'rgba(0, 0, 255, 0.2)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                title: {
                    display: true,
                    text: `Streaks Over Time for User: ${username}`
                },
                scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'day', // Customize the time unit as needed
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Date'
                        }
                    }],
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Streak Count'
                        }
                    }]
                }
            }
        });
    })
    .catch(error => console.error('Error fetching data:', error));
