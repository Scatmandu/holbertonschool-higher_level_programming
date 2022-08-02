#!/usr/bin/node
// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(URL, function (data) {
  const hello = data.hello;
  $('DIV#hello').text(hello);
});
