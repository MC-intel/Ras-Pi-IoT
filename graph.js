var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // x-axis labels
        datasets: [{
            label: 'Co2 Levels', // y-axis label
            data: [], // data points
            backgroundColor: 'rgba(255, 99, 132, 0.2)', // background color
            borderColor: 'rgba(255, 99, 132, 1)', // line color
            borderWidth: 1, // line width
            pointRadius: 3, // point radius
            pointBackgroundColor: 'black', // point background color
            pointBorderWidth: 2, // point border width
            pointHoverRadius: 6, // point hover radius
            pointHoverBackgroundColor: 'rgba(255, 99, 132, 1)' // point hover background color
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                gridLines: {
                    color: 'rgba(0, 0, 0, 0.1)'
                },
                ticks: {
                    fontColor: 'rgba(0, 0, 255, 0.5)',
                    fontSize: 12
                }
            },
            x: {
                gridLines: {
                    color: 'rgba(0, 0, 0, 0.1)'
                },
                ticks: {
                    fontColor: 'rgba(0, 0, 255, 0.5)',
                    fontSize: 12
                }
            }
        },
        legend: {
            labels: {
                fontColor: 'rgba(0, 0, 0, 0.5)',
                fontSize: 12
            }
        }
    }
});

// Use fetch API or XMLHttpRequest to load json from file
fetch("/data.json")
.then(function(response) {
    return response.json();
})
.then(function(data) {
    // update the chart's data
    myChart.data.labels = data.x;
    myChart.data.datasets[0].data = data.y;
    myChart.update();
});

// ... chart code ...

async function updateChart() {
    try {
        const response = await fetch("/data.json");
        const data = await response.json();
        // update the chart's data
        myChart.data.labels = data.x;
        myChart.data.datasets[0].data = data.y;
        myChart.update();
    } catch (error) {
        console.error(error);
    }
}

setInterval(updateChart, 1000);