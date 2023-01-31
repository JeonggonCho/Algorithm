import sys

N = int(sys.stdin.readline())
n_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if i in n_list:
        print(1, end=' ')
    else:
        print(0, end=' ')