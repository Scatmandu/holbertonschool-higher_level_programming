#!/usr/bin/node

const numbie = parseInt(process.argv[2]);

if (numbie) {
  console.log('My number: ' + numbie);
} else {
  console.log('Not a number');
}