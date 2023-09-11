T = int(input())

for i in range(1, T+1):
    N = int(input())
    li = []

    for j in range(N):
        num = int(input())
        li.append(num)

    equal = sum(li) / len(li)
    cnt = 0

    for k in li:
        cnt += abs(equal - k)
    result = int(cnt // 2)

    print(f'#{i} {result}')