def solution(n):
    num = 0
    while True:
        num += 1
        if num ** 2 == n:
            answer = 1
            break
        elif num ** 2 > n:
            answer = 2
            break
    return answer