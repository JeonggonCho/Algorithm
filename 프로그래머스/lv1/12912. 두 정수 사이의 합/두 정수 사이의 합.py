def solution(a, b):
    answer = 0
    min_num = min(a, b)
    max_num = max(a, b)
    while min_num != max_num+1:
        answer += min_num
        min_num += 1
    return answer