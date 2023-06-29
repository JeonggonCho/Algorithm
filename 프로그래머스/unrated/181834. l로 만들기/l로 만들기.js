function solution(myString) {
    var answer = '';
    for (let i = 0; i < myString.length; i++) {
        if (myString.charCodeAt(i) < 108) {
            answer += 'l';
        } else {
            answer += myString.at(i);
        }
    }
    return answer;
}