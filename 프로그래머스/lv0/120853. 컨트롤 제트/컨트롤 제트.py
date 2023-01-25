def solution(s):
    answer = 0
    a = s.split()
    for i in range(len(a) - 1):
        if a[i+1] != 'Z' and a[i] != 'Z':
            answer += int(a[i])
    if a[len(a) - 1] != 'Z':
        answer += int(a[len(a) - 1])
    return answer