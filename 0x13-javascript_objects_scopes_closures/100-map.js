#!/usr/bin/node
const list = require('./100-data').list;
const mappy = list.map(x, i) => i * x);
console.log(list);
console.log(mappy);
