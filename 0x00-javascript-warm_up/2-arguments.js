#!/usr/bin/node

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
