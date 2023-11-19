import sys

scale = list(map(int, sys.stdin.readline().split()))

if scale == [i for i in range(1, 9)]:
    print("ascending")
elif scale == [j for j in range(8, 0, -1)]:
    print("descending")
else:
    print("mixed")