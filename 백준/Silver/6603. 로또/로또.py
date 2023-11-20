import sys
from itertools import combinations

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers == [0]:
        break
    else:
        lotto = combinations(numbers[1::], 6)

    for i in lotto:
        print(" ".join(map(str, i)))
    print()