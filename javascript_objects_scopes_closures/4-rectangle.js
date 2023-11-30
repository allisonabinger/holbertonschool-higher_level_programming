#!/usr/bin/node
/**
 * contains rectangle class
 */
class Rectangle {
  constructor (w, h) {
    // initializes width att with w, height att with h
    // if h or w is <= 0, creates an empty object
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;// empty object
    }
  }

  print () {
    // prints a rectangle using the width and height with the 'X' character
    for (let n = 0; n < this.height; n++) {
      console.log('X'.repeat(this.width));
      // much better method than using two+ loops!
    }
  }

  rotate () {
    // rotates the rectangle by swapping the height and width
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // doubles the size of rectangle by multiplying width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
