function solution(start, end) {
    var answer = [];
    for(let i = start; i > end - 1; i--) {
        answer.push(i);
    }
    return answer;
}