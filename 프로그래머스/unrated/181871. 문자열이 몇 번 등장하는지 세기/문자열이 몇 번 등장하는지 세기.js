function solution(myString, pat) {
    var answer = 0;
    for (i = 0; i < myString.length - pat.length + 1; i++) {
        var sliceStr = myString.slice(i,i + pat.length);
        if (sliceStr === pat) {
            answer += 1;
        }
    }
    return answer;
}