list1 = []
list2 = []

for i in range(10):
    list1.append(int(input()))
for j in list1:
    list2.append(j % 42)
print(len(set(list2)))