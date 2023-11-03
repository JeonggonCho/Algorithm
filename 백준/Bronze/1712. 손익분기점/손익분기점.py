import sys

A, B, C = map(int, sys.stdin.readline().split())

if C <= B:
    n = -1
else:
    n = A // (C - B) + 1

print(n)