def solution(my_str, n):
    answer = []
    cnt = 0
    char = ''
    for i in my_str:
        cnt += 1
        char += i
        if cnt == n:
            answer.append(char)
            cnt = 0
            char = ''
    if char != '':
        answer.append(char)
    return answer