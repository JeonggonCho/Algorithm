T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    num_li = list(map(int, input().split()))

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for j in range(1, N + 1):
        for k in range(K + 1):
            if k >= num_li[j - 1]:
                dp[j][k] += dp[j - 1][k - num_li[j - 1]]
            dp[j][k] += dp[j - 1][k]

    result = dp[N][K]
    print(f'#{i} {result}')