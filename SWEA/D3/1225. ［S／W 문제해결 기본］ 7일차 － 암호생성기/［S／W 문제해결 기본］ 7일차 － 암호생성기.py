from collections import deque

T = 10

for i in range(1, T+1):
    test_num = int(input())
    numbers = deque(list(map(int, input().split())))

    while True:
        for j in range(1,6):
            num = numbers.popleft()-j
            if num > 0:
                numbers.append(num)
            else:
                numbers.append(0)
                break
        if num <= 0:
                break
    print(f'#{i}', end=' ')
    print(*numbers)