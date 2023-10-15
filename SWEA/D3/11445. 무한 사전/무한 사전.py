T = int(input())

for i in range(1, T + 1) :
    p = input().strip()
    q = input().strip()

    if p + "a" != q :
        print(f'#{i} Y')
    else :
        print(f'#{i} N')