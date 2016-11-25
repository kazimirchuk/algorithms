var fs = require('fs');

var text = "";

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

for (var i=0; i<100; i++) {
    min = getRandomInt(0, 1000);
    max = getRandomInt(min, 10000);
    text += min.toString() + ' ' + max.toString() + '\n';
}

fs.writeFile("./cases.txt", text, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
});
