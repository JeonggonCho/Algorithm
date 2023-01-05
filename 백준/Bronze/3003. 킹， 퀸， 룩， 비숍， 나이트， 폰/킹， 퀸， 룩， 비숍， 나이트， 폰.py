a, b, c, d, e, f = input().split( )
list1 = [1, 1, 2, 2, 2, 8]
list2 = [a, b, c, d, e, f]
list3 = []

for i in range(6):
    if list1[i] == list2[i]:
        list3.append(list2[i])
    else:
        list3.append(int(list1[i]) - int(list2[i]))
for j in list3:
    print(j, end=' ')