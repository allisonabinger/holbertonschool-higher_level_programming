#!/usr/local/bin/node
/**
 * prints three lines using an array, similar to 1-multi_languages.js.
 */
const messages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let x = 0;
while (x < 3) {
  console.log(messages[x]);
  x++;
}
