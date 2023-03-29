import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1, n+1):
    num_list = combinations(numbers, i)

    for j in num_list:
        if sum(j) == s:
            cnt += 1
print(cnt)