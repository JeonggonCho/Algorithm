import sys

n = int(sys.stdin.readline())

score_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer_list = [0 for _ in range(n)]

for j in range(len(score_list[1])):
    num_list = []
    for k in range(n):
        num_list.append(score_list[k][j])
    for l in range(n):
        if num_list.count(num_list[l]) == 1:
            answer_list[l] += num_list[l]

print(*answer_list, sep='\n')