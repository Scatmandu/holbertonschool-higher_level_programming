#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
      row = '';
    }
  }

  rotate () {
    const storeHeight = this.height;
    const storeWidth = this.width;
    this.height = storeWidth;
    this.width = storeHeight;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
