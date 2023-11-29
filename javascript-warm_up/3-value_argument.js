#!/usr/local/bin/node
/**
 * prints argument given after calling function
 * or prints 'No argument' if none is given
 */
const args = process.argv.slice(2);
const arg1 = args[0];
if (arg1 === undefined) {
  console.log('No argument');
} else {
  console.log(arg1);
}
