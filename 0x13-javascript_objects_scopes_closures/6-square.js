#!/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      if (i < this.height) {
        process.stdout.write('\n');
      }
    }
  } 
};
