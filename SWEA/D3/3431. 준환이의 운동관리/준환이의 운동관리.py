T = int(input())

for i in range(1, T+1):
    l, u, x = map(int, input().split())
    if x < l:
        print(f'#{i} {l - x}')
    elif x >= l and x <= u:
        print(f'#{i} 0')
    elif x > u:
        print(f'#{i} -1')