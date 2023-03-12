T = int(input())

for i in range(1, T+1):
    score = input()
    if 15 - (len(score)) + score.count('o') >= 8:
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')