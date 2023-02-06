T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for j in range(n)]
    result = 0

    for l in range(n):
        cnt = 0
        for m in range(n):
            if matrix[l][m] == 1:
                cnt += 1
            elif matrix[l][m] == 0:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    for l in range(n):
        cnt = 0
        for m in range(n):
            if matrix[m][l] == 1:
                cnt += 1
            elif matrix[m][l] == 0:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    print(f'#{i} {result}')