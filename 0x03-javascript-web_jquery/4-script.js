#!/usr/bin/node

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
