def solution(num, total):
    answer = []
    sum_value = 0
    
    for i in range(0, num):
        sum_value += i
    value = (total - sum_value) / num
    
    for j in range(num):
        answer.append(value)
        value += 1
        
    return answer