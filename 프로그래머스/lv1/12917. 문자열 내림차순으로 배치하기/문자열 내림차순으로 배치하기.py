def solution(s):
    answer = ''
    for i in sorted(list(s))[::-1]:
        answer += i
    return answer