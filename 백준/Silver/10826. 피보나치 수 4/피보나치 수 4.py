import sys
from collections import deque

sequence = deque([0, 1])

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    for i in range(n-1):
        sequence.append(sum(sequence))
        sequence.popleft()
    print(sequence.pop())