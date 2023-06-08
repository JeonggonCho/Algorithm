function solution(arr, n) {
    var answer = [];
    if (arr.length % 2 !== 0) {
        var cnt = 0;
        var arrReverse = arr.reverse();
        var arrLength = arr.length;
        for (i = 0; i < arrLength; i++) {
            if (cnt % 2 === 0) {
                answer.push(arrReverse.pop() + n);
                cnt += 1;
            } else {
                answer.push(arrReverse.pop());
                cnt += 1;
            }
        }
    } else {
        var cnt = 0;
        var arrReverse = arr.reverse();
        var arrLength = arr.length;
        for (i = 0; i < arrLength; i++) {
            if (cnt % 2 !== 0) {
                answer.push(arrReverse.pop() + n);
                cnt += 1;
            } else {
                answer.push(arrReverse.pop());
                cnt += 1;
            }
        }
    }
    return answer;
}