T = int(input())

for i in range(1, T+1):
    num = int(input())
    value = 0
    for j in range(num):
        num1, num2 = map(float, input().split())
        value += num1 * num2
        result = round(value, 6)
    print(f'#{i} {result}')