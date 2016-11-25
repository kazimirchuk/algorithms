var fs = require('fs');

var text = "";

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

for (var i=0; i<3; i++) {
    var n = getRandomInt(1, 5);
    text += n.toString() + ' ';
    for (var j=0; j<n * 2; j++) {
        text += getRandomInt(1, 100).toString() + ' ';
    }
    text += '\n';
}

fs.writeFile("./cases.txt", text, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
});
