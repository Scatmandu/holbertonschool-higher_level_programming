#!/usr/bin/node

const request = require('request');
const starWars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWars, function (_error, _response, body) {
  const parse = JSON.parse(body);
  console.log(parse.title);
});
