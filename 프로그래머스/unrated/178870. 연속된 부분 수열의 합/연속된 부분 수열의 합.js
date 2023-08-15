// function solution(sequence, k) {
//     var answer = [];
//     for (let i = 0; i < sequence.length; i++) {
//         for (let j = i; j < sequence.length + 1; j++) {
//             var numbers = sequence.slice(i, j);
//             let sum = 0;
//             numbers.forEach(num => {
//                 sum += num;
//             })
//             if (sum === k && answer.length === 0) {
//                 answer.push([i, j - 1]);
//                 break;
//             } else if (sum === k && (answer[0][1] - answer[0][0]) > j- 1 -i) {
//                 answer.pop();
//                 answer.push([i, j - 1]);
//                 break;
//             }
//         }
//     }
//     return answer[0];
// }

function solution(sequence, k) {
  let left = 0;
  let right = 0;
  let sum = 0;
  let answer = [];

  while (right <= sequence.length) {
    if (sum == k) {
      if (answer.length == 0 || (right - 1) - left < answer[1] - answer[0]) {
        answer = [left, right - 1];
      }
      sum -= sequence[left++];
    } else if (sum < k) {
      sum += sequence[right++];
    } else { 
      sum -= sequence[left++];
    }
  }
  return answer;
}
