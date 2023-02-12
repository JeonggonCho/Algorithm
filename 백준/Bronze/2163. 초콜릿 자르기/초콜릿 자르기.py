import sys

n, m = map(int, input().split())

if n > m:
    print((m - 1) + (n - 1) * m)
else:
    print((n - 1) + (m - 1) * n)