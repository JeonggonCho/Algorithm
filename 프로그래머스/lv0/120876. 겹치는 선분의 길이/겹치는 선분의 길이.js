function solution(lines) {
    var answer = 0;
    var obj = {};
    for (const i of lines) {
        for (let j = i[0]; j < i[1]; j++) {
            if (obj[j] === undefined) {
                obj[j] = 1;
            } else {
                obj[j]++;
            }
        }
    }
    for (const k of Object.values(obj)) {
        if (k > 1) {
            answer++;
        }
    }
    return answer;
}