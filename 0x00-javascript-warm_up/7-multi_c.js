#!/usr/bin/node
// prints x times “C is fun”

const strang = 'C is fun';
const numbie = parseInt(process.argv[2]);

if (Number.isInteger(numbie)) {
  for (let i = 0; i < numbie; i++) {
    console.log(strang);
  }
} else {
  console.log('Missing number of occurrences');
}
