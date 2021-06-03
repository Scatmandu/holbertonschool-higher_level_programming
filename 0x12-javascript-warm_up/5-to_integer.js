#!/usr/bin/node
// prints an arg if its a number
const numby = process.argv[2];
if (isNaN(numby)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numby);
}
