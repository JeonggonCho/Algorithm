let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const heights = input[1].split(' ').map(Number);

let start = 1;
let end = Math.max(...heights);

let answer = 0;
while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let total = 0

  for (let i of heights) {
    if (i > mid) {
      total += i - mid;
    }
  }

  if (total >= m) {
    answer = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(answer);