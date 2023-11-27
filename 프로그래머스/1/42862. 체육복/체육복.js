function solution(n, lost, reserve) {
    var answer = 0;
    let uniform = {}
    
    for (let i = 1; i <= n; i++) {
        if ((lost.includes(i) && reserve.includes(i)) || (!lost.includes(i) && !reserve.includes(i))) {
            uniform[i] = 1;
        } else if (lost.includes(i)) {
            uniform[i] = 0;
        } else if (reserve.includes(i)) {
            uniform[i] = 2;
        }
    }
    
    for (let j = 1; j <= n; j++) {
        if (uniform[j] === 0 && uniform[j-1] === 2) {
            uniform[j] += 1;
            uniform[j-1] -= 1;
        } else if (uniform[j] === 0 && uniform[j+1] === 2) {
            uniform[j] += 1;
            uniform[j+1] -= 1;
        }
    }
    
    for (let k = 1; k <= n; k++) {
        if (uniform[k] !== 0) {
            answer += 1;
        }
    }
    return answer;
}