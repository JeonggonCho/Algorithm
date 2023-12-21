T = int(input())

for i in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))[::-1]

    li = []
    while prices:
        price = prices.pop()
        for j in range(len(prices)):
            if prices[j] == (price * (4 / 3)):
                prices.pop(j)
                li.append(str(price))
                break
    print(f'#{i} {" ".join(li)}')