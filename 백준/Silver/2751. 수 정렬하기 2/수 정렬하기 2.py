import sys
from heapq import heappush, heappop

numbers = []

N = int(sys.stdin.readline())

for i in range(N):
    heappush(numbers, int(sys.stdin.readline().strip()))

while len(numbers) > 0:
    print(heappop(numbers))