const dfs = (result, depth) => {
  if (depth === n - 1) {
    let str = '';
    for (let i = 0; i < n - 1; i++) {
      str += arr[i] + result[i];
    }
    str += arr[n - 1] + '';

    let current = eval(str.split(' ').join(''));

    if (current === 0) console.log(str);
    return;
  }

  for (let j of [' ', '+', '-']) {
    result.push(j);
    dfs(result, depth + 1);
    result.pop();
  }
};

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let test = Number(input[0]);
for (let l = 1; l <= test; l++) {
  n = Number(input[l].trim());
  arr = [];
  for (let m = 1; m <= n; m++) {
    arr.push(m);
  }
  dfs([], 0);
  console.log();
}
