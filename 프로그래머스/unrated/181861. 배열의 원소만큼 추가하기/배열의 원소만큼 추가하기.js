function solution(arr) {
    var answer = [];
    for (const i of arr) {
        for (j = 0; j < i; j++) {
            answer.push(i);
        }
    }
    return answer;
}