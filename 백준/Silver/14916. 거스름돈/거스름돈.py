import sys

n = int(sys.stdin.readline())

cnt = 0

if n >= 5:
    while n % 5 != 0:
        n -= 2
        cnt += 1
        if n < 0:
            print(-1)
            break
        elif n == 0:
            print(cnt)
            break
    else:
        cnt += n // 5
        print(cnt)

else:
    while n > 0:
        n -= 2
        cnt += 1
    if n == 0:
        print(cnt)
    else:
        print(-1)