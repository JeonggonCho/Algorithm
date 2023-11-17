import sys

n = int(sys.stdin.readline())
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

if n == 1:
    nums = sorted([a, b, c, d, e, f])
    print(sum(nums[0:5]))

else:
    combi = []
    for i in [a, f]:
        for j in [b, e]:
            for k in [c, d]:
                combi.append([i, j, k])

    results = []
    for l in combi:
        l.sort()
        result = sum(l) * 4 + sum(l[0:2]) * (8 * n - 12) + l[0] * (5 * n - 6) * (n - 2)
        results.append(result)

    print(min(results))
