import sys

x = int(sys.stdin.readline())

n = 1
sum_n = 1

while sum_n < x:
    n += 1
    sum_n += n

if sum_n == x:
    if n % 2 == 0:
        print(f'{n}/1')
    else:
        print(f'1/{n}')
else:
    if n % 2 == 0:
        print(f'{n - (sum_n - x)}/{1 + (sum_n - x)}')
    else:
        print(f'{1 + (sum_n - x)}/{n - (sum_n - x)}')