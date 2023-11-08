import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if [a, b, c] == [0, 0, 0]:
        break
    else:
        max_length = 0
        small_length = 0
        for i in [a, b, c]:
            if i == max([a, b, c]):
                max_length = i ** 2
            else:
                small_length += i ** 2
        if max_length == small_length:
            print('right')
        else:
            print('wrong')