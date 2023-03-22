import sys

n = int(sys.stdin.readline())
number_n = set(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
number_m = list(map(int, sys.stdin.readline().split()))
set_m = set(number_m)

numbers = number_n & set_m

for i in number_m:
    if i in numbers:
        print(1)
    else:
        print(0)