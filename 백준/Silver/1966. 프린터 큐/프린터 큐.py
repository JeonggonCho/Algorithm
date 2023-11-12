import sys
from collections import deque

def check_greater_than_a(li, a):
    for num in li:
        if num > a:
            return True
    return False

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    li = deque([])

    for j in range(len(nums)):
        li.append((nums[j], j))

    sorted_li = []

    while True:
        tmp = li.popleft()
        importance = [k for (k, l) in li]
        if check_greater_than_a(importance, tmp[0]):
            li.append(tmp)
        else:
            sorted_li.append(tmp)
            if tmp[1] == M:
                break

    print(len(sorted_li))