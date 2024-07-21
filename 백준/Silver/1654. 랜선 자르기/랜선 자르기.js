let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [k, n] = input[0].split(' ').map(Number);
const wires = input.slice(1, k + 1).map(Number);

let start = 1;
let end = Math.max(...wires);

let answer = 0;

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0;

  for (let wire of wires) {
    total += Math.floor(wire / mid);
  }

  if (total < n) {
    end = mid - 1;
  } else {
    answer = mid;
    start = mid + 1;
  }
}

console.log(answer);