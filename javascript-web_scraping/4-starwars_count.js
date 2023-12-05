#!/usr/local/bin/node
/**
 * Script that prints the number of movies where the
 * character "Wedge Antilles" is present
 * The first argument is the API URL: https://swapi-api.hbtn.io/api/films/
 * Wedge Antilles is character ID 18
 */
const request = require('request');
const ID = '18';
const url = process.argv[2];

request(url, (error, request, body) => {
  if (error) {
    console.error('Error', error.message);
    process.exit(1);
  } else {
    const data = JSON.parse(body);
    let n = 0;
    for (const movie in data.results) {
      const chars = data.results[movie].chars;
      for (const char in chars) {
        if (chars[char].includes(ID)) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
