#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie, where the epixode number
 * matches a given integer.
 * The first argument is movie ID.
 * Star Wars API endpoint: https://swapi-api.hbtn.io/api/films/:id
 */
const request = require('request');
const ID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${ID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  } else {
  const data = JSON.parse(body);
  console.log(`${data.title}`);
  }
});
