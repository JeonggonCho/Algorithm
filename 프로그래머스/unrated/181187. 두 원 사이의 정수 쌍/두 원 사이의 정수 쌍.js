// 시간초과
// function solution(r1, r2) {
//     let points = 0;
//     for (let x = 1; x <= r2; x++) {
//         for (let y = 1; y <= r2; y++) {
//             var r = Math.sqrt(x ** 2 + y ** 2)
//             if (Math.sqrt(x ** 2 + y ** 2) <= r2 && Math.sqrt(x ** 2 + y ** 2) >= r1) {
//                 points++;
//             }
//         }
//     }
//     const answer = (points + (r2 - r1 + 1)) * 4
//     return answer;
// }


function solution(r1, r2) {
    let points = 0;
    for (let x = 1; x <= r2; x++) {
        if (x > r1) {
            y1 = 0;
        } else {
            var y1 = Math.ceil(Math.sqrt(r1 ** 2 - x ** 2));
        }
        var y2 = Math.floor(Math.sqrt(r2 ** 2 - x ** 2));
        points += (y2 - y1 + 1);
    }
    const answer = points * 4
    return answer;
}
