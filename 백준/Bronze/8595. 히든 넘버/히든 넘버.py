import sys

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = 0
num = ''

n = int(sys.stdin.readline())

chars = sys.stdin.readline()

for i in chars:
    if len(num) > 6:
        print(0)
        break
    elif i in numbers:
        num += i
    elif i not in numbers and len(num) != 0:
        answer += int(num)
        num = ''
else:
    print(answer)