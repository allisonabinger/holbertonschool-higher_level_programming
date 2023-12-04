#!/usr/bin/node
/**
 * Script that reads and prints the contents of a file.
 * First argument is the file path, if an error occured,
 * it prints the error object.
 */
const fs = require('fs');
/* fs is a built-in module that can interact with file system */
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
