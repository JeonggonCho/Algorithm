import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    chars = list(sys.stdin.readline().split())
    print(f'Case #{i}:',*(chars[::-1]))