#!/usr/bin/node
/**
 * searches the second biggest integer in the list of arguments passed to function
 * if no argument passed, or if # of arguments is 1, prints 0
 */
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]);
}
