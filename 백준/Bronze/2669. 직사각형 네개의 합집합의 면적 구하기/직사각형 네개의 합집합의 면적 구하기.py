import sys

pt_list = []

for i in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for j in range(a, c):
        for k in range(b, d):
            pt_list.append((j, k))
print(len(set(pt_list)))