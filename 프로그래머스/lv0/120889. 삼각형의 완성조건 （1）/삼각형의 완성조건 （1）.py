def solution(sides):
    if max(sides) < (sum(sides) - max(sides)):
        answer = 1
    else:
        answer = 2
    return answer