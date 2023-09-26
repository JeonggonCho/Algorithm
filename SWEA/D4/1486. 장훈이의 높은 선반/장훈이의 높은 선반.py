from  itertools import combinations

T = int(input())

for i in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    li = []

    for j in range(1, N+1):
        for k in combinations(H, j):
            li.append(sum(k))

    sorted_li = sorted(li)

    for l in sorted_li:
        if l >= B:
            result = l - B
            break

    print(f'#{i} {result}')