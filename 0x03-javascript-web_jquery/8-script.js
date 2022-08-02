#!/usr/bin/node
// fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(URL, function (data) {
  const getTitles = data.results;
  $.each(getTitles, function (key, value) {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
