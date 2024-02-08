function solution(m, n, puddles) {
    const divNum = 1000000007;
    const dp = Array.from({ length: n }, () => Array(m).fill(0));
    dp[0][0] = 1;

    for (let puddle of puddles) {
        dp[puddle[1] - 1][puddle[0] - 1] = -1;
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (dp[i][j] === -1) {
                continue;
            }
            if (i > 0 && dp[i - 1][j] !== -1) {
                dp[i][j] += dp[i - 1][j] % divNum;
            }
            if (j > 0 && dp[i][j - 1] !== -1) {
                dp[i][j] += dp[i][j - 1] % divNum;
            }
        }
    }
    return dp[n - 1][m - 1] % divNum;
}
