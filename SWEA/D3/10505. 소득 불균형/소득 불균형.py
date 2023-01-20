T = int(input())

for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    for j in numbers:
        if j <= sum(numbers) / N:
            cnt += 1
            
    print(f'#{i} {cnt}')