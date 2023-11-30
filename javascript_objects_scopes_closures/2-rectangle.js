#!/usr/bin/node
/**
 * contains Rectangle class
 * initializes width att with w, height att with h
 * if w or h is <= 0, creates an empty object
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;// empty object
    }
  }
}
module.exports = Rectangle;
