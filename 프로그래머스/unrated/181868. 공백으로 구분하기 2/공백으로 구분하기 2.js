function solution(my_string) {
    var answer = [];
    const arr = my_string.split(' ');
    for (const i of arr) {
        if (i !== '') {
            answer.push(i);
        }
    }
    return answer;
}