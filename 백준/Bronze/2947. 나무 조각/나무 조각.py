numbers = list(map(int, input().split()))

while True:
    a = 0
    b = 0
    for i in range(4):
        if numbers[a] > numbers[a+1]:
            b = numbers[a+1]
            numbers[a+1] = numbers[a]
            numbers[a] = b
            print(*numbers)
        a += 1
    if numbers == [1, 2, 3, 4, 5]:
        break