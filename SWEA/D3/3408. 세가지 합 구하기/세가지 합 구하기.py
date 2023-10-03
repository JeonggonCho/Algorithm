T = int(input())

for i in range(1, T+1):
    N = int(input())

    s1 = (1 + N) * N // 2
    s2 = N ** 2
    s3 = (1 + N) * N

    print(f'#{i} {s1} {s2} {s3}')