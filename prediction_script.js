function prediction() {
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


    total_revenue = [];
    for( var i = 0; i < storeA.length; i++){

    total_revenue.push(storeA[i]+storeA[i]+storeA[i]);
}

}