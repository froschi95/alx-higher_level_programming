#!/usr/bin/node
const p = process.argv[2];
if (isNaN(p)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < p; i++) {
    console.log('C is fun');
  }
}
