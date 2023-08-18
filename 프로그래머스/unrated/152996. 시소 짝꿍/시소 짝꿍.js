// function solution(weights) {
//     var answer = 0;
//     var len = weights.length;
//     for (let i = 0; i < len; i++) {
//         var weight = weights.pop();
//         var weights2 = weights.map((x) => x * 2);
//         var weights3 = weights.map((x) => x * 3);
//         var weights4 = weights.map((x) => x * 4);
//     }
//     return answer;
// }

function solution(weights) {
    var answer = 0;
    const weight = {};
    const cal = [1, 3/2, 2, 4/3];

    weights.sort((a, b)=> b - a).forEach((x) => {
        let num;
        cal.forEach((i)=>{
            if( num = x * i, weight[num] ){
              answer += weight[num];
            }
        });
        if (!weight[x]) {
            weight[x] = 1;
        } else {
            weight[x]++;
        }
    });
    return answer;
}