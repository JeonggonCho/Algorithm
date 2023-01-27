import sys

A, B = map(int, sys.stdin.readline().split())
list_A = list(map(int, sys.stdin.readline().split()))
list_B = list(map(int, sys.stdin.readline().split()))

print(len(set(list_A) ^ set(list_B)))