N = int(input())

for i in range(1, N+1): # 숫자 하나씩 꺼내기
    list1 = []
    for j in str(i):
        list1.append(j) # 각자리의 숫자 쪼개기
    if '3' in list1 or '6' in list1 or '9' in list1: # 3, 6, 9 있는지 비교하기
        num = '-' * (list1.count('3') + list1.count('6') + list1.count('9'))
    else:
        num = str(i)
    print(num, end=' ')