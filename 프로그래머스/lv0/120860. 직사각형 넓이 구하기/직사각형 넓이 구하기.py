def solution(dots):
    answer = 0
    length = []
    for i in range(0, 3):
        d1 = dots[i]
        for j in range(i+1, 4):
            d2 = dots[j]
            if d1[0] == d2[0]:
                length.append(abs(d1[1] - d2[1]))
            if d1[1] == d2[1]:
                length.append(abs(d1[0] - d2[0]))
    length2 = list(set(length))
    if len(length2) == 1:
        answer = length2[0] ** 2
    else:
        answer = length2[0] * length2[1]
    return answer