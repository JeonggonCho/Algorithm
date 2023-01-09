import sys

N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

min = numbers[0]
max = numbers[0]

for i in numbers:
    if max <= i:
        max = i
    elif min >= i:
        min = i
print(min, max)