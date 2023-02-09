import math

l, a, b, c, d = [int(input()) for i in range(5)]

korean = math.ceil(a / c)
mat = math.ceil(b / d)
print(l - max(korean, mat))