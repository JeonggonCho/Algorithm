def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    a = max(n, m)
    while True:
        if a % n == 0 and a % m == 0:
            answer.append(a)
            break
        else:
            a += 1
    return answer