import sys

N = int(sys.stdin.readline())

cnt = 0
range = 1

while N > range:
    cnt += 1
    range += cnt * 6
print(cnt + 1)