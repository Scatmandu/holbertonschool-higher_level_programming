#!/usr/bin/node
// prints My number: <first argument converted in integer> 
// if the first argument can be converted to an integer

const numbie = parseInt(process.argv[2]);

if (numbie) {
  console.log('My number: ' + numbie);
} else {
  console.log('Not a number');
}
