function solution(q, r, code) {
    var answer = '';
    for (i = 0; i < code.length; i++) {
        if (i % q === r) {
            answer += code.charAt(i);
        }
    }
    return answer;
}