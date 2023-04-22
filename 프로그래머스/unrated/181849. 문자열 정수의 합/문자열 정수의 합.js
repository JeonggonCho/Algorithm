function solution(num_str) {
    var answer = 0;
    for (const i of num_str) {
        answer += parseInt(i)
    }
    return answer;
}