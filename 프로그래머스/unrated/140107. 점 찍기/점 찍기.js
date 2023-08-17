// function solution(k, d) {
//     var answer = 0;
//     var i = 0;
//     var arr = [];
//     while (i * k <= d) {
//         arr.push(i * k);
//         i++;
//     }
//     for (const j of arr) {
//         for (const k of arr) {
//             var dist = Math.sqrt(j ** 2 + k ** 2);
//             if (dist <= d) {
//                 answer++;
//             }
//         }
//     }
//     return answer;
// }


function solution(k, d) {
    var answer = 0;
    for (let i = 0; i <= d; i += k) {
        const num = Math.sqrt(d ** 2 - i ** 2);
        answer += Math.floor(num / k) + 1;
    }

    return answer;
}