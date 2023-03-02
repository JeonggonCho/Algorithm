import sys

k = int(sys.stdin.readline())

for i in range(1, k+1):
    numbers = list(map(int, sys.stdin.readline().split()))
    score = sorted(numbers[1::])
    gap_list = []

    for j in range(1, len(score)):
        gap_list.append(score[j] - score[j-1])

    print(f'Class {i}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(gap_list)}')