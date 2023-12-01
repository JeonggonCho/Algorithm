import sys

N, M = map(int, sys.stdin.readline().split())
package_prices = []
piece_prices = []

for i in range(M):
    package_price, piece_price = map(int, sys.stdin.readline().split())
    package_prices.append(package_price)
    piece_prices.append(piece_price)

min_package_price = min(package_prices)
min_piece_price = min(piece_prices)

result = 0

# 최소 패키지 가격과 최소 조각 가격을 이용하여 최소 비용 계산
while N >= 6:
    if min_package_price < min_piece_price * 6:
        result += min_package_price
    else:
        result += min_piece_price * 6
    N -= 6

# 남은 조각을 살 때
if min_package_price < min_piece_price * N:
    result += min_package_price
else:
    result += min_piece_price * N

print(result)