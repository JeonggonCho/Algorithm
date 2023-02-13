import sys

n = int(sys.stdin.readline())
num = 1
cnt =0

for i in range(1, n+1):
    num *= i
for j in reversed(str(num)):
    if j == '0':
        cnt += 1
    else:
        break
print(cnt)