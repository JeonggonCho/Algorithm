import sys

score_list = []

for i in range(20):
    score_list.append(int(sys.stdin.readline()))

w_score_list = sorted(score_list[0:10])
k_score_list = sorted(score_list[10:20])

w_score = sum(w_score_list[-3:])
k_score = sum(k_score_list[-3:])

print(w_score, k_score)