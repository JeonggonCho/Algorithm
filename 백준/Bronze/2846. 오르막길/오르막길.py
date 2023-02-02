import sys

height_gap = []
up = []
cnt_up = 0

N = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    height_gap.append(height[i] - height[i-1])

for j in height_gap:
    if j > 0:
        cnt_up += j
    else:
        up.append(cnt_up)
        cnt_up = 0
else:
    up.append(cnt_up)

if sum(up) == 0:
    print(0)
else:
    print(max(up))