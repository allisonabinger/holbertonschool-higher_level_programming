#!/usr/bin/node
/**
 * prints the addition of two integers
 * first and second args are first and second integers, respectively
 * uses function prototype: function add(a,b)
 */
function add (a, b) {
  return a + b;
}
const args = process.argv.slice(2);
const x = +args[0];
const y = +args[1];

if (Number.isFinite(x) && Number.isInteger(x) && Number.isFinite(y) && Number.isInteger(y)) {
  const sum = add(x, y);
  console.log(sum);
} else {
  console.log('NaN');
}
