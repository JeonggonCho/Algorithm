T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    num = (A // B) ** 2
    print(f'#{i} {num}')