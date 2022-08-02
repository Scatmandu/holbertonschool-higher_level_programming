#!/usr/bin/node
// function that returns the number of occurences in a list

export function nbOccurences (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
}
