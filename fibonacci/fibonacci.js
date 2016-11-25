var readline = require('readline');

process.stdin.setEncoding('utf8');
var rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

rl.on('line', readLine);

var fibonacciStack = {
  0: 0,
  1: 1
};

function fibonacci(n) {
  if (fibonacciStack[n] === undefined) {
    fibonacciStack[n] = fibonacci(n-1) + fibonacci(n-2);
  }
  return fibonacciStack[n];
}

function readLine (line) {
  if (line !== "\n") {
    var n = parseInt(line.toString().split(' ')[0], 10);
    console.log(fibonacci(n));
    process.exit();
  }
}
