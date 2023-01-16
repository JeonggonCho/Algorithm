n = int(input())

for i in range(n):
    list1 = input()
    list2 = []
    total = 0
    for j in list1:
        if j == 'O':
            total += 1
            list2.append(total)
        else:
            total = 0
    print(sum(list2))