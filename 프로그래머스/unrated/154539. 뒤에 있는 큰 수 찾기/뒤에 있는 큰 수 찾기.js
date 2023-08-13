// function solution(numbers) {
//     var answer = [];
//     var n = numbers.length;
//     for (let i = 0; i < n; i++) {
//         var num = numbers[i];
//         var back = numbers.slice(i + 1);
//         var check = false;
//         while (back.length !== 0) {
//             var backNum = back.shift();
//             if (backNum > num) {
//                 answer.push(backNum);
//                 check = true;
//                 break;
//             }
//         }
//         if (back.length === 0 && check === false) {
//             answer.push(-1);
//         }
//     }
//     return answer;
// }

function solution(numbers) {
    const answer = new Array(numbers.length).fill(-1);
    const stack = [];
    for (let i = 0; i < numbers.length; i++) {
        while (stack.length && numbers[stack[stack.length - 1]] < numbers[i]) {
            answer[stack.pop()] = numbers[i];
        }
        stack.push(i);
    }
    return answer;
}
