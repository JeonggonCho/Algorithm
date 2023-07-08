function solution(picture, k) {
    var answer = [];
    for (const i of picture) {
        var char = '';
        for (const j of i) {
            char += (j.repeat(k));
        }
        for (let l = 0; l < k; l++) {
            answer.push(char);
        }
    }
    return answer;
}