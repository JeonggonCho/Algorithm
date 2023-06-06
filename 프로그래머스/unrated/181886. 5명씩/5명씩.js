function solution(names) {
    var answer = [];
    for (const i of names) {
        if ((names.indexOf(i) + 1) % 5 === 1 ) {
            answer.push(i);
        }
    }
    return answer;
}