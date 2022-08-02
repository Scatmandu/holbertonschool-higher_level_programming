#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present

import request from 'request';
const URL = process.argv[2];
let count = 0;

request(URL, function (_error, _response, body) {
  const bodyJSON = JSON.parse(body).results;

  for (let i = 0; i < bodyJSON.length; i++) {
    const characters = bodyJSON[i].characters;

    for (let j = 0; j < characters.length; j++) {
      const char = characters[j];
      const charID = char.split('/')[5];

      if (charID === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
