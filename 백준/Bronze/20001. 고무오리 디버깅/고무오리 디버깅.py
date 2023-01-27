import sys

stack = []
chars = sys.stdin.readline()

while True:
    order = sys.stdin.readline().strip()
    if order == '문제':
        stack.append('a')
    elif order == '고무오리':
        if len(stack) != 0:
            stack.pop()
        else:
            stack.append('a')
            stack.append('a')
    elif order == '고무오리 디버깅 끝':
        break

if len(stack) != 0:
    print('힝구') 
else:
    print('고무오리야 사랑해')