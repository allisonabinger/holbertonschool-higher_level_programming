#!/usr/bin/node
/**
 * contains square class
 */
const OGSquare = require('./5-square');
// imports the rectangle parent class

class Square extends OGSquare {
  // inherits from OGsquare, which inherits from rectangle!
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
