T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    if W >= R:
        B = Q + (W - R) * S
    else:
        B = Q
    if A > B:
        print(f'#{i} {B}')
    else:
        print(f'#{i} {A}')