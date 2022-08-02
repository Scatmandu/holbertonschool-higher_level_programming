#!/usr/bin/node
// function that returns the reversed version of a list

export function esrever (list) {
  const newList = [];
  let j = 0;

  for (let i = list.length - 1; i >= 0; i--, j++) {
    newList[j] = list[i];
  }
  return newList;
}
