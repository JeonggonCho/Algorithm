import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    categories = {}
    result = 0

    for j in range(n):
        stuff, category = sys.stdin.readline().split()
        if category not in categories:
            categories[category] = 1
        else:
            categories[category] += 1
    amount = list(categories.values())

    result = 1
    for k in amount:
        result *= (k + 1)
    print(result - 1)
