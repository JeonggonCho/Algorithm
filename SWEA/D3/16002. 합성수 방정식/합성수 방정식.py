import math


def is_composite(num):
    for j in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % j == 0:
            return True


T = int(input())

for i in range(1, T + 1):
    N = int(input())
    num = 4
    check = False
    while True:
        if is_composite(num):
            compare_num = num + N
            if is_composite(compare_num):
                print(f'#{i} {compare_num} {num}')
                check = True
                break
            else:
                num += 1
            if check == True:
                break
        else:
            num += 1
        if check == True:
            break