T = int(input())
results = []

for i in range(1, T+1):
    A, B, C, D = map(int, input().split())
    set1 = set(range(A, B+1))
    set2 = set(range(C, D+1))
    intersected = list(set1.intersection(set2))
    points = len(intersected)
    if points <= 1:
        results.append(f'#{i} 0')
    else:
        results.append(f'#{i} {points-1}')

for j in results:
    print(j)