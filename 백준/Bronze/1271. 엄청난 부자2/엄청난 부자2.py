import sys

n, m = map(int, sys.stdin.readline().split())

print(*divmod(n, m), sep='\n')