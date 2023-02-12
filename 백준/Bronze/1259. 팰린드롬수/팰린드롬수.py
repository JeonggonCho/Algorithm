import sys

while True:
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')