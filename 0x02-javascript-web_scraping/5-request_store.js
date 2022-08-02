#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

import request from 'request';
import { writeFile } from 'fs';

request(process.argv[2], function (_error, _response, body) {
  writeFile(process.argv[3], body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
