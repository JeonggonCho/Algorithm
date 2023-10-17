T = int(input())
results = []

for i in range(1, T+1):
    N, PD, PG = map(int, input().split())

    if PD != 0 and PG == 0:
        results.append(f'#{i} Broken')
    elif PD != 100 and PG == 100:
        results.append(f'#{i} Broken')
    else:
        check = 0
        for j in range(1, N+1):
            if (j * PD) / 100 == (j * PD) // 100:
                check = 1
                break
        if check == 1:
            results.append(f'#{i} Possible')
        else:
            results.append(f'#{i} Broken')

for k in results:
    print(k)