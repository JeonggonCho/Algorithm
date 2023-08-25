for i in range(10):
    T = int(input())
    num_list = []
    for j in range(100):
        num_list.append(list(map(int, input().split())))
    
    sum_list = []
    for k in range(100):
        sum_list.append(sum(num_list[k]))
        col_value = 0
        for l in range(100):
            col_value += num_list[l][k]
        sum_list.append(col_value)
    
    diag_value1 = 0
    diag_value2 = 0
    for m in range(100):
        diag_value1 += num_list[m][m]
        diag_value2 += num_list[m][-m - 1]
    sum_list.append(diag_value1)
    sum_list.append(diag_value2)

    max_value = max(sum_list)
    print(f'#{T} {max_value}')