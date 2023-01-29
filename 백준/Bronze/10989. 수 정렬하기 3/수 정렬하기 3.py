import sys

numbers = {}

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num not in numbers:
        numbers[num] = 1
    else:
        numbers[num] += 1

for j in sorted(numbers):
    for k in range(numbers.get(j)):
        print(j)