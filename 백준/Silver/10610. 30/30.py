import sys
from itertools import combinations

n = sorted(list(sys.stdin.readline().rstrip()))

combi = combinations(n, len(n))
for i in combi:
    target = int(''.join(sorted(i, reverse=True)))
    if target % 30 == 0:
        print(target)
        break
else:
    print(-1)