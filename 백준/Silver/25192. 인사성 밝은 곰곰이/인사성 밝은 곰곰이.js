let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
let chars = input.slice(1, n + 1);

let answer = 0;

let logs = new Set();
for (let i = 0; i < n; i++) {
  if (chars[i] === "ENTER") {
    answer += logs.size;
    logs = new Set();
  } else {
    if (!logs.has(chars[i])) {
      logs.add(chars[i]);
    }
  }
}
answer += logs.size;

console.log(answer);