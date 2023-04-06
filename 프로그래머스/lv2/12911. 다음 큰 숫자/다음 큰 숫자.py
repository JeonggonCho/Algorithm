def solution(n):
    a = bin(n)[2:].count('1')
    while True:
        n += 1
        b = bin(n)[2:].count('1')
        if a == b:
            answer = n
            break
    return answer