function solution(arr) {
    var answer = 1;
    while (true) {
        var cnt = 0;
        for (const i of arr) {
            if (answer % i === 0) {
                cnt++;
            } else {
                break;
            }
        }
        if (cnt === arr.length) {
            return answer;
            break;
        } else {
            answer++;
        }
    }
}