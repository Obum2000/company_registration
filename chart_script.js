var weeks = [1, 2, 3, 4];
var storeA = [];
var storeB = [];
var storeC = [];

function display() {
    storeA = [];
    storeB = [];
    storeC = [];

    storeA.push(document.getElementById("week1a").value);
    storeA.push(document.getElementById("week2a").value);
    storeA.push(document.getElementById("week3a").value);
    storeA.push(document.getElementById("week4a").value);

    storeB.push(document.getElementById("week1b").value);
    storeB.push(document.getElementById("week2b").value);
    storeB.push(document.getElementById("week3b").value);
    storeB.push(document.getElementById("week4b").value);

    storeC.push(document.getElementById("week1c").value);
    storeC.push(document.getElementById("week2c").value);
    storeC.push(document.getElementById("week3c").value);
    storeC.push(document.getElementById("week4c").value);

    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: weeks,
            datasets: [
                {
                    data: storeA,
                    label: "Store A",
                    borderColor: "red",
                    fill: false
                },
                {
                    data: storeB,
                    label: "Store B",
                    borderColor: "green",
                    fill: false
                },
                {
                    data: storeC,
                    label: "Store C",
                    borderColor: "blue",
                    fill: false
                },
            ]
        }
    });
}