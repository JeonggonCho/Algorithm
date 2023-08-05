def solution(n, m, section):
    answer = 0
    painted = section[0] - 1
    for i in section:
        if i > painted:
            painted = i + m - 1
            answer += 1
    return answer