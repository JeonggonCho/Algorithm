let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

function cantor(n) {
  if (n === 0) {
    return '-';
  }
  let prev = cantor(n - 1);
  let spaces = ' '.repeat(3 ** (n - 1));
  return prev + spaces + prev;
}

let answers = input.map(n => cantor(n));
console.log(answers.join('\n'));