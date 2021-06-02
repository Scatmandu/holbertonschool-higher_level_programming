#!/usr/bin/node
// prints the value of the first argument passed
const noArg = 'No argument';
if (process.argv[2] == null) {
  console.log(noArg);
} else {
  console.log(process.argv[2]);
}
