directions = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}

T = int(input())

for i in range(1, T+1):
    H, W = map(int, input().split())

    matrix = []
    for j in range(H):
        row_input = list(input())
        if '^' in row_input:
            position = [j, row_input.index('^')]
            direct = 'U'
        elif 'v' in row_input:
            position = [j, row_input.index('v')]
            direct = 'D'
        elif '<' in row_input:
            position = [j, row_input.index('<')]
            direct = 'L'
        elif '>' in row_input:
            position = [j, row_input.index('>')]
            direct = 'R'
        matrix.append(row_input)

    N = int(input())

    commands = list(input())
    for k in commands:
        if k == 'U':
            direct = 'U'
            if position[0] + directions[direct][0] >= 0 and matrix[position[0] + directions[direct][0]][position[1]] == '.':
                matrix[position[0]][position[1]] = '.'
                position[0] += directions[direct][0]
        elif k == 'D':
            direct = 'D'
            if position[0] + directions[direct][0] <= H - 1 and matrix[position[0] + directions[direct][0]][position[1]] == '.':
                matrix[position[0]][position[1]] = '.'
                position[0] += directions[direct][0]
        elif k == 'L':
            direct = 'L'
            if position[1] + directions[direct][1] >= 0 and matrix[position[0]][position[1] + directions[direct][1]] == '.':
                matrix[position[0]][position[1]] = '.'
                position[1] += directions[direct][1]
        elif k == 'R':
            direct = 'R'
            if position[1] + directions[direct][1] <= W - 1 and matrix[position[0]][position[1] + directions[direct][1]] == '.':
                matrix[position[0]][position[1]] = '.'
                position[1] += directions[direct][1]
        elif k == 'S':
            bullet = [position[0], position[1]]

            while True:
                bullet[0] += directions[direct][0]
                bullet[1] += directions[direct][1]

                if 0 <= bullet[0] < H and 0 <= bullet[1] < W:
                    if matrix[bullet[0]][bullet[1]] in ['.', '_']:
                        continue
                    elif matrix[bullet[0]][bullet[1]] == '*':
                        matrix[bullet[0]][bullet[1]] = '.'
                        break
                    elif matrix[bullet[0]][bullet[1]] == '#':
                        break
                else:
                    break

    if direct == 'U':
        matrix[position[0]][position[1]] = '^'
    elif direct == 'D':
        matrix[position[0]][position[1]] = 'v'
    elif direct == 'L':
        matrix[position[0]][position[1]] = '<'
    elif direct == 'R':
        matrix[position[0]][position[1]] = '>'

    result = []
    for l in matrix:
        result.append(''.join(l))
    answer = '\n'.join(result)
    print(f'#{i} {answer}')