import sys

len_num = []

matrix = [list(sys.stdin.readline().strip()) for i in range(5)]

for j in matrix:
    len_num.append(len(j))
max_len = max(len_num)

for k in range(max_len):
    for l in range(5):
        try:
            print(matrix[l][k], end='')
        except:
            pass