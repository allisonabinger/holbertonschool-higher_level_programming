#!/usr/local/bin/node
/**
 * Script that writes a string to a file, using the first arg as the file path
 * the second argument is the string to write
 * if an error occured during the writing, print the rror object
 */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err){
    console.error(err);
  }
});
