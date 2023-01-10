list1 = []
list2 = []

for i in range(28):
    list1.append(int(input()))
for j in range(1, 31):
    if j not in list1:
        list2.append(j)
for k in sorted(list2):
    print(k)