T = int(input())

compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
center = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
surround = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for i in range(1, T + 1):
    sudoku = []
    check = True
    for j in range(9):
        numbers = list(map(int, input().split()))
        sudoku.append(numbers)
        
    for k in range(9):
        if sorted(sudoku[k]) != compare:
            print(f'#{i} 0')
            check = False
            break
        
        col = sorted([l[k] for l in sudoku])
        
        if col != compare:
            print(f'#{i} 0')
            check = False
            break
    else:
        for m in center:
            square = []
            square.append(sudoku[m[0]][m[1]])
            for n in surround:
                square.append(sudoku[m[0] + n[0]][m[1] + n[1]])
            if sorted(square) != compare:
                print(f'#{i} 0')
                check = False
                break
    
    if check == True:
        print(f'#{i} 1')