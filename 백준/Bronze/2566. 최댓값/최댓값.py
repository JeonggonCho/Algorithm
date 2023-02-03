import sys

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
max_value = matrix[0][0]
max_x = 0
max_y = 0

for j in range(9):
    for k in range(9):
        if max_value < matrix[j][k]:
            max_value = matrix[j][k]
            max_x = j
            max_y = k

print(max_value)
print(max_x+1, max_y+1)