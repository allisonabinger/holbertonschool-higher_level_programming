#!/usr/local/bin/node
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
  print() {
    for (let n = 0; n < this.height; n++){
      console.log('X'.repeat(this.width))
      // much better method than using two+ loops!
    }
  }
}
module.exports = Rectangle;
