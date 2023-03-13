from collections import deque
import sys

n = int(sys.stdin.readline())

num_list = deque([])

for i in range(n):
    char = sys.stdin.readline().split()
    if char[0] == 'push':
        num_list.append(char[1])
    elif char[0] == 'pop':
        if num_list:
            print(num_list.popleft())
        else:
            print(-1)
    elif char[0] == 'size':
        print(len(num_list))
    elif char[0] == 'empty':
        if num_list:
            print(0)
        else:
            print(1)
    elif char[0] == 'front':
        if num_list:
            print(num_list[0])
        else:
            print(-1)
    elif char[0] == 'back':
        if num_list:
            print(num_list[-1])
        else:
            print(-1)