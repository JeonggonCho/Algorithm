function solution(strArr) {
    var answer = [];
    for (const i of strArr) {
        if (strArr.indexOf(i) % 2 === 0) {
            answer.push(i.toLowerCase());
        } else {
            answer.push(i.toUpperCase());
        }
    }
    return answer;
}