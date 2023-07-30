// 시간초과
// function solution(n, left, right) {
//     var answer = [];
//     for (let i = 0; i < n; i++) {
//         for (let j = 0; j < n; j++) {
//             var idx = i * n + j;
//             if (left <= idx && idx <= right) {
//                 answer.push(Math.max(i, j) + 1);
//             }
//         }
//     }
//     return answer;
// }

function solution(n, left, right) {
    var answer = [];
    for (let i = left; i <= right; i++) {
        var quot = Math.floor(i / n) + 1;
        var remain = i % n + 1;
        answer.push(Math.max(quot, remain));
    }
    return answer;
}