list1 = []
list2 = []

for i in range(5):
    list1.append(int(input()))
for j in list1:
    if j >= 40:
        list2.append(j)
    else:
        list2.append(40)
print(int(sum(list2) / len(list2)))