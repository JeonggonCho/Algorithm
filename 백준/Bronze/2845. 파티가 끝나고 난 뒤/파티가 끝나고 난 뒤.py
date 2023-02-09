import sys

L, P = map(int, sys.stdin.readline().split())

article = list(map(int, sys.stdin.readline().split()))

num = L * P

for i in article:
    print(i - num, end=' ')