import sys

max_total = 0

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = numbers[i] + numbers[j] + numbers[k]

            if max_total < total <= M:
                max_total = total
                
print(max_total)