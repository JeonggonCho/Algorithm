import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if len(heap) != 0:
            print(heappop(heap)[1])
        else:
            print('0')