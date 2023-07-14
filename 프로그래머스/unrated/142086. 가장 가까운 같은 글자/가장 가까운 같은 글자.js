function solution(s) {
    var answer = [];
    for (let i = 0; i < s.length; i++) {
        var frontChar = s.slice(0, i);
        var checkPoint = 0;
        for (let j = 1; j <= frontChar.length; j++) {
            if (frontChar.charAt(frontChar.length - j) === s.charAt(i)) {
                answer.push(j);
                checkPoint = 1;
                break;
            }
        }
        if (checkPoint !== 1) {
            answer.push(-1);
        }
    }
    return answer;
}