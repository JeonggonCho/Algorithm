def solution(n):
    answer = 0
    cnt = 0
    
    while True:
        cnt += 1
        num = n * cnt
        if num % 6 == 0:
            answer = num // 6
            break
        
    return answer