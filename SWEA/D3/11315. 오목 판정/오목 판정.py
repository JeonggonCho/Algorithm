def row_check(matrix, check):
    for k in matrix:
        if check in ''.join(k):
            return True
    return False


def column_check(matrix, check):
    for l in range(len(matrix)):
        column_line = []
        for m in matrix:
            column_line.append(m[l])
        if check in ''.join(column_line):
            return True
    return False


def diagonal_check(matrix, check):
    for n in range(N - 4):
        a, b = 0, n
        diagonal_line = []
        for o in range(N - n):
            if a < N and b < N:
                diagonal_line.append(matrix[a][b])
            a += 1
            b += 1
        if check in ''.join(diagonal_line):
            return True

        a, b = n, 0
        diagonal_line = []
        for p in range(N - n):
            if a < N and b < N:
                diagonal_line.append(matrix[a][b])
            a += 1
            b += 1
        if check in ''.join(diagonal_line):
            return True

    for q in range(4, N):
        a, b = 0, q
        diagonal_line = []
        for r in range(q + 1):
            if a < N and b < N:
                diagonal_line.append(matrix[a][b])
            a += 1
            b -= 1
        if check in ''.join(diagonal_line):
            return True

        a, b = N - q - 1, N - 1
        diagonal_line = []
        for s in range(q + 1):
            if a < N and b < N:
                diagonal_line.append(matrix[a][b])
            a += 1
            b -= 1
        if check in ''.join(diagonal_line):
            return True
    return False


T = int(input())
check = 'ooooo'

for i in range(1, T+1):
    N = int(input())
    matrix = []

    for j in range(N):
        row = list(input())
        matrix.append(row)

    if row_check(matrix, check) or column_check(matrix, check) or diagonal_check(matrix, check):
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')