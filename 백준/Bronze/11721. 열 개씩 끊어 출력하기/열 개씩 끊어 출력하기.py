import math

char = input()
a = math.ceil(len(char) / 10)
cnt = 0

for i in range(a):
    cnt += 1
    b = cnt * 10
    print(char[(b-10):b])