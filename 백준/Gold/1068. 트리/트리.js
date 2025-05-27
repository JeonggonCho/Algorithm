let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]); // 노드 개수
const arr = input[1].split(' ').map(Number); // 각 노드의 부모 노드 번호, 루트 노드는 -1
const removedNode = Number(input[2]); // 지울 노드 번호

let cnt = 0; // 리프노드 개수 카운트

const dfs = (num, arr) => {
  arr[num] = -2; // 삭제 처리
  for (let i = 0; i < n; i++) {
    if (arr[i] === num) {
      dfs(i, arr); // 자식도 삭제
    }
  }
};

dfs(removedNode, arr);

for (let j = 0; j < n; j++) {
  if (arr[j] !== -2) {
    let isLeaf = true;
    for (let k = 0; k < n; k++) {
      if (arr[k] === j) {
        isLeaf = false;
        break;
      }
    }
    if (isLeaf) cnt++;
  }
}

console.log(cnt);