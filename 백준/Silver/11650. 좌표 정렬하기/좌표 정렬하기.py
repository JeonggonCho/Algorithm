import sys

pt_list = []

N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pt_list.append((a, b))
for j in sorted(pt_list, key = lambda x: (x[0], x[1])):
    print(*j)