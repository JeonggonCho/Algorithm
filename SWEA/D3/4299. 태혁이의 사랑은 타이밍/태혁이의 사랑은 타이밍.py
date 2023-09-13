T = int(input())

for i in range(1, T+1):

    D, H, M = map(int, input().split())
    result = 0
    result += (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)

    if result < 0 :
        result = -1

    print(f"#{i} {result}")