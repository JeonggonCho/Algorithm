import sys

time = 0

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

for i in sorted(numbers):
    time += (i * n)
    n -= 1
print(time) 