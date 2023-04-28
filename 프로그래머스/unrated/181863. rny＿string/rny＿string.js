function solution(rny_string) {
    var answer = '';
    for (const i of rny_string) {
        if (i === 'm') {
            answer += 'rn';
        } else {
            answer += i;
        }
    }
    return answer;
}