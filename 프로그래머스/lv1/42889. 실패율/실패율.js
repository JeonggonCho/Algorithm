function solution(N, stages) {
    var failArr = [];
    for (let i = 1; i <= N; i++) {
        var fail = 0; // 통과 못한 사람
        var play = 0; // 스테이지에 도달한 사람
        for (const j of stages) {
            if (j >= i) {
                play += 1;
            }
            if (j === i) {
                fail += 1;
            }
        }
        var failRate = fail / play; // 실패율
        failArr.push([i, failRate]);
    }
    failArr.sort(function(a, b) {
        return b[1] - a[1];
    });
    var answer = [];
    for (const k of failArr) {
        answer.push(k[0]);
    }
    return answer;
}