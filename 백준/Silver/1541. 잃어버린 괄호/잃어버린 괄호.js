let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let formulas = input[0].split("-");
let results = [];

for (let i = 0; i < formulas.length; i++) {
  let numbers = formulas[i].split("+").map(x => parseInt(x))
  const sumNumbers = numbers.reduce((acc, cur) => acc + cur, 0);
  results.push(sumNumbers);
}

if (results.length === 1) console.log(results[0]);
else {
  let answer = results[0];
  for (let j = 1; j < results.length; j++) {
    answer -= results[j];
  }
  console.log(answer);
}