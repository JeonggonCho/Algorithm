import sys

number = sys.stdin.readline().strip()
length = len(number)
answer = 0
num1 = '1'
for i in range(1, length):
    num1 += '0'
    num2 = '9'
    for j in range(i-1):
        num2 += '0'
    answer += int(num2) * i

answer += (int(number) - int(num1) + 1) * length

print(answer)