T = int(input())

for i in range(1, T+1):
    n, a, b = map(int, input().split())
    if (a + b) <= n:
        print(f'#{i} {min(a, b)} {0}')
    else:
        print(f'#{i} {min(a, b)} {(a + b) - n}')