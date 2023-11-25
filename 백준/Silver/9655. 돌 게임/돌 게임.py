import sys

N = int(sys.stdin.readline())

if N % 4 == 1 or N % 4 == 3:
    print("SK")
else:
    print("CY")