#!/usr/bin/node
// implements method charPrint that prints the square using C or X
const Square0 = require('./5-square');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }
  // prints the square using C or X
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
      row = '';
    }
  }
}

module.exports = Square;
