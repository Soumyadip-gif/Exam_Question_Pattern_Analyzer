// =================================
// EXAM QUESTION PATTERN ANALYZER
// JAVASCRIPT
// =================================


// =================================
// TOPIC FREQUENCY BAR CHART
// =================================

const topicBars = document.querySelectorAll(".topic-bar");

if (topicBars.length > 0) {

    let maxCount = 0;

    // Find the highest number of questions
    topicBars.forEach(function (bar) {

        const count = parseInt(bar.dataset.count, 10);

        if (!isNaN(count) && count > maxCount) {
            maxCount = count;
        }

    });


    // Set width of each topic bar
    topicBars.forEach(function (bar) {

        const count = parseInt(bar.dataset.count, 10);

        if (!isNaN(count) && maxCount > 0) {

            const percentage = (count / maxCount) * 100;

            bar.style.width = percentage + "%";

        }

    });

}


// =================================
// TOPIC DISTRIBUTION CHART
// =================================

document.addEventListener("DOMContentLoaded", function () {

    const topicDataElement =
        document.getElementById("topic-data");

    const chartCanvas =
        document.getElementById("topicChart");


    // Check whether required elements exist
    if (!topicDataElement || !chartCanvas) {

        console.error(
            "Topic chart elements were not found."
        );

        return;
    }


    // =================================
    // CHECK CHART.JS
    // =================================

    if (typeof Chart === "undefined") {

        console.error(
            "Chart.js is not loaded."
        );

        const message = document.createElement("p");

        message.textContent =
            "Unable to load the Topic Distribution Chart. Please check your internet connection.";

        message.style.textAlign = "center";
        message.style.fontWeight = "bold";

        chartCanvas.parentElement.appendChild(message);

        return;
    }


    // =================================
    // READ FLASK DATA
    // =================================

    let topicData;

    try {

        topicData = JSON.parse(
            topicDataElement.textContent.trim()
        );

    } catch (error) {

        console.error(
            "Unable to read topic data:",
            error
        );

        return;
    }


    // =================================
    // CHECK DATA
    // =================================

    const topics = Object.keys(topicData);

    const counts = Object.values(topicData);


    if (topics.length === 0) {

        console.log(
            "No topic data available for chart."
        );

        return;
    }


    // =================================
    // CREATE CHART
    // =================================

    new Chart(chartCanvas, {

        type: "bar",

        data: {

            labels: topics,

            datasets: [

                {

                    label: "Number of Questions",

                    data: counts,

                    borderWidth: 1

                }

            ]

        },


        options: {

            responsive: true,

            maintainAspectRatio: false,


            plugins: {

                legend: {

                    display: true

                },

                title: {

                    display: true,

                    text: "Questions by Topic"

                }

            },


            scales: {

                x: {

                    ticks: {

                        autoSkip: false

                    }

                },


                y: {

                    beginAtZero: true,

                    ticks: {

                        stepSize: 1

                    }

                }

            }

        }

    });

});