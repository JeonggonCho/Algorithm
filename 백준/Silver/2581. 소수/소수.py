import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

num_list = []

for i in range(a, b+1):
    num = []
    for j in range(1, i+1):
        if i % j == 0:
            num.append(j)
    if sum(num) == i + 1:
        num_list.append(i)

if num_list:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)