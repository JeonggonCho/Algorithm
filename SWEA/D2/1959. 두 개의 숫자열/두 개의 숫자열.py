T = int(input())

for i in range(1, T + 1):
    total = []
    a, b = map(int, input().split())
    numbers_1 = list(map(int, input().split()))
    numbers_2 = list(map(int, input().split()))

    if len(numbers_1) >= len(numbers_2):
        arr_long = numbers_1
        arr_short = numbers_2
    else:
        arr_long = numbers_2
        arr_short = numbers_1

    for j in range(len(arr_long) - len(arr_short) + 1):
        num = 0
        for k in range(len(arr_short)):
            num += arr_long[k + j] * arr_short[k]
        total.append(num)

    print(f'#{i} {max(total)}')