T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for j in range(n)]
    numbers = []

    for k in range(n-m+1):
        for l in range(n-m+1):
            cnt = 0
            for o in range(m):
                for p in range(m):
                    cnt += matrix[k+o][l+p]
                numbers.append(cnt)
    
    print(f'#{i} {max(numbers)}')