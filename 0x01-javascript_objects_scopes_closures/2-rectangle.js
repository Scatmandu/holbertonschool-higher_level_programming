#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (this.width > 0 && this.height > 0) {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
