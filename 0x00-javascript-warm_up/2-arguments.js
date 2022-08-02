#!/usr/bin/node
// prints different strings depending on the number of args

const zeroArg = 'No argument';
const oneArg = 'Argument found';
const twoPlus = 'Arguments found';

if (process.argv.length === 2) {
  console.log(zeroArg);
} else if (process.argv.length === 3) {
  console.log(oneArg);
} else {
  console.log(twoPlus);
}
