#!/usr/bin/node
// displays the status code of a GET request

import request from 'request';

request(process.argv[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
