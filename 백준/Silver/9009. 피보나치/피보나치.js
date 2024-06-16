let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = Number(input[0]);
const targets = input.slice(1, T+1).map(Number);

let answers = [];

for (let target of targets) {
  let fibonacciNumbers = [0, 1];
  while (fibonacciNumbers.at(-1) < target) {
    let newFibonacci = fibonacciNumbers.at(-1) + fibonacciNumbers.at(-2);
    fibonacciNumbers.push(newFibonacci);
  }

  let num = 0;
  let arr = [];
  while (num !== target) {
    let lastFibonacci = fibonacciNumbers.pop()
    if (num + lastFibonacci <= target) {
      num += lastFibonacci;
      arr.push(lastFibonacci);
    }
  }
  let answer = arr.sort((a,b) => a - b).join(" ");
  answers.push(answer);
}

console.log(answers.join('\n'));