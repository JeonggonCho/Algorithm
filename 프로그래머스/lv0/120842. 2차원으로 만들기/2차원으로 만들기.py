def solution(num_list, n):
    answer = []
    num = []
    for i in num_list:
        num.append(i)
        if len(num) == n:
            answer.append(num)
            num =[]
    return answer