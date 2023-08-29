T = int(input())

for i in range(1, T + 1):
    num = int(input())
    for j in range(1, 10):
        if num % j == 0 and (num // j) >= 1 and (num // j) <= 9:
            print(f'#{i} Yes')
            break
    else:
        print(f'#{i} No')