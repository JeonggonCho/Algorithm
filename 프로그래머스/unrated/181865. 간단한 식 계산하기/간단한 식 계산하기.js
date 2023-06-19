function solution(binomial) {
    var answer = 0;
    const arr = binomial.split(" ");
    var num1 = parseInt(arr[0]);
    var num2 = parseInt(arr[2]);
    var calc = arr[1];
    if (calc === '+') {
        answer = num1 + num2;
    } else if (calc === '-') {
        answer = num1 - num2;
    } else if (calc === '*') {
        answer = num1 * num2;
    }
    return answer;
}