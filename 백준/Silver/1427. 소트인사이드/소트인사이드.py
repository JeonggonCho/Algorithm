import sys

num_list = []

numbers = sys.stdin.readline().strip()

for i in numbers:
    num_list.append(int(i))

sort_num = sorted(num_list, reverse = True)

for j in sort_num:
    print(j, end = '')