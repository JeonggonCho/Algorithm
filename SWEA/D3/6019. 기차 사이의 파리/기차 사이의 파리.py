T = int(input())

for i in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    dist = round(F * time, 6)
    print(f'#{i} {dist}')