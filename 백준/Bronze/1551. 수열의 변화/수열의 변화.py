import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split(',')))

for i in range(k):
    numbers = []
    for j in range(1, len(num_list)):
        numbers.append(num_list[j] - num_list[j-1])
    num_list = numbers

print(*num_list, sep=',')