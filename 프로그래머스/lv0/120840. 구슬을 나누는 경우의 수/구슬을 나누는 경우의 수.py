def solution(balls, share):
    answer = 0
    num1 = 1
    num2 = 1
    num3 = 1
    for i in range(1, balls + 1):
        num1 *= i
    for j in range(1, balls - share + 1):
        num2 *= j
    for k in range(1, share + 1):
        num3 *= k
    answer = num1 / (num2 * num3)
    return answer