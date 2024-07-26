let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();

let n = Number(input);
let arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(i);
}

let visited = new Array(n).fill(false);
let selected = [];

let answer = '';

const dfs = (arr, depth) => {
  if (depth === n) {
    let result = [];
    for (let j of selected) {
      result.push(arr[j]);
    }
    for (let k of result) {
      answer += k + ' ';
    }
    answer += '\n';
  }
  
  for (let l = 0; l < arr.length; l++) {
    if (visited[l]) continue;
    selected.push(l);
    visited[l] = true;
    dfs(arr, depth + 1);
    selected.pop();
    visited[l] = false;
  }
};

dfs(arr, 0);

console.log(answer);