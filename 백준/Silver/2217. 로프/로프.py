import sys

N = int(sys.stdin.readline())
ropes = []

for i in range(N):
    rope = int(sys.stdin.readline())
    ropes.append(rope)
ropes.sort(reverse=True)

max_weight = 0
for j in range(len(ropes)):
    weight = (j + 1) * ropes[j]
    if max_weight < weight:
        max_weight = weight

print(max_weight)