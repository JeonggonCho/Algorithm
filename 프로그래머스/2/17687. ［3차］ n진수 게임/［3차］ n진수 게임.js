function solution(n, t, m, p) {
    let answer = '';
    let numbers = '';
    let num = 0;
    let index = p - 1;
    while (numbers.length < p + m * (t - 1)) {
        numbers += num.toString(n).toUpperCase();
        num++;
    }
    while (answer.length !== t) {
        answer += numbers[index];
        index += m;
    }
    return answer;
}