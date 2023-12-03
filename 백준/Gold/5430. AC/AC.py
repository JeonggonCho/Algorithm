import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    P = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    li_input = sys.stdin.readline().strip().strip("[]")
    li = deque(map(int, li_input.split(','))) if li_input else deque()
    check = True

    for j in P:
        if j == "R":
            if check == True:
                check = False
            else:
                check = True
        elif j == "D":
            if len(li) == 0:
                print("error")
                break
            elif check == True:
                li.popleft()
            elif check == False:
                li.pop()
    else:
        if check == True:
            print("[" + ",".join(map(str, li)) + "]")
        else:
            print("[" + ",".join(map(str, reversed(li))) + "]")