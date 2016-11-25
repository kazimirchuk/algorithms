var fs = require('fs');

var text = "200000\n";

for (var i=0; i<200000-1; i++) {
    text += Math.floor((Math.random() * 100000) + 0).toString() + ' ';
}


fs.writeFile("./mpp_test.txt", text, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 
