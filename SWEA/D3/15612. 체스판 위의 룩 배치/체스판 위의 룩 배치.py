def attack(li):
    cnt_rook = 0
    for _ in li:
        if 'O' in _:
            cnt_rook += _.count('O')
            if _.count('O') > 1 or _.count('O') == 0:
                return 'no'
    if cnt_rook != 8:
        return 'no'

    row_numbers = []
    column_numbers = []
    for k in range(len(li)):
        for l in range(len(li[k])):
            if li[k][l] == 'O':
                if (k in row_numbers) or (l in column_numbers):
                    return 'no'
                else:
                    row_numbers.append(k)
                    column_numbers.append(l)
    return 'yes'


T = int(input())

for i in range(1, T+1):
    chess_board = []
    cnt_rook = 0
    check = True
    for j in range(8):
        row = list(input().strip())
        chess_board.append(row)
    answer = attack(chess_board)

    print(f'#{i} {answer}')
