#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }

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
