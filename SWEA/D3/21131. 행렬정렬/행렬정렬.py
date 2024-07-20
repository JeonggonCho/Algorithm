T = int(input())


def transpose(matrix, size):
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


answers = []
for _ in range(T):
    N = int(input())
    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    targetNum = N
    cnt = 0

    for i in range(N - 1, 0, -1):
        if matrix[0][i] != i + 1:
            matrix = transpose(matrix, i + 1)
            cnt += 1

    answers.append(cnt)

print('\n'.join(map(str, answers)))