function solution(myString) {
    var answer = [];
    var cntNum = 0;
    for (i = 0; i < myString.length; i++) {
        if (myString.charAt(i) === 'x') {
            answer.push(cntNum);
            cntNum = 0;
        } else {
            cntNum += 1;
        }
    }
    answer.push(cntNum);
    return answer;
}