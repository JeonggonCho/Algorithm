import sys

N = int(sys.stdin.readline())

result = 0

while N >= 3:
    if N % 5 == 0:
        result += N // 5
        N %= 5
    else:
        N -= 3
        result += 1

if N == 0:
    print(result)
else:
    print(-1)