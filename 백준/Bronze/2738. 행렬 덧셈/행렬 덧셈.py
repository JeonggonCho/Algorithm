import sys

n, m = map(int, sys.stdin.readline().split())

matrix_1 = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
matrix_2 = [list(map(int, sys.stdin.readline().split())) for j in range(n)]
result_matrix = [[0] * m for k in range(n)]

for l in range(n):
    for o in range(m):
        result_matrix[l][o] = matrix_1[l][o] + matrix_2[l][o]

for p in result_matrix:
    print(*p)