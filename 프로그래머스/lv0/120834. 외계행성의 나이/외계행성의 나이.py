def solution(age):
    answer = ''
    alpha_num = {}
    for i in range(97, 123):
        alpha_num[i-97] = chr(i)
    for j in str(age):
        answer += alpha_num[int(j)]
    return answer