#!/usr/bin/node
// added instance methods rotate and double

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
  // prints the rectangle using X
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
  // rotates the rectangle
  rotate () {
    const storeHeight = this.height;
    const storeWidth = this.width;
    this.height = storeWidth;
    this.width = storeHeight;
  }
  // doubles the rectangle's size
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
