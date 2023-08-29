T = int(input())

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(1, T+1):
    money_result = []
    money = int(input())
    for j in money_list:
        if money // j != 0:
            money_result.append(money // j)
        else:
            money_result.append(0)
        money = money % j
    print(f'#{i}')
    print(*money_result)