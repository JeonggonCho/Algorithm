import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    answer = 0
    for j in range(a, b+1):
        answer += str(j).count('0')
    print(answer)