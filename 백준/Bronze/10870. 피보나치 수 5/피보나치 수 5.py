import sys

n = int(sys.stdin.readline())
cnt = 1
li = [0, 1]

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while cnt != n:
        li.append(li[-1] + li[-2])
        cnt += 1
    print(li[-1])