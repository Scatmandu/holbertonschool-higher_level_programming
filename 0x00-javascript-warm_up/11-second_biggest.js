#!/usr/bin/node

const array = [];

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2, j = 0; i < process.argv.length; i++, j++) {
    array[j] = process.argv[i];
    array.sort();
  }
  const arrayIndex = array.length - 2;
  console.log(array[arrayIndex]);
}
