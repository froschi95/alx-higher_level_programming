#!/usr/bin/node
const dictInput = require('./101-data').dict;
const outputDict = [];

for (const key in dictInput) {
  const ocurr = dictInput[key];
  outputDict[ocurr] = [];
  for (const keys in dictInput) {
    if (dictInput[keys] === ocurr) {
      outputDict[ocurr].push(keys);
    }
  }
}
console.log(outputDict);
