let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let N = parseInt(input[0]);
let terms = input.slice(1, N + 1);

terms = terms.map(x => x.split(" ").map(Number));
terms.sort((a, b) => a[1] - b[1] || a[0] - b[0]);

let cnt = 1;
let cur = 0;

for (let i = 1; i < N; i++) {
  if (terms[cur][1] <= terms[i][0]) {
    cur = i;
    cnt += 1;
  }
}

console.log(cnt);