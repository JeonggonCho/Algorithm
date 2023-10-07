T = int(input())
result = []

for i in range(1, T+1):
    A, B, C, D = map(int, input().split())
    Alice_win_rate = A / B
    Bob_win_rate = C / D
    if Alice_win_rate > Bob_win_rate:
        result.append(f'#{i} ALICE')
    elif Bob_win_rate > Alice_win_rate:
        result.append(f'#{i} BOB')
    else:
        result.append(f'#{i} DRAW')
for j in result:
    print(j)