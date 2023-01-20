T = int(input())

for i in range(1, T+1):
    mirrored = ''
    chars = input()
    for j in chars:
        if j == 'b':
            mirrored += 'd'
        elif j == 'd':
            mirrored += 'b'
        elif j == 'p':
            mirrored += 'q'
        else:
            mirrored += 'p'

    print(f'#{i} {mirrored[::-1]}')