def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(sorted_emergency.index(i)+1)
    return answer