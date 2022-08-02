#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
import request from 'request';
const starWars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWars, function (_error, _response, body) {
  const parse = JSON.parse(body);
  console.log(parse.title);
});
