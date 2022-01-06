#!/usr/bin/node

const numbie = parseInt(process.argv[2]);
let row = '';

if (numbie) {
  for (let i = 0; i < numbie; i++) {
    for (let j = 0; j < numbie; j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
} else {
  console.log('Missing size');
}
