i = int(input())
list1 = []

while i > 0:
    num1, num2 = input().split( )
    list1.append(int(num1) + int(num2))
    i -= 1
for j in list1:
    print(j)