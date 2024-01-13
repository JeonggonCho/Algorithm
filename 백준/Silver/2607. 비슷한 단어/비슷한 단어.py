import sys


N = int(sys.stdin.readline())
answer = 0
standard = list(sys.stdin.readline().strip())

for i in range(N - 1):
    origin = standard[:]
    compare = list(sys.stdin.readline().strip())
    different_cnt = 0

    for j in compare:
        if j in origin:
            origin.remove(j)
        else:
            different_cnt += 1

    if different_cnt <= 1 and len(origin) <= 1:
        answer += 1

print(answer)