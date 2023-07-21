function solution(code) {
    var answer = '';
    var mode = 0;
    const len = code.length;
    for (let i = 0; i < len; i++) {
        if (mode === 0) {
            if (code.charAt(i) !== '1' && i % 2 === 0) {
                answer += code.charAt(i);
            } else if (code.charAt(i) === '1') {
                mode = 1;
            }
        } else {
            if (code.charAt(i) !== '1' && i % 2 !== 0) {
                answer += code.charAt(i);
            } else if (code.charAt(i) === '1') {
                mode = 0;
            }
        }
    }
    if (answer.length) {
        return answer;
    } else {
        return 'EMPTY';
    }
}