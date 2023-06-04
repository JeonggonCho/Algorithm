function solution(myString) {
    var answer = [];
    var char = '';
    for (i = 0; i < myString.length; i ++) {
        if (myString.charAt(i) !== 'x') {
            char += myString.charAt(i);
        } else {
            if (char.length !== 0) {
                answer.push(char);
                char = '';
            }
        }
    }
    if (char.length !== 0) {
        answer.push(char);
    }
    answer.sort();
    return answer;
}