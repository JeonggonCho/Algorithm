T = int(input())

for i in range(1, T+1):
    n = int(input())
    number = [1]
    print(f'#{i}', *number, sep='\n')

    for j in range(n - 1):
        number.insert(0, 0)
        number.append(0)
        new_number = []

        for k in range(len(number) - 1):
            new_number.append(number[k] + number[k+1])
        print(*new_number)
        number = new_number