T = int(input())

for i in range(1, T+1):
    stack = []
    chars = sorted(list(input()))
    length = len(chars)

    for j in range(length):
        char = chars.pop()
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        elif stack[-1] != char:
            stack.append(char)

    if len(stack) == 0:
        print(f'#{i} Good')
    else:
        print(f'#{i} {"".join(stack[::-1])}')