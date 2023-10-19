results = []

for i in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    M = int(input())
    order = list(input().split())

    length = len(order)

    for j in range(length):
        if order[j] == 'I':
            x = int(order[j + 1])
            y = int(order[j + 2])
            for k in range(y):
                li.insert(x + k, order[j + k + 3])

        elif order[j] == 'D':
            x = int(order[j + 1])
            y = int(order[j + 2])
            for l in range(y):
                del li[x + l]

        elif order[j] == 'A':
            y = int(order[j + 1])
            for m in range(y):
                li.append(order[j + m + 2])

    ten_nums = li[0:10]

    result = ' '.join(ten_nums)

    results.append(f'#{i} {result}')

for o in results:
    print(o)