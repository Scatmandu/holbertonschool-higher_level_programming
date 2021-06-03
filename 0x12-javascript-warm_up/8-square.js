#!/usr/bin/node
// prints a square of X's i times where x is argv[2]
const numby = process.argv[2];
if (isNaN(numby)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numby; i++) {
    let myStr = '';
    for (let j = 0; j < numby; j++) {
      myStr += 'X';
    }
    console.log(myStr);
  }
}
