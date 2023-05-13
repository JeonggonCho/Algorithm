function solution(a, b) {
    var answer = 0;
    var num1 = operation(a, b);
    var num2 = operation(b, a);
    if (num1 >= num2) {
        answer = num1;
    } else {
        answer = num2;
    }
    return answer;
}
function operation(c, d) {
    const answer = parseInt(c.toString() + d.toString());
    return answer;
}