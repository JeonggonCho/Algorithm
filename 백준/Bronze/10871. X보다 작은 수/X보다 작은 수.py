import sys

list1 = []
N, X = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for i in numbers:
    if i < X:
        list1.append(i)
print(*list1)