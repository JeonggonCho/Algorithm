T = int(input())

for i in range(1, T+1):
    N, M, K = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    for j in range(N):
        left_bread = nums[j] // M * K - (j + 1)
        if left_bread < 0:
            result = 'Impossible'
            break
    else:
        result = 'Possible'

    print(f'#{i} {result}')