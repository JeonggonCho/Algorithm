T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    for j in numbers:
        if j >= max_num:
            max_num = j
    print(f"#{i} {max_num}")