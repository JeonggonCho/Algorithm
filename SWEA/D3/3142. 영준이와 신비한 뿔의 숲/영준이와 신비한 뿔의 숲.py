T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    print(f'#{i} {2 * m - n} {n - m}')