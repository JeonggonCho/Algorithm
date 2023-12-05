import sys

# 행과 열의 크기를 입력받음
n, m = map(int, sys.stdin.readline().split())

# 행렬을 저장할 리스트 생성
matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

# 각 행에 대해 누적 합 계산
for i in range(n):
    for j in range(1, m):
        matrix[i][j] += matrix[i][j - 1]

# 부분합을 계산할 쿼리의 개수를 입력받음
k = int(sys.stdin.readline())

# 각 쿼리에 대해 부분합을 계산하고 출력
for _ in range(k):
    sum_value = 0
    i, j, x, y = map(int, sys.stdin.readline().split())

    # 특정 열에 대한 부분합 계산
    for row in range(i - 1, x):
        if j == 1:
            sum_value += matrix[row][y - 1]
        else:
            sum_value += matrix[row][y - 1] - matrix[row][j - 2]

    print(sum_value)