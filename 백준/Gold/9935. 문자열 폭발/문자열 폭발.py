import sys

char = list(sys.stdin.readline().strip())
bomb = sys.stdin.readline().strip()

stack = []

for i in char:
    stack.append(i)
    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        # 폭발 문자열이 발견되면 스택에서 제거
        del stack[-len(bomb):]

result = ''.join(stack)

if result:
    print(result)
else:
    print("FRULA")