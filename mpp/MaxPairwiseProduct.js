var readline = require('readline');

process.stdin.setEncoding('utf8');
var rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

var n, numbers;
var count = 0;

function getMaxPairwiseProduct(numbers) {
    var n, max_index1, max_index2;
    n = numbers.length;
    max_index1 = -1;
    max_index2 = -1;

    for (var i = 0; i < n; ++i) {
        if ((max_index1 === -1) || (numbers[i] > numbers[max_index1])) {
            max_index1 = i;
        }
    }
    for (var j = 0; j < n; ++j) {
        if (
             (j !== max_index1) &&
             ((max_index2 == -1) || (numbers[j] > numbers[max_index2]))
           ) {
            max_index2 = j;
        }
    }

    return numbers[max_index1] * numbers[max_index2];
};

rl.on('line', function (line) {
  if (line !== "\n") {
    count++;
    if (count === 1) {
      n = parseInt(line.toString(), 10);
    } else if (count === 2) {
      numbers = line.toString().split(' ');
      for (var i=0; i<n; i++) {
        numbers[i] = parseInt(numbers[i], 10);
      }
      console.log(getMaxPairwiseProduct(numbers));
      process.exit();
    }
  }
});
