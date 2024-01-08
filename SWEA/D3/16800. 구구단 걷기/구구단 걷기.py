import math
import heapq

T = int(input())

for i in range(1, T+1):
    start_position = [1, 1]
    div_cases = []
    N = int(input())

    for j in range(1, math.ceil(math.sqrt(N)) + 1):
        if N % j == 0:
            div_cases.append([j, N // j])

    distances = []
    for k in div_cases:
        distance = k[0] - 1 + k[1] - 1
        heapq.heappush(distances, distance)

    print(f'#{i} {heapq.heappop(distances)}')