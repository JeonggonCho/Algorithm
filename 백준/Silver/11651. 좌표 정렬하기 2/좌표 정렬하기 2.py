import sys

N = int(sys.stdin.readline())

pt_list = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pt_list.append((a, b))
for j in sorted(pt_list, key = lambda x: (x[1], x[0])):
    print(*j)