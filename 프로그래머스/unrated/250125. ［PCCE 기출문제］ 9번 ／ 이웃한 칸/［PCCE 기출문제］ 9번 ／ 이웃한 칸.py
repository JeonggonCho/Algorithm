def solution(board, h, w):
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    answer = 0
    target_color = board[h][w]
    length = len(board)
    
    for i in move:
        h_check = h + i[0]
        w_check = w + i[1]
        if 0 <= h_check < length and 0 <= w_check < length:
            moved_color = board[h_check][w_check]
            if moved_color == target_color:
                answer += 1
                
    return answer