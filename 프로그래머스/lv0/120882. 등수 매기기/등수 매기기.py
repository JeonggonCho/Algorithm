def solution(score):
    answer = []
    mean_list = []
    for i in score:
        mean = (i[0] + i[1]) / 2
        mean_list.append(mean)
    for j in mean_list:
        rank = 1
        for k in mean_list:
            if j < k:
                rank += 1
        answer.append(rank)
    return answer