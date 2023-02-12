import sys

height = []

for i in range(9):
    height.append(int(sys.stdin.readline().strip()))

for j in range(8):
    for k in range(j+1, 9):
        if sum(height) - height[j] - height [k] == 100:
            n1 = j
            n2 = k
for l in sorted(height):
    if l != height[n1] and l != height[n2]:
        print(l)