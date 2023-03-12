import math

T = int(input())

for i in range(1, T+1):
    n, d = map(int, input().split())
    print(f'#{i} {math.ceil(n / (d * 2 + 1))}')