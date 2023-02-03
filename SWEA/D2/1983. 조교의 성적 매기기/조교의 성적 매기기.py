T = int(input())

for i in range(1, T+1):
    score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    score_list = []
    
    n, k = map(int, input().split())

    for j in range(n):
        score_1, score_2, score_3 = map(int, input().split())
        score_list.append(score_1 * 0.35 + score_2 * 0.45 + score_3 * 0.2)

    # k번째 학생의 점수
    k_score = score_list[k-1]
    # 높은 점수부터 정렬
    sorted_score = sorted(score_list)[::-1]
    
    print(f'#{i}', end=' ')
    print(score[sorted_score.index(k_score)*10//n])