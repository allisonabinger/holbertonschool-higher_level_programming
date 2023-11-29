#!/usr/bin/node
/**
 * prints "My number: <first arg converted to integer",
 * if the first argument can be converted.
 * if it cannot, prints "Not a number"
 */
const args = process.argv.slice(2);
const arg1 = args[0];
const num = +arg1;
if (Number.isFinite(num) && Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
