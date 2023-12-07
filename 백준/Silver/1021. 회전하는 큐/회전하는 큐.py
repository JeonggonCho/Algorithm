import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
cnt = 0

queue = deque([i for i in range(1, N+1)])
for j in targets:
    while queue[0] != j:
        if len(queue) % 2 == 0: # 전체 요소 개수가 짝수일 경우,
            if queue.index(j) < (len(queue) - 1) / 2: # 찾고자 하는 요소가 전체 요소의 중앙보다 앞쪽에 있을 때,
                num = queue.popleft()
                queue.append(num)
                cnt += 1
            else: # 찾고자 하는 요소가 전체 요소의 중앙보다 뒤쪽에 있을 때,
                num = queue.pop()
                queue.appendleft(num)
                cnt += 1
        else: # 전체 요소 개수가 홀수일 경우,
            if queue.index(j) <= (len(queue) - 1) // 2: # 찾고자 하는 요소가 중앙을 포함하여 앞쪽에 있을 때,
                num = queue.popleft()
                queue.append(num)
                cnt += 1
            else: # 찾고자 하는 요소가 중앙보다 뒤쪽에 있을 때,
                num = queue.pop()
                queue.appendleft(num)
                cnt += 1

    queue.popleft() # 맨 앞으로 찾고자 하는 요소가 위치한 경우, 빼내기

print(cnt)