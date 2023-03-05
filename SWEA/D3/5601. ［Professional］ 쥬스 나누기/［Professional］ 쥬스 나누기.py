T = int(input())

for i in range(1, T+1):
    n = int(input())
    print(f'#{i}', end='')
    for j in range(n):
        print(f' 1/{n}',end='')
    print()