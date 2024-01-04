def start_setting(matrix, length):
    matrix[(length // 2) - 1][(length // 2)] = 1
    matrix[(length // 2)][(length // 2) - 1] = 1
    matrix[(length // 2) - 1][(length // 2) - 1] = 2
    matrix[(length // 2)][(length // 2)] = 2
    return matrix


def change_color(matrix, column, row, color):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
    if color == 1:
        for d in direction:
            li = []
            r = row
            c = column
            if 0 <= r + d[0] < len(matrix) and 0 <= c + d[1] < len(matrix[0]):
                if matrix[r + d[0]][c + d[1]] == 2:
                    while 0 <= r + d[0] < len(matrix) and 0 <= c + d[1] < len(matrix[0]):
                        if matrix[r + d[0]][c + d[1]] == 2:
                            li.append([r + d[0], c + d[1]])
                            r += d[0]
                            c += d[1]
                        elif matrix[r + d[0]][c + d[1]] == 1 and li:
                            for o in li:
                                matrix[o[0]][o[1]] = 1
                            break
                        elif matrix[r + d[0]][c + d[1]] == 0:
                            break
                        else:
                            break
    elif color == 2:
        for d in direction:
            li = []
            r = row
            c = column
            if 0 <= r + d[0] < len(matrix) and 0 <= c + d[1] < len(matrix[0]):
                if matrix[r + d[0]][c + d[1]] == 1:
                    while 0 <= r + d[0] < len(matrix) and 0 <= c + d[1] < len(matrix[0]):
                        if matrix[r + d[0]][c + d[1]] == 1:
                            li.append([r + d[0], c + d[1]])
                            r += d[0]
                            c += d[1]
                        elif matrix[r + d[0]][c + d[1]] == 2 and li:
                            for o in li:
                                matrix[o[0]][o[1]] = 2
                            break
                        elif matrix[r + d[0]][c + d[1]] == 0:
                            break
                        else:
                            break
    return matrix



T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board = start_setting(board, N)

    for l in range(M):
        column, row, color = map(int, input().split())
        row -= 1
        column -= 1
        board[row][column] = color
        board = change_color(board, column, row, color)

    black_cnt = 0
    white_cnt = 0
    for m in range(len(board)):
        for n in range(len(board[m])):
            if board[m][n] == 1:
                black_cnt += 1
            elif board[m][n] == 2:
                white_cnt += 1

    print(f'#{i} {black_cnt} {white_cnt}')