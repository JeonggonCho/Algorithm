function solution(my_string) {
    var answer = [];
    for (let i = 65; i < 91; i++) {
        var cntNum = 0;
        for (const j of my_string) {
            if (j === String.fromCharCode(i)) {
                cntNum += 1;
            }
        }
        answer.push(cntNum);
    }
    for (let k = 97; k < 123; k++) {
        cntNum = 0;
        for (const l of my_string) {
            if (l === String.fromCharCode(k)) {
                cntNum += 1;
            }
        }
        answer.push(cntNum);
    }
    return answer;
}