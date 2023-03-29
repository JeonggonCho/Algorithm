import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heappush(heap,(-x, x))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)