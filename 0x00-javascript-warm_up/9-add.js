#!/usr/bin/node
// prints the addition of 2 integers

function add (a, b) {
  return a + b;
}
const numbieA = parseInt(process.argv[2]);
const numbieB = parseInt(process.argv[3]);
console.log(add(numbieA, numbieB));
