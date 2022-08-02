#!/usr/bin/node
// fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function (data) {
  const name = data.name;
  $('DIV#character').text(name);
});
