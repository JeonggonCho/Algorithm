import sys
from heapq import heapify, heappop

numbers = list(map(int, sys.stdin.readline().split()))
heapify(numbers)
for i in range(2):
    second_num = heappop(numbers)
print(second_num)