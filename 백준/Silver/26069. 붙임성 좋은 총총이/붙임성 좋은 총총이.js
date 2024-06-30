let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const meets = input.slice(1, n + 1).map(x => x.split(' '));

let flag = false;
let set = new Set();
  for (let i = 0; i < meets.length; i++) {
  if (meets[i].includes('ChongChong')) {
    set.add(meets[i][0]);
    set.add(meets[i][1]);
    flag = true;
  } else if (flag && set.has(meets[i][0]) || set.has(meets[i][1])) {
    set.add(meets[i][0]);
    set.add(meets[i][1]);
  }
}

console.log(set.size);