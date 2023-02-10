T = int(input())

for i in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    m = (m1 + m2) % 60
    h3 = (m1 + m2) // 60
    h = h1 + h2 + h3
    if h % 12 == 0:
        h =12
    else:
        h = h % 12
    
    print(f'#{i} {h} {m}')