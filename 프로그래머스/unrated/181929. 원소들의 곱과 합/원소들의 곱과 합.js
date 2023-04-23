function solution(num_list) {
    var answer = 0;
    var a = 1;
    var b = 0;
    for (const i of num_list) {
        a *= i;
        b += i;
    }
    if (a < b ** 2) {
        answer = 1;
    }
    return answer;
}