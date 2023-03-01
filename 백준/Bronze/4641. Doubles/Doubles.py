import sys

while True:
    answer = 0
    numbers = list(map(int, sys.stdin.readline().split()))
    if -1 in numbers:
        break
    for i in numbers[:-1]:
        if i * 2 in numbers[:-1]:
            answer += 1
    print(answer)