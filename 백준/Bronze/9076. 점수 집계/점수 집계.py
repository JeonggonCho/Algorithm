import sys

T = int(sys.stdin.readline())

for i in range(T):
    score_list = list(map(int, sys.stdin.readline().split()))

    sorted_score = sorted(score_list)
    if sorted_score[3] - sorted_score[1] >= 4:
        print('KIN')
    else:
        print(sum(sorted_score[1:4]))