function solution(myString, pat) {
    var answer = 0;
    newString = '';
    for(const i of myString) {
        if (i === 'A') {
            newString += 'B';
        } else {
            newString += 'A';
        }
    }
    if (newString.includes(pat)) {
        answer = 1;
    }
    return answer;
}