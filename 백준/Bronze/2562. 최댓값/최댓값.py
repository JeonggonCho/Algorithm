import sys
list1 = []

for i in range(9):
    list1.append(int(input()))

max = list1[0]

for j in list1:
    if max <= j:
        max = j
print(f"{max}\n{list1.index(max) + 1}")