def solution(n):
    num_list = []
    answer = ''
    for i in str(n):
        num_list.append(int(i))
    for j in sorted(num_list, reverse=True):
        answer += str(j)
    answer = int(answer)        
    return answer