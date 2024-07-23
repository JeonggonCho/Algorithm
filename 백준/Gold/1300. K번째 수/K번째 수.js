let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, k] = input.map(Number);

let start = 1;
let end = n ** 2;

let result = 0;

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += Math.min(parseInt(mid / i), n);
  }
  if (total >= k) {
    result = mid;
    end = mid - 1;
  } else {
    start = mid + 1;
  }
}

console.log(result);