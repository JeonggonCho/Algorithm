def solution(chicken):
    answer = 0
    card = chicken
    while card >= 10:
        answer += card // 10
        card = card // 10 + card % 10
    return answer