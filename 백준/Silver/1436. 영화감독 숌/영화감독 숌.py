import sys

n = int(sys.stdin.readline())

cnt = 0
num = 0

while cnt != n:
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)