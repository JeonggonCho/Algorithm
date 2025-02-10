def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
    return max(triangle[-1])