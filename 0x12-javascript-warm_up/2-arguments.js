#!/usr/bin/node
// prints arguments
const noArg = 'No argument';
const oneArg = 'Argument found';
const multiArg = 'Arguments found';
if (process.argv[2] == null) {
  console.log(noArg);
} else if (process.argv[2] !== null && process.argv[3] == null) {
  console.log(oneArg);
} else {
  console.log(multiArg);
}
