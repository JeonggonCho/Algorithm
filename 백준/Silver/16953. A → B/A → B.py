import sys

A, B = sys.stdin.readline().strip().split()

cnt = 0
while True:
    if B[-1] == '1':
        B = B[0: len(B) - 1]
        cnt += 1
    elif int(B) % 2 == 0:
        B = str(int(B) // 2)
        cnt += 1
    elif int(B) % 2 == 1:
        print(-1)
        break

    if A == B:
        print(cnt + 1)
        break
    elif int(A) > int(B):
        print(-1)
        break
