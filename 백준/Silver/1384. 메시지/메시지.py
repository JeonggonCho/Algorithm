import sys

group_num = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    name_list = []
    pn_list = [[] for i in range(n)]

    for j in range(n):
        name_pn = sys.stdin.readline().split()
        name_list.append(name_pn[0])
        pn_list[j] = name_pn[1:]
    check = True

    print(f'Group {group_num}')
    pn_order = 0
    for k in pn_list:
        n_order = 0
        for l in k:
            if l == 'N':
                check = False
                print(f'{name_list[pn_order - (n_order + 1)]} was nasty about {name_list[pn_order]}')
            n_order += 1
        pn_order += 1
    
    if check:
        print('Nobody was nasty')

    print()
    group_num += 1