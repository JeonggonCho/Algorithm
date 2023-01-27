import sys

N, M = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline() for _ in range(N)])
cnt = 0
for i in range(M):
    t = sys.stdin.readline()
    if t in s:
        cnt += 1
print(cnt)