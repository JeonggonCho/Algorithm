// 효율성 검사에서 시간초과
// function solution(s) {
//     const cnt = s.length / 2;
//     for (let i = 0; i < cnt; i++) {
//         var len = s.length
//         var check = 0;
//         for (let j = 0; j < len; j++) {
//             var char = s.charAt(j);
//             if (char === s.charAt(j + 1)) {
//                 s = s.replace(char.repeat(2), "");
//                 check = 1;
//                 break;
//             }
//         }
//         if (check === 0) {
//             return 0;
//         }
//     }
//     return 1;
// }

// 스택이용
function solution(s) {
    const arr = [];
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === arr[arr.length - 1]) {
            arr.pop();
        } else {
            arr.push(s.charAt(i));
        }
    }
    let answer = (arr.length) ? 0 : 1;
    return answer;
}