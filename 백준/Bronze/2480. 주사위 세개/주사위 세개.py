list1 = list(map(int, input().split()))

if list1[0] == list1[1] == list1[2]:
    print(10000 + list1[0] * 1000)
elif list1[0] == list1[1] != list1[2]:
    print(1000 + list1[0] * 100)
elif list1[0] != list1[1] == list1[2]:
    print(1000 + list1[1] * 100)
elif list1[1] != list1[0] == list1[2]:
    print(1000 + list1[0] * 100)
else:
    print(max(list1) * 100)