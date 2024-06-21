let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [n, k] = input[0].split(" ").map(Number);

let answer = 0;

const countOne = (num) => {
  let cnt = 0;
  while (num > 0) {
    if (num % 2 === 1) {
      cnt++;
    }
    num = Math.floor(num / 2);
  }
  return cnt;
};

while (true) {
  let cntOne = countOne(n);
  if (cntOne <= k) {
    break;
  } else {
    n++;
    answer++;
  }
}

console.log(answer);