function solution(myString, pat) {
    var answer = 0;
    if ((myString.toUpperCase()).includes(pat.toUpperCase())) {
        answer = 1;
    }
    return answer;
}