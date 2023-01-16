N = int(input())
list1 = list(map(int, input().split()))
total = 0
list2 = []

for i in list1:
    if i == 1:
        total += 1
        list2.append(total)
    else:
        total = 0
print(sum(list2))