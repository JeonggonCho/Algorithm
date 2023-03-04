T = int(input())

for i in range(1, T+1):
    n = int(input())
    if n < 3:
        print(f'#{i} 0')
    elif n >= 3:
        print(f'#{i} {n // 3}')