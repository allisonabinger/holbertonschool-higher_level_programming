#!/usr/local/bin/node
/**
 * prints "C is fun" x amount of times
 * if x can't be converted to an int - prints "Missing number of occurrences"
 * x is first argument of script
 */
const args = process.argv.slice(2);
const x = +args[0];
let y = 0;
if (Number.isFinite(x) && Number.isInteger(x)) {
  while (y < x) {
    console.log('C is fun');
    y++;
  }
} else {
  console.log('Missing number of occurrences');
}
