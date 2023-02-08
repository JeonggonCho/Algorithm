import sys

N, M, K = map(int, sys.stdin.readline().split())

print(*divmod(K, M))