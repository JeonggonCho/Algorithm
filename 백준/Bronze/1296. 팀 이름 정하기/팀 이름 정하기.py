import sys
from collections import deque

dict = {}
char = 'LOVE'

name = sys.stdin.readline()
n = int(sys.stdin.readline())

for i in range(n):
    score = 1
    cnt = deque([])
    candidate = sys.stdin.readline().strip()
    a = name + candidate

    for j in char:
        cnt.append(a.count(j))

    for j in range(len(cnt)-1):
        b = cnt.popleft()
        for k in cnt:
            score *= (b + k)
    per = score % 100
    dict[candidate] = per

max_value = max(list(dict.values()))

keys = []

for l in list(dict.keys()):
    if dict[l] == max_value:
        keys.append(l)
        
print(sorted(keys)[0])