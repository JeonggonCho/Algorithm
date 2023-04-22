function solution(arr, k) {
    var answer = [];
    for (const i of arr) {
        if (k % 2 === 1) {
            answer.push(i * k);
        } else {
            answer.push(i + k);
        }
    }
    return answer;
}