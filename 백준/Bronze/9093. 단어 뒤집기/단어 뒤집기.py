T = int(input())

for i in range(T):
    list1 = []
    chars = input().split()
    for j in chars:
        list1.append(j[::-1])
    print(*list1)