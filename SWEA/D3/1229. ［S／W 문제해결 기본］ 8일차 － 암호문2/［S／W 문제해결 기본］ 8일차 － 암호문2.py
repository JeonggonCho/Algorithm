results = []

for i in range(1, 11):
    N = int(input())
    li = list(input().split())
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
            del li[x:x + y]

    ten_nums = li[0:10]

    result = ' '.join(ten_nums)

    results.append(f'#{i} {result}')

for m in results:
    print(m)