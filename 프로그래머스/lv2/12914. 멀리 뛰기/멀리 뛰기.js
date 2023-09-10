function solution(n) {
    var answer = 0;
    var num1 = 0;
    var num2 = 1;
    for(let i = 2 ; i <= n + 1 ; i++) {
        answer = num1 + num2 % 1234567;
        num1 = num2;
        num2 = answer;
    }
    return answer % 1234567;
}