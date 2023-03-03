import sys

n, l = map(int, sys.stdin.readline().split())

num_list = sorted(list(map(int, sys.stdin.readline().split())))

for i in num_list:
    if i <= l:
        l += 1
    else:
        break
print(l)