function solution(l, r) {
    var answer = [];
    var exNum = ["1", "2", "3", "4", "6", "7", "8", "9"];
    for (let i = l; i < r + 1; i++) {
        var check = 0;
        var caseNum = (i.toString()).split("");
        for (const j of caseNum) {
            if (exNum.includes(j)) {
                check = 1;
            }
        }
        if (check === 0) {
            answer.push(i);
        }
    }
    if (answer.length) {
        return answer;
    } else {
        answer.push(-1);
        return answer;
    }
}