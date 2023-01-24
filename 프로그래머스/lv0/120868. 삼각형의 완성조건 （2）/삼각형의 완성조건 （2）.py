def solution(sides):
    answer = 0
    answer += max(sides) - ((sorted(sides))[1] - (sorted(sides))[0] + 1) + 1
    answer += (sum(sides) - 1) - (max(sides) + 1) + 1
    return answer