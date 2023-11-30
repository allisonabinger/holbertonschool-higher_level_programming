#!/usr/bin/node
exports.nb0ccurences = function (list, searchElement) {
  let n = 0;
  for (const element of list) {
    if (element === searchElement) {
      n++;
    }
  }
  return n;
};
