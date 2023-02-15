def solution(s):
    import math
    if len(s) % 2 == 0:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        answer = s[math.floor(len(s) // 2)]
    return answer