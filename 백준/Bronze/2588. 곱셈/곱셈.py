a = int(input())
b = int(input())
list1 = []

for i in str(b):
    list1.append(i)

for j in list1[::-1]:
    print(a * int(j))
print(a * b)