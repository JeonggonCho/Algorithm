import sys

day = []
num = 0

n = int(sys.stdin.readline())

num_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in num_list:
    day.append(i + num)
    num += 1

print(max(day) + 2)