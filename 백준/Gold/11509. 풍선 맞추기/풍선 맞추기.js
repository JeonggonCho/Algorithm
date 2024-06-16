let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let balloons = Number(input[0]);
let heights = input[1].split(" ").map(Number);

let answer = 0;
let used = Array(balloons).fill(false);

for (let i = 0; i < balloons; i++) {
  if (!used[i]) {
    answer++;
    let cur = heights[i];
    for (let j = i; j < balloons; j++) {
      if (cur === heights[j] && !used[j]) {
        used[j] = true;
        cur--;
      }
    }
  }
}

console.log(answer);