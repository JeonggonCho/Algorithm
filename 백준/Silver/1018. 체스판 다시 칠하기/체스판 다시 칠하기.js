let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const matrix = input.slice(1, n + 1).map(x => x.split(''));

let answer = 100000000;

for (let i = 0; i < n - 7; i++) {
  for (let j = 0; j < m - 7; j++) {
    let board = [];
    for (let k = 0; k < 8; k++) {
      board.push(matrix[i + k].slice(j, j + 8));
    }
    let cnt = checkRePaint(board);
    answer = Math.min(answer, cnt);
  }
}

console.log(answer);

function checkRePaint(board) {
  let caseA = 0; // 왼쪽 위가 검정으로 시작하는 경우
  let caseB = 0; // 왼쪽 위가 흰색으로 시작하는 경우

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if (i % 2 === j % 2) {
        board[i][j] === 'B' ? caseB++ : caseA++;
      } else {
        board[i][j] === 'B' ? caseA++ : caseB++;
      }
    }
  }
  return Math.min(caseA, caseB);
}