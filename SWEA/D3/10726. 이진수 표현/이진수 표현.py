T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    for j in range(N):
        if M % 2 == 0:
            print(f'#{i} OFF')
            break
        M //= 2
    else:
        print(f'#{i} ON')