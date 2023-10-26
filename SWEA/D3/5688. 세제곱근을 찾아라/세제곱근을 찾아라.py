results = []

T = int(input())

for i in range(1, T+1):
    N = int(input())
    cubic = round(N ** (1.0 / 3.0))
    if cubic ** 3 == N:
        results.append(f'#{i} {cubic}')
    else:
        results.append((f'#{i} -1'))

for j in results:
    print(j)