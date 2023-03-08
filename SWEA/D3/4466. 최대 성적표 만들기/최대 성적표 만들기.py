T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    score_list = list(map(int, input().split()))
    choice = sorted(score_list, reverse=True)[:b]
    print(f'#{i} {sum(choice)}')