    <script>
    var sentiment = ["Neutral", "Positive", "Negative"];
    var sentiment_data = {{ sentimentTypeCount }};
    var things_mentioned = ["Trump", "black-lives-matter", "elephant", "china", "justice"];
    var mentioned_count = ["4500", "5300", "6250", "7800", "9800"];

    var pctx = document.getElementById('piechart').getContext('2d');
    var piechart = new Chart(pctx, {
    type: 'doughnut',
    data: {
        labels: sentiment,
        datasets: [{
            data: sentiment_data,
            backgroundColor: [
                'rgba(255, 206, 86, 0.2)', //blue
                'rgba(75, 192, 128, 0.2)', //yellow
                'rgba(255, 99, 132, 0.2)', //pink

                'rgba(75, 192, 192, 0.2)', //cyan
                'rgba(153, 102, 255, 0.2)', //violet
                'rgba(255, 159, 64, 0.2)', //orange
            ],
            borderColor: [
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 128, 1)',
                'rgba(255, 99, 132, 1)',

                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    "options": {
        "maintainAspectRatio": false,
        "legend": {
            "display": false,
            "position": "bottom"
        },
        "title": {}
    }
});

var bctx = document.getElementById('barchart').getContext('2d');
var barchart = new Chart(bctx, {
    type: 'horizontalBar',
    data: {
        labels: things_mentioned,
        datasets: [{
            data: mentioned_count,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
    </script>