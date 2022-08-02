#!/usr/bin/node
// computes and prints a factorial

function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const numbie = parseInt(process.argv[2]);
console.log(factorial(numbie));
