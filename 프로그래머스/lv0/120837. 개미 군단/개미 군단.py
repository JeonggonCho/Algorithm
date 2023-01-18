def solution(hp):
    answer = 0
    answer += hp // 5
    answer += (hp % 5) // 3
    answer += (hp % 5) % 3
    return answer