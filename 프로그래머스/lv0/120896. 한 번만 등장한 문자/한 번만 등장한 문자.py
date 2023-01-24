def solution(s):
    answer = ''
    char = ''
    for i in s:
        if s.count(i) == 1:
            char += i
    for j in sorted(char):
        answer += j
    return answer