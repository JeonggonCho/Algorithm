def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if int(j) == 7:
                answer += 1
    return answer