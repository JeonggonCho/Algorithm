T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(f'#{i} -1')
    else:
        print(f'#{i} {a * b}')