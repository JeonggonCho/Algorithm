function solution(a, b) {
    var answer = 0;
    var num1 = parseInt(a.toString() + b.toString());
    var num2 = 2 * a * b;
    answer = Math.max(num1, num2);
    return answer;
}