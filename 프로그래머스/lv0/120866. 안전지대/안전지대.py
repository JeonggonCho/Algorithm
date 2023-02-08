def solution(board):
    answer = 0
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in dx:
                    for l in dy:
                        if 0 <= i+k <= (len(board)-1) and 0 <= j+l <= (len(board)-1) and board[i+k][j+l] != 1:
                            board[i+k][j+l] = 2
    for m in range(len(board)):
        for n in range(len(board)):
            if board[m][n] == 0:
                answer += 1
    return answer