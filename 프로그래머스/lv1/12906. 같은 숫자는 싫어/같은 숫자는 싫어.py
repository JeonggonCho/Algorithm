def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or i != answer[-1]:
            answer.append(i)
    return answer