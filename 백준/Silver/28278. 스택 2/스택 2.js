let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const process = input.slice(1, n + 1).map(x => x.split(" "));

let answers = [];
let stack = [];

for (let i = 0; i < n; i++) {
  switch (process[i][0]) {
    case "1":
      stack.push(process[i][1]);
      break;
    case "2":
      stack.length !== 0 ? answers.push(stack.pop()) : answers.push(-1);
      break;
    case "3":
      answers.push(stack.length);
      break;
    case "4":
      stack.length !== 0 ? answers.push(0): answers.push(1);
      break;
    case "5":
      stack.length !== 0 ? answers.push(stack.at(-1)) : answers.push(-1);
      break;
  }
}

console.log(answers.join('\n'));