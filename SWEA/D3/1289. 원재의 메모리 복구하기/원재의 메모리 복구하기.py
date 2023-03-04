T = int(input())

for i in range(1, T+1):
    numbers = str(int(input()))
    if len(numbers) == 0:
        print(f'#{i} 0')
    else:
        cnt = 1
        for j in range(1, len(numbers)):
            if numbers[j] != numbers[j-1]:
                cnt += 1
        print(f'#{i} {cnt}')