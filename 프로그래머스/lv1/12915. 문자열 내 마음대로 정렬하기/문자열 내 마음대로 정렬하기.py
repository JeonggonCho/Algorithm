def solution(strings, n):
    answer = []
    char = []
    for i in strings:
        char.append((i[n],i))
    char = sorted(char, key = lambda x:(x[0], x[1]))
    for j in char:
        answer.append(j[1])
    return answer