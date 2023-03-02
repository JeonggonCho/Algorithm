import sys

a = 1
b = 0

k = int(sys.stdin.readline())

for i in range(k):
    c = a + b
    a = b
    b = c

print(a, b)