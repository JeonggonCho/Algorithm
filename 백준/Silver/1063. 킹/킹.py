import sys

matrix = [[0] * 8 for i in range(8)]

delta = {
    'R' : (0, 1),
    'L' : (0, -1),
    'T' : (-1, 0),
    'B' : (1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1, -1)
}

k, s, n = sys.stdin.readline().split()

kx = ord(k[0]) - 65
ky = 8 - int(k[1])
sx = ord(s[0]) - 65
sy = 8 - int(s[1])

matrix[ky][kx] = 1
matrix[sy][sx] = 2

for i in range(int(n)):
    order = sys.stdin.readline().strip()
    
    dx = delta.get(str(order))[1]
    dy = delta.get(str(order))[0]

    if ky+dy >= 0 and kx+dx >= 0 and ky+dy < 8 and kx+dx < 8:

        if matrix[ky+dy][kx+dx] != 2:
            matrix[ky][kx] = 0
            matrix[ky+dy][kx+dx] = 1

            kx = kx+dx
            ky = ky+dy

        else:
            if sy+dy >= 0 and sx+dx >= 0 and sy+dy < 8 and sx+dx < 8:
                matrix[ky][kx] = 0
                matrix[sy][sx] = 0
                matrix[ky+dy][kx+dx] = 1
                matrix[sy+dy][sx+dx] = 2

                kx = kx+dx
                ky = ky+dy
                sx = sx+dx
                sy = sy+dy

for j in range(8):
    for l in range(8):
        y = str(chr(l + 65))
        x = str(8 - j)
        if matrix[j][l] == 1:
            print(y + x)
        
for m in range(8):
    for o in range(8):
        y = str(chr(o + 65))
        x = str(8 - m)
        if matrix[m][o] == 2:
            print(y + x)