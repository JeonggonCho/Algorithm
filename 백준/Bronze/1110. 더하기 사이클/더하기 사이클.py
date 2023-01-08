N = int(input())
cycle = 0

if N >= 0 and N <= 9:
    N = N * 10

N1 = N

while True:
    cycle += 1
    N1 = ((N1 % 10) * 10) + (((N1 // 10) + (N1 % 10)) % 10)
    if N == N1:
        break
print(cycle)