import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

if len(heap) == 1:
    print(0)
else:
    result = 0
    while len(heap) != 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        result += (num1 + num2)
        heapq.heappush(heap, (num1 + num2))
    print(result)