def solution(strlist):
    answer = []
    for i in strlist:
        num = 0
        for j in i:
            num += 1
        answer.append(num)
    return answer