#!/usr/bin/node
// computes/prints a factorial
const numby = parseInt(process.argv[2]);
function myFactorial (numby) {
  if (numby === 0 || isNaN(numby)) {
    return 1;
  } else if (numby < 0) {
    return 0;
  } else {
    return numby * myFactorial(numby - 1);
  }
}
console.log(myFactorial(numby));
