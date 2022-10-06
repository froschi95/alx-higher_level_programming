#!/usr/bin/node
let nextMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  fmax = Math.max(...args);
  index = args.indexOf(fmax);
  args.splice(index, 1);
  nextMax = Math.max(...args);
}
console.log(nextMax);
