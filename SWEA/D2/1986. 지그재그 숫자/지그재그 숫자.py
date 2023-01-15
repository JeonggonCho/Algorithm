T = int(input())

for i in range(1, T+1):
    num = int(input())
    total = 0
    for j in range(1, num+1):
        if j % 2 == 1:
            total += j
        else:
            total -= j
    print(f'#{i} {total}')