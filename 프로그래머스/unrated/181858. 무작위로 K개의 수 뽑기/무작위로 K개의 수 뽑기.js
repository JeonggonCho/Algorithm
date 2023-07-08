function solution(arr, k) {
    var answer = [];
    for (const i of arr) {
        if (!answer.includes(i)) {
            answer.push(i);
        }
        if (answer.length === k) {
            return answer;
        }
    }
    const len = answer.length;
    for (let j = 0; j < k - len; j++) {
        answer.push(-1);
    }
    return answer;
}