#!/usr/bin/node

const numbie = parseInt(process.argv[2]);
if (Number.isInteger(numbie)) {
  console.log('My number is: ' + numbie);
} else {
  console.log('Not a number');
}
