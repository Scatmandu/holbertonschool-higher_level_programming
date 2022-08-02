#!/usr/bin/node
// prints an arg if there is one, otherwise prints a string

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
