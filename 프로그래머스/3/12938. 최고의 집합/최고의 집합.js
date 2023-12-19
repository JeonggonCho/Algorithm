function solution(n, s) {
    var answer = [];
    const num = Math.floor(s / n)
    const moreNum = num + 1;
    const cntMoreNum = s % n;
    
    if (num === 0) {
        return [-1];
    } else {
        for (let i = 1; i <= n - cntMoreNum; i++) {
            answer.push(num);
        }
        for (let j = 1; j <= cntMoreNum; j++) {
            answer.push(moreNum);
        }
    }
    return answer;
}