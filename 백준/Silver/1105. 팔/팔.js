let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [l, r] = input[0].split(" "); // l과 r 입력받기
let result = 0;

// 두 수의 자릿수가 다른 경우, 10, 100, 1000...과 같은 10의 거듭제곱이 포함되므로 8이 아예 없는 0이 최소
if (l.length !== r.length) {
  console.log(0);
  return;
} else {
  // 자릿수가 같은 경우, 높은 자리 수부터 비교
  for (let i = 0; i < l.length; i++) {
    if (l[i] === r[i]) {
      if (l[i] === "8") {
        result++;
      }
    } else {
      break;
    }
  }
  console.log(result);
  return;
}