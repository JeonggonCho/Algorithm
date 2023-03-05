T = int(input())

for i in range(1, T+1):
    new_score = []
    score_list = list(map(int, input().split()))
    for j in score_list:
        if j < 40:
            new_score.append(40)
        else:
            new_score.append(j)
    print(f'#{i} {sum(new_score) // len(new_score)}')