let fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin'));
let points = 2;
for (let i = 0; i < input; i++) {
  points = points * 2 - 1;
}
console.log(points ** 2);