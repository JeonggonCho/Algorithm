import sys
from heapq import heappush, heappop

heap = []
set_heap = []

N = int(sys.stdin.readline())

for i in range(N):
    char = sys.stdin.readline().strip()
    if (len(char), char) not in heap:
        heappush(heap, (len(char), char))

for k in range(len(heap)):
    print((heappop(heap))[1])