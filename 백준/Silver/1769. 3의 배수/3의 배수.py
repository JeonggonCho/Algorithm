import sys

cnt = 0
num_list = ['3', '6', '9']

num = sys.stdin.readline().strip()

while len(num) != 1:
    cnt += 1
    total = 0
    for i in num:
        total += int(i)
    num = str(total)

print(cnt)

if num in num_list:
    print('YES')
else:
    print('NO')