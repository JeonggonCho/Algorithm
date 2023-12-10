import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

result = [0]
stack = [(heights[0], 0)]  # 스택에는 (높이, 인덱스)를 저장

for i in range(1, len(heights)):
    now_height = heights[i]

    while stack and stack[-1][0] <= now_height:
        stack.pop()

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1] + 1)

    stack.append((now_height, i))

print(*result)
