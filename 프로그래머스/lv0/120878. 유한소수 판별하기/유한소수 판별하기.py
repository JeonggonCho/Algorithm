def solution(a, b):
    num_list1 = []
    num_list2 = []
    for i in range(1, a+1):
        if a % i == 0:
            num_list1.append(i)
    for j in range(1, b+1):
        if b % j == 0:
            num_list2.append(j)
    max_div = max(set(num_list1) & set(num_list2))
    b //= max_div
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    if b == 1:
        answer = 1
    else:
        answer = 2
    
    return answer