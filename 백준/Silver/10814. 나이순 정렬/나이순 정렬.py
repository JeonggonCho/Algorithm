import sys

N = int(sys.stdin.readline())

info_list = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    info_list.append((int(age), name))
sort_info = sorted(info_list, key = lambda x: x[0])
for j in sort_info:
    print(*j)