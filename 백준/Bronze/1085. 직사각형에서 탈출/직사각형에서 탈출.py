import sys

x, y, w, h = map(int, sys.stdin.readline().split())

distances = [x, y, h-y, w-x]

print(min(distances))