#!/usr/bin/node
//  prints a square using X

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
