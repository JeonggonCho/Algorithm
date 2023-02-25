import sys

T = int(sys.stdin.readline())

for i in range(T):
    num_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    print(num_list[2])