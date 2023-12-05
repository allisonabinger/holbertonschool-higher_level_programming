#!/usr/bin/node
/**
 * Script that displays the status code of a GET request
 * The first arugment is the url to request
 */
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code:', response.statusCode);
});
