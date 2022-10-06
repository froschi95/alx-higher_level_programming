#!/usr/bin/node
let nextMax = 0;
const args = process.argv.slice(2).map(x => parseInt(x));
if (args.length > 1) {
  args.sort();
  const fmax = Math.max(...args);
  const index = args.indexOf(fmax);
  args.splice(index, 1);
  // console.log(args)
  nextMax = Math.max(...args);
}
console.log(nextMax);
