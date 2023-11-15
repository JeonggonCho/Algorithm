import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    cnt = 0
    k = 1

    while distance > 0:
        distance -= k
        cnt += 1
        if cnt % 2 == 0:
            k += 1

    print(cnt)