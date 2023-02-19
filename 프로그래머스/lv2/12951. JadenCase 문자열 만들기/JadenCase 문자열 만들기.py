def solution(s):
    from collections import deque
    answer = ''
    s = deque(s)
    while s:
        a = s.popleft()
        if answer:
            if answer[-1] == ' ':
                answer += a.upper()
            else:
                answer += a.lower()
        else:
            answer += a.upper()
    return answer