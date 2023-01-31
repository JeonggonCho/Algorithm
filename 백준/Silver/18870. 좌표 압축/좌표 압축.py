import sys

dict = {}

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

set_numbers = sorted(list(set(numbers)))

dict = {set_numbers[i]:i for i in range(len(set_numbers))} 
for j in numbers:
    print(dict[j], end=' ')