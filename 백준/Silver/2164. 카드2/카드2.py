from collections import deque
import sys

num_list = deque([i for i in range(1, int(sys.stdin.readline()) + 1)])

while len(num_list) != 1:
    num_list.popleft()
    num_list.append(num_list.popleft())
print(*num_list)