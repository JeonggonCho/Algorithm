def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) != 0:
            stack.pop()
        else:
            answer = False
            break
    else:
        if len(stack) == 0:
            answer = True
        else:
            answer = False
    return answer