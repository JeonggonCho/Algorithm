import sys
from collections import deque

def ripen(m, n, d, matrix, queue):
    check = False
    new_queue = deque()
    while queue:
        j, k = queue.popleft()
        for l in d:
            ni, nj = j + l[0], k + l[1]
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == 0:
                matrix[ni][nj] = 1
                new_queue.append((ni, nj))
                check = True
    return check, new_queue

def all_ripen(m, n, matrix):
    for row in matrix:
        if 0 in row:
            return False
    return True

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

today_tomato = matrix[:]
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
cnt = 0

queue = deque([(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 1])

while queue:
    result, queue = ripen(m, n, d, today_tomato, queue)
    if result:
        cnt += 1

if all_ripen(m, n, today_tomato):
    print(cnt)
else:
    print(-1)
