function solution(s) {
    var answer = 0;
    while (s.length !== 0) {
        var x = s[0];
        var same = 0;
        var diff = 0;
        var check = false;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === x) {
                same++;
            } else {
                diff++;
            }
            if (same === diff) {
                answer++;
                s = s.substring(i + 1);
                check = true;
                break;
            }
        }
        if (check === false) {
            answer++;
            break;
        }
    }
    return answer;
}