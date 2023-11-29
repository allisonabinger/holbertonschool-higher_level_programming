#!/usr/bin/node
/**
 * prints a square using the 'X' character
 * the length and width of the square is the first argument
 * prints "Missing size" if argument cannot be converted into an integer
 */
const args = process.argv.slice(2);
const size = +args[0];
let h = 0;
if (Number.isFinite(size) && Number.isInteger(size)) {
  while (h < size) {
    let row = '';
    for (let l = 0; l < size; l++) {
      row += 'X';
    }
    console.log(row);
    h++;
  }
} else {
  console.log('Missing size');
}
