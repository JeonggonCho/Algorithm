def fac(a):
    cnt = 1
    for i in range(1, a+1):
        cnt *= i
    return cnt

T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    print(fac(m) // (fac(n) * fac(m-n)))