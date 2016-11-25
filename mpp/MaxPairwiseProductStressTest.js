var n, numbers;
var count = 0;

function getMaxPairwiseProduct(numbers) {
  var n = numbers.length;
  var result = 0;
  for (var i=0; i<n; ++i) {
    for (var j=i+1; j<n; ++j) {
      if (numbers[i] * numbers[j] > result) {
        result = numbers[i] * numbers[j];
      }
    }
  }
  return result;
}

function getMaxPairwiseProductFast(numbers) {
    var n, max_index1, max_index2;
    n = numbers.length;
    max_index1 = -1;
    max_index2 = -1;

    for (var i = 0; i < n; ++i) {
        if ((max_index1 === -1) || (numbers[i] > numbers[max_index1])) {
            console.log('maxindex1' + i);
            max_index1 = i;
        }
    }
    for (var j = 0; j < n; ++j) {
        if (
             (j !== max_index1) &&
             ((max_index2 == -1) || (numbers[j] > numbers[max_index2]))
           ) {
            console.log('maxindex2' + j);
            max_index2 = j;
        }
    }

    return numbers[max_index1] * numbers[max_index2];
};

while (true) {
  var n = Math.floor((Math.random() * 2) + 5);
  console.log(n);
  var numbers = [];
  for (var i=0; i<n; i++) {
      numbers.push(Math.floor((Math.random() * 10) + 0));
  }
  var numbersString = '';
  for (var i = 0; i <n; i++) {
    numbersString += numbers[i].toString() + ' ';
  }
  console.log(numbersString);
  console.log(numbers);
  var res1 = getMaxPairwiseProduct(numbers);
  var res2 = getMaxPairwiseProductFast(numbers);
  if (res1 !== res2) {
    console.log("Wrong answer: " + res1 + ' ' + res2);
    break;
  } else {
    console.log("OK");
  }
}
process.exit();
