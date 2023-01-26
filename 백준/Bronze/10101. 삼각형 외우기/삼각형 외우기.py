import sys

angle_list = []
stack = []

for i in range(3):
    angle_list.append(int(sys.stdin.readline()))

if sum(angle_list) == 180:
    for j in angle_list:
        if j not in stack:
            stack.append(j)
    if len(stack) == 1:
        print('Equilateral')
    elif len(stack) == 2:
        print('Isosceles')
    elif len(stack) == 3:
        print('Scalene')
else:
    print('Error')