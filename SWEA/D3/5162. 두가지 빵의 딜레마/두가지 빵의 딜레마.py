T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    print(f'#{i} {int(c / min(a,b))}')