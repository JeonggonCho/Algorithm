import sys

N = int(sys.stdin.readline())
seat = sys.stdin.readline()

cup = '*'

for i in seat:
    if i == 'S':
        cup += 'S*'
    elif i == 'L' and cup[-1] != 'L':
        cup += 'L'
    elif i == 'L' and cup[-1] == 'L':
        cup += 'L*'

if cup.count('*') >= N:
    print(N)
else:
    print(cup.count('*'))