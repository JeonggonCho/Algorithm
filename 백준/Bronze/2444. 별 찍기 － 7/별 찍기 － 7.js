let fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin'));

let answer = [];

for (let i = 1; i < input * 2; i++) {
  if (i <= input) {
    let row = " ".repeat(input - i) + "*".repeat(2 * i - 1);
    answer.push(row);
  } else {
    let row = " ".repeat(i - input) + "*".repeat(2 * (input * 2 - i) - 1);
    answer.push(row);
  }
}

console.log(answer.join('\n'));