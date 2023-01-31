import sys

N= int(sys.stdin.readline())

matrix = []
for i in range(N):
    matrix.append([' '] * N)

for j in range(N):
    for k in range(j+1):
        matrix[k][j] = '*'

for l in range(N):
    for m in range(N):
        print(matrix[l][m], end='')
    print()