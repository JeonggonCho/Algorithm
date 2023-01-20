T = int(input())

for i in range(1, T+1):
    list1 = []
    sides = list(map(int, input().split()))
    for j in sides:
        if sides.count(j) % 2 == 1:
            list1.append(j)
    print(f'#{i} {list1[0]}')