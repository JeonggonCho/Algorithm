import sys

cnt = 0

N = int(input())
numbers = list(map(int, sys.stdin.readline().split( )))
v = int(input())

for j in numbers:
    if j == v:
        cnt += 1
print(cnt)