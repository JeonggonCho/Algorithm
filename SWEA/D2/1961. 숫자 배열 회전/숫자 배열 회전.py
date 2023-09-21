def rotate(matrix, N):
    rotated_matrix = [[0] * N for j in range(N)]

    for k in range(N):
        for l in range(N):
            rotated_matrix[k][l] = matrix[N-l-1][k]
    return rotated_matrix

T = int(input())

for i in range(1, T+1):
    N = int(input())
    matrix = []

    for m in range(N):
        nums = list(map(int, input().split()))
        matrix.append(nums)

    rotated_90 = rotate(matrix, N)
    rotated_180 = rotate(rotated_90, N)
    rotated_270 = rotate(rotated_180, N)

    print(f'#{i}')
    for n in range(N):
        result1 = "".join(map(str, rotated_90[n]))
        result2 = "".join(map(str, rotated_180[n]))
        result3 = "".join(map(str, rotated_270[n]))
        print(f'{result1} {result2} {result3}')