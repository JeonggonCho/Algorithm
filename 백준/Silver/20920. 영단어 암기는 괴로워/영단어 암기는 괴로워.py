import sys


N, M = map(int, sys.stdin.readline().split())

dict = {}
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= M:
        if word not in dict:
            dict[word] = [1, len(word)]
        else:
            dict[word][0] += 1

for j in sorted(dict, key=lambda x: (-dict[x][0], -dict[x][1], x)):
    print(j)