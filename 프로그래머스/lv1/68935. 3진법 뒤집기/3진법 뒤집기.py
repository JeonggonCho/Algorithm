def solution(n):
    answer = 0
    n_3 = ''
    while n >= 3:
        n_3 += str(n % 3)
        n = n // 3
    n_3 += str(n)
    a = 1
    for i in n_3[::-1]:
        answer += int(i) * a
        a *=  3
    return answer