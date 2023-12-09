import sys
from collections import deque

char = deque(sys.stdin.readline().strip())

li = []
while char:
    if char[0] == "(" and char[1] == ")":
        li.append("l")
        char.popleft()
        char.popleft()
    else:
        li.append(char.popleft())

result = 0
temp = 0
for i in range(len(li)):
    if li[i] == "(":
        temp += 1
    elif li[i] == ")":
        temp -= 1
        result += 1
    elif li[i] == "l":
        result += temp

print(result)