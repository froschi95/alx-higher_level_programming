#!/usr/bin/node
const p = process.argv[2];
if (isNaN(p)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < p; i++) {
    console.log('X'.repeat(p));
  }
}
