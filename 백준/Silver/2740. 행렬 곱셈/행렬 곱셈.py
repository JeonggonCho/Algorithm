import sys

def matrix_multiply(matrix1, matrix2):
    length1 = len(matrix1[0])
    length2 = len(matrix2[0])
    results = []
    for m in matrix1:
        result = []
        for n in range(length2):
            li = []
            for o in matrix2:
                li.append(o[n])
            multiple_num = 0
            for p in range(length1):
                multiple_num += m[p] * li[p]
            result.append(multiple_num)
        results.append(result)
    return results

matrix1 = []
matrix2 = []

N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    row1 = list(map(int, sys.stdin.readline().split()))
    matrix1.append(row1)

M, K = map(int, sys.stdin.readline().split())
for j in range(M):
    row2 = list(map(int, sys.stdin.readline().split()))
    matrix2.append(row2)

answer = matrix_multiply(matrix1, matrix2)

for k in answer:
    print(' '.join(map(str, k)))