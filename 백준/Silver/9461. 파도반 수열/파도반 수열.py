import sys

T = int(sys.stdin.readline())

for i in range(T):
    seq = [1, 1, 1, 2, 2]
    N = int(sys.stdin.readline())
    if N <= 5:
        print(seq[N-1])
    else:
        for j in range(N-5):
            num = seq[-1] + seq[-5]
            seq.append(num)
        print(seq[-1])