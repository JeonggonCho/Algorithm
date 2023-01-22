def solution(n):
    answer = 0
    num = 1
    while True:
        answer += 1
        num *= answer
        if num > n:
            break
    return (answer - 1)