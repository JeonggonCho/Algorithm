def solution(s):
    answer = []
    n = 0 # 0의 개수
    m = 0 # 이진변환 횟수
    while s != '1':
        n += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        m += 1
    answer.append(m)
    answer.append(n)
    return answer