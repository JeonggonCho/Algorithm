def solution(i, j, k):
    answer = 0
    for num1 in range(i, j+1):
        for num2 in str(num1):
            if int(num2) == k:
                answer += 1
    return answer