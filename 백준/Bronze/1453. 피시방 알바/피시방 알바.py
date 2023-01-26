import sys
from collections import deque

queue = []
ban = []

N = int(sys.stdin.readline())
seat_list = deque(map(int, sys.stdin.readline().split()))
while len(seat_list) > 0:
    if seat_list[0] not in queue:
        queue.append(seat_list.popleft())
    else:
        ban.append(seat_list.popleft())
print(len(ban))