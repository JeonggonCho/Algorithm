N = int(input())
cycle = 0
N1 = N

while True:
    A = N1 % 10
    B = N1 // 10
    N1 = (A * 10) + ((A + B) % 10)
    cycle += 1
    if N == N1:
        break
print(cycle)