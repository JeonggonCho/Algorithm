import sys

S = int(sys.stdin.readline())

sum_value = 0
num = 0
cnt = 0

while sum_value < S:
    num += 1
    sum_value += num
    cnt += 1

if sum_value > S:
    cnt -= 1

print(cnt)
