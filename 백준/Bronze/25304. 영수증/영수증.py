X = int(input())
N = int(input())
sum = 0

for i in range(1, N + 1):
    A, B = input(). split( )
    sum += int(A) * int(B)
if sum == X:
    print('Yes')
else:
    print('No')