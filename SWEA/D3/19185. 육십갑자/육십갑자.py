T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    Q = int(input())

    results = []
    for j in range(Q):
        Y = int(input())
        result = ''
        result += s[Y % N - 1]
        result += t[Y % M - 1]
        results.append(result)
    print(f'#{i} {" ".join(results)}')