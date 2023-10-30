results = []

T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    dp = [1 for j in range(N)]

    for k in range(N):
        for l in range(k):
            if arr[k] > arr[l]:
                dp[k] = max(dp[k], dp[l] + 1)

    results.append(f'#{i} {max(dp)}')

for m in results:
    print(m)