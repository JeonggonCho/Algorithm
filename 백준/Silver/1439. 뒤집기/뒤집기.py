import sys
import math

S = sys.stdin.readline()

answer = 0

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        answer += 1
print(math.ceil(answer // 2))