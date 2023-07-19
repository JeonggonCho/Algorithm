function solution(k, score) {
    var answer = [];
    var topRank = [];
    for (const i of score) {
        if (topRank.length < k) {
            topRank.push(i);
            answer.push(Math.min(...topRank));
        } else {
            topRank.push(i);
            topRank.sort(function(a, b) {
                return b - a;
            });
            topRank.pop();
            answer.push(Math.min(...topRank));
        }
    }
    return answer;
}