T = int(input())

for i in range(1, T+1):
    n = int(input())
    list1 = []
    x = 0
    while sorted(set(list1)) != ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        x += 1
        N = x * n
        for k in str(N):
            if k not in list1:
                list1.append(k)
    print(f'#{i} {N}')