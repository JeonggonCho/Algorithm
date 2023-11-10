import sys

N = int(sys.stdin.readline())
cnt = 0

for i in range(N):
    char = list(sys.stdin.readline().rstrip())
    li = []
    for j in char:
        if len(li) == 0:
            li.append(j)
        if li[-1] != j and j in li:
            break
        else:
            li.append(j)
    else:
        cnt += 1

print(cnt)