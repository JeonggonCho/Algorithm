def solution(n):
    answer = 0
    num = 1
    while num <= n:
        answer += 1
        num *= answer
    return (answer - 1)