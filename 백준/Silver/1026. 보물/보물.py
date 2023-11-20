import sys

n = int(sys.stdin.readline())
numbers1 = sorted(list(map(int, sys.stdin.readline().split())))
numbers2 = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

result = 0
for i in range(n):
    result += (numbers1[i] * numbers2[i])

print(result)