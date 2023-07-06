function solution(arr) {
    var answer = arr;
    var a = arr.length;
    var b = arr[0].length;
    if (a > b) {
        for (let i = 0; i < a; i++) {
            for (let j = 0; j < a - b; j++) {
                answer[i].push(0);
            }
        }
    } else if (a < b) {
        for (let k = 0; k < b - a; k++) {
            var zeroArr = [];
            for (let l = 0; l < b; l++) {
                zeroArr.push(0);
            }
            answer.push(zeroArr);
        }
    }
    return answer;
}