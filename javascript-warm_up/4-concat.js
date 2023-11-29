#!/usr/bin/node
/**
 * prints two arguments passed to it
 * in the following format: "arg1" is "arg2"
 */
const args = process.argv;
// no slicing necessary
console.log(args[2], 'is', args[3]);
