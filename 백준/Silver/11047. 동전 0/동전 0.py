import sys

n, k = map(int, sys.stdin.readline().split())

li = []
for i in range(n):
    money_unit = int(sys.stdin.readline())
    li.append(money_unit)

answer = 0
while k != 0:
    money = li.pop()
    if k >= money:
        answer += k // money
        k %= money

print(answer)