function solution(strArr) {
    var answer = 0;
    const arr = [];
    const result = {};
    for (const i of strArr) {
        arr.push(i.length);
    }
    arr.forEach((x) => {
        result[x] = (result[x] || 0) + 1;
    })
    for (const j in result) {
        if (Number(result[j]) >= answer) {
            answer = Number(result[j]);
        }
    }
    return answer;
}