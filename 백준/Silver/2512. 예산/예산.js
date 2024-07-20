let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const budgets = input[1].split(' ').map(x => Number(x));
const m = Number(input[2]);

let start = 1;
let end = budgets.reduce((accumulator, currentValue) => Math.max(accumulator, currentValue));

let result = 0;
while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0;
  for (i of budgets) {
    total += Math.min(mid, i);
  }
  if (total <= m) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);