function solution(arr) {
    var answer = [];
    var checkPoint = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 2) {
            checkPoint.push(i);
        }
    }
    if (checkPoint.length === 0) {
        answer.push(-1);
    } else {
        answer = arr.slice(checkPoint[0], checkPoint.at(-1) + 1);
    }
    return answer;
}