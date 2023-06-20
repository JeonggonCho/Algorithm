function solution(numLog) {
    var answer = '';
    for (i = 0; i < numLog.length - 1; i++) {
        var gapValue = numLog[i+1] - numLog[i];
        if (gapValue === 1) {
            answer += 'w';
        } else if (gapValue === -1) {
            answer += 's';
        } else if (gapValue === 10) {
            answer += 'd';
        } else if (gapValue === -10) {
            answer += 'a';
        }
    }
    return answer;
}