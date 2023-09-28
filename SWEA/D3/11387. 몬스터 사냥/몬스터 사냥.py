T = int(input())

for i in range(1, T+1):
    D, L, N = map(int, input().split())
    damage_sum = int(D * N + D * L * N * (N-1) / 200)
    print(f'#{i} {damage_sum}')