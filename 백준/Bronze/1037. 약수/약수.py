import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

print(max(numbers) * min(numbers))