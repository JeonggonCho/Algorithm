import math

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    num_list = []
    for j in range(N):
        numbers = list(input())
        num_list.append(numbers)
    
    position = math.ceil(N // 2)
    center = math.ceil(N // 2)
    get_num = 1
    result = 0
    for k in num_list:
        result += sum(map(int, k[position:position + get_num]))
        if num_list.index(k) < center:
            position -= 1
            get_num += 2
        else:
            position += 1
            get_num -= 2
    print(f'#{i} {result}')