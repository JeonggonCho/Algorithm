from itertools import combinations

T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    sum_values = set()
    combi = combinations(numbers, 3)
    for j in combi:
        sum_values.add(sum(j))
    sorted_values = sorted(sum_values, reverse=True)
    print(f'#{i} {sorted_values[4]}')