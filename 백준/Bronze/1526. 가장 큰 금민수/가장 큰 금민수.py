import sys

n = int(sys.stdin.readline())

while True:
    for i in str(n):
        if i != '4' and i != '7':
            break
    else:
        print(n)
        break
    n -= 1