let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(" ").map(Number); // 행렬의 크기 n, m
const matA = input.slice(1, n+1).map(el => el.split("").map(Number)); // 행렬A
const matB = input.slice(n+1).map(el => el.split("").map(Number)); // 행렬B

let cnt = 0; // 뒤집기 횟수

// 행렬 뒤집기
const invertMatrix = (mat, startRow, startCol) => {
  for (let row = startRow; row < startRow+3; row++) {
    for (let col = startCol; col < startCol+3; col++) {
      (mat[row][col] === 1) ? mat[row][col] = 0 : mat[row][col] = 1;
    }
  }
};

// 두 배열이 같은지 판별하기
const isSameMatrix = (compA, compB) => {
  for (let i = 0; i < compA.length; i++) {
    for (let j = 0; j < compA[0].length; j++) {
      if (compA[i][j] !== compB[i][j]) return false;
    }
  }
  return true;
};

if (n < 3 || m < 3) {
  console.log(isSameMatrix(matA, matB) ? 0 : -1);
} else {
  for (let matRow = 0; matRow <= n-3; matRow++) {
    for (let matCol = 0; matCol <= m-3; matCol++) {
      if (matA[matRow][matCol] !== matB[matRow][matCol]) {
        invertMatrix(matA, matRow, matCol);
        cnt++;
      }
    }
  }
  console.log(isSameMatrix(matA, matB) ? cnt : -1);
}