import sys

num_list = []

for i in range(5):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)
print(sum(num_list) // len(num_list))
print(sorted(num_list)[2])