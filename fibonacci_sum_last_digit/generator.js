var fs = require('fs');

var text = "";

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

for (var i=0; i<1000; i++) {
    text += getRandomInt(0, 10000).toString() + ' ';
}

fs.writeFile("./cases.txt", text, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
});
