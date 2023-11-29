#!/usr/bin/node
/**
 * computes and prints a factorial
 * first arg is an integer used
 * factorial of NaN is 1
 * recursive function format
 */
const num = process.argv[2];
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (parseInt(num)) {
  console.log(factorial(num));
} else console.log(1);
