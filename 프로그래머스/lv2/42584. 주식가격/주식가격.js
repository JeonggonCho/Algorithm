// function solution(prices) {
//     var answer = [];
//     var leng = prices.length;
//     for (let i = 0; i < leng; i++) {
//         var price = prices.shift();
//         var check = false;
//         var max = prices.length;
//         for (let j = 0; j < max; j++) {
//             if (prices[j] < price) {
//                 answer.push(j + 1);
//                 check = true;
//                 break;
//             }
//         }
//         if (check === false) {
//             answer.push(max);
//         }
//     }
//     return answer;
// }

function solution(prices) {
    const n = prices.length;
    const answer = new Array(n).fill(0);
    const stack = [];

    for (let i = 0; i < n; i++) {
        while (stack.length && prices[stack[stack.length - 1]] > prices[i]) {
            const top = stack.pop();
            answer[top] = i - top;
        }
        stack.push(i);
    }

    while (stack.length) {
        const top = stack.pop();
        answer[top] = n - 1 - top;
    }

    return answer;
}