import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

stack = []
numbers = deque(map(int, list(sys.stdin.readline().strip())))
cnt = 0

while cnt != K:
    if not numbers:
        break

    num = numbers.popleft()
    if not stack:
        stack.append(num)
    else:
        while stack and stack[-1] < num and cnt != K:
            stack.pop()
            cnt += 1
        stack.append(num)

while cnt < K:
    stack.pop()
    cnt += 1

if stack:
    front_numbers = ''.join(map(str, stack))
else:
    front_numbers = ''

if numbers:
    back_numbers = ''.join(map(str, numbers))
else:
    back_numbers = ''

answer = front_numbers + back_numbers
print(answer)
