function solution(n) {
    var answer = [];
    for (let i = 0; i < n; i++) {
        answer.push([]);
    }
    for (let j = 0; j < n; j++) {
        for (let k = 0; k < n; k++) {
            if (j === k) {
                (answer[j]).push(1);
            } else {
                (answer[j]).push(0);
            }
        }
    }
    return answer;
}