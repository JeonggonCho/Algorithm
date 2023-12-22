T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    num1 = abs((a + c) / 2 - b)
    num2 = abs(b + (b - a) - c)
    num3 = abs(b - (c - b) - a)
    print(f'#{i} {min(num1, num2, num3)}')