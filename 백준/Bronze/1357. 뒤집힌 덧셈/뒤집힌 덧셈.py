import sys

x, y = map(int, sys.stdin.readline().split())

def rev(a, b):
    answer = 0
    a = int(str(a)[::-1])
    b = int(str(b)[::-1])
    answer = a + b
    answer = int(str(answer)[::-1])
    print(answer)

rev(x, y)