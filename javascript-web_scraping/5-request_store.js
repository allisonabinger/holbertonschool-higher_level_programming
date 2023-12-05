#!/usr/local/bin/node
/**
 * Script that gets the contents of a webpage and
 * stores it in a file
 * 1st arg: url to request
 * 2nd arg: file path to store the body response
 * gives an error and exits if arguments are invalid or error in file writing
 */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

if (!url || !file)  {
  console.error('Invalid arguments');
  process.exit(1);
}
request(url, (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    process.exit(1);
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error occured in writing: ', err);
      process.exit(1);
    }
  });
});
