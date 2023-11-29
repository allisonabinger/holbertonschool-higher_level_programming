#!/usr/bin/node
const args = process.argv.slice(2);
// sliced 2 because first two are node and name of file
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
