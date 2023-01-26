import sys

K = int(sys.stdin.readline())
num_list = []

for i in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()
print(sum(num_list))