T = int(input())

for i in range(1, T+1):
    k = int(input()) - 1
    n = 0

    while k >= 0:
        if k % 2 == 1:
            k = (k - 1) // 2
        if k % 4 == 0:
            n = 0
            break
        elif k % 2 == 0:
            n = 1
            break

    print(f'#{i} {n}')