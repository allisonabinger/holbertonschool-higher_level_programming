#!/usr/local/bin/node
/**
 * contains square class
 */
const Rectangle = require('./4-rectangle');
// imports the rectangle parent class

class Square {
  constructor (size) {
    // initializes using the constructor in rectangle
    // size = width and height
    super(size, size)
  }
}
module.exports = Square;
