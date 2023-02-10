def solution(dots):
    slope = []
    
    for i in range(0, 3):
        d1 = dots[i]
        for j in range(i+1, 4):
            d2 = dots[j]
            s = (d1[1] - d2[1]) / (d1[0] - d2[0])
            slope.append(s)
    if len(slope) != len(set(slope)):
        answer = 1
    else:
        answer = 0
    return answer