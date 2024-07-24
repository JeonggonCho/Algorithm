function solution(n) {
    let queens = [];
    let answer = 0;
    
    function isPossible(x, y) {
        for (let [a, b] of queens) {
            if (a == x || b == y) return false;
            if (Math.abs(a - x) === Math.abs(b - y)) return false;
        }
        return true;
    }
    
    function dfs(row) {
        if (row === n) answer++;
        for (let i = 0; i < n; i++) {
            if (!isPossible(row, i)) continue;
            queens.push([row, i]);
            dfs(row + 1);
            queens.pop();
        }
    }
    dfs(0);
    return answer;
}