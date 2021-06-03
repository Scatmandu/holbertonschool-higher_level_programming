#!/usr/bin/node
// prints a string x times where x is argv[2]
const numby = process.argv[2];
const strang = 'C is fun';
let i = 0;
while (i < numby) {
  console.log(strang);
  i++;
}
