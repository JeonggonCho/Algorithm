import sys

people_num = 0
numbers = []

for i in range(4):
    e_num, i_num = map(int, sys.stdin.readline().split())
    people_num -= e_num
    numbers.append(people_num)
    people_num += i_num
    numbers.append(people_num)

print(max(numbers))