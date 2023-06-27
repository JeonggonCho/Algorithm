function solution(myStr) {
    var answer = [];
    var char = "";
    for (const i of myStr) {
        if (i === 'a' || i === 'b'|| i === 'c') {
            if (char.length !== 0) {
                answer.push(char);
                char = "";
            }
        } else {
            char += i;
        }
    }
    if (char.length !== 0) {
        answer.push(char);
    }
    if (answer.length === 0) {
        return ["EMPTY"];
    }
    return answer;
}