function solution(a, d, included) {
    var answer = 0;
    for (const i of included) {
        if (i === true) {
            answer += a;
            a += d;
        } else {
            a += d;
        }
    }
    return answer;
}