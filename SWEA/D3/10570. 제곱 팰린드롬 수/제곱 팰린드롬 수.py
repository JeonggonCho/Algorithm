T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    cnt = 0
    for j in range(a, b+1):
        if str(j) == str(j)[::-1] and (j ** (1/2)) == int(j ** (1/2)) and str(int(j ** (1/2))) == str(int(j ** (1/2)))[::-1]:
            cnt += 1
    print(f'#{i} {cnt}')