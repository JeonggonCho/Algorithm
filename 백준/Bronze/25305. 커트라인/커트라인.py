import sys

N, k = map(int, sys.stdin.readline().split())

score_list = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)

print(score_list[k-1])