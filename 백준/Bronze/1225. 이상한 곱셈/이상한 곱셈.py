import sys

a_sum = 0
b_sum = 0

a, b = sys.stdin.readline().split()
a = list(a)
b = list(b)

while len(a) > 0:
    a_sum += int(a.pop())
while len(b) > 0:
    b_sum += int(b.pop())
print(a_sum * b_sum)