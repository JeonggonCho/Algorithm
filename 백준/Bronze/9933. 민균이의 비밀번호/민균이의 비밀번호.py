import sys

N = int(sys.stdin.readline())

password = [sys.stdin.readline().strip() for i in range(N)]

for j in password:
    if j[::-1] in password:
        a = len(j)
        b = j[a//2]
        print(a, b)
        break