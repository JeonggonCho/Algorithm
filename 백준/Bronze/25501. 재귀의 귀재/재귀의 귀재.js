let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = Number(input[0]);
const tests = input.slice(1, T + 1);

let answers = [];

for (let i = 0; i < T; i++) {
  let recursionCnt = 0;
  answers.push(isPalindrome(tests[i], recursionCnt));
}

function recursion(s, l, r, recusionCnt) {
  recusionCnt++;
  if(l >= r) {
    return `1 ${recusionCnt}`;
  } else if(s[l] !== s[r]) {
    return `0 ${recusionCnt}`;
  } else {
    return recursion(s, l+1, r-1, recusionCnt);
  }
}

function isPalindrome(s, recursionCnt) {
  return recursion(s, 0, s.length - 1, recursionCnt);
}

console.log(answers.join('\n'));