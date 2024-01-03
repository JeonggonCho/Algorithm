import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
    score = int(sys.stdin.readline())
    li.append(score)

answer = 0
bigger_score = li.pop()
while li:
    now_score = li.pop()
    while now_score >= bigger_score:
        now_score -= 1
        answer += 1
    bigger_score = now_score


print(answer)