import math

T = int(input())
results = []

for i in range(1, T+1):
    score_sum = 0 # 점수 총 합 초기화
    N = int(input()) # 화살 개수 N
    for j in range(N):
        x, y = map(int, input().split()) # 화살이 떨어진 위치의 좌표 x, y
        r = math.ceil(math.sqrt(x * x + y * y) / 20)

        if r <= 0:
            score_sum += 10
        elif r <= 11:
            score = 11 - r
            score_sum += score

    results.append(f'#{i} {score_sum}')

for l in results:
    print(l)