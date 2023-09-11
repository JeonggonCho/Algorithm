def chunk(li, L, R, k):
    li = li[0:L-1] + [k for l in range(R-L+1)] + li[R:]
    return li

T = int(input())

for i in range(1, T+1):
    N, Q = map(int, input().split())
    li = [0 for j in range(N)]
    for k in range(1, Q+1):
        L, R = map(int, input().split())
        li = chunk(li, L, R, k)

    print(f'#{i}', *li)