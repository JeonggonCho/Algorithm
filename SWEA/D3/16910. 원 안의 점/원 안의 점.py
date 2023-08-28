import math

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    cnt = 0
    for j in range(1, N + 1):
        cnt += math.floor((N ** 2 - j ** 2) ** (1 / 2))
    print(f'#{i} {cnt * 4 + N * 4 + 1}')