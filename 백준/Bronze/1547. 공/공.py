import sys

M = int(sys.stdin.readline())
list = [1, 0, 0]

for i in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    list[X-1], list[Y-1] = list[Y-1], list[X-1]
    
print(list.index(1)+1)