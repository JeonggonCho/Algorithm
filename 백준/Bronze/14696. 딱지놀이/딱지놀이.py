import sys

N = int(sys.stdin.readline())

for i in range(N):

    a_list = list(map(int, sys.stdin.readline().split()))
    a_cnt = a_list[0]
    a = sorted(a_list[1::])

    b_list = list(map(int, sys.stdin.readline().split()))
    b_cnt = b_list[0]
    b = sorted(b_list[1::])

    for j in range(min(a_cnt, b_cnt)):
        a_num = a.pop()
        b_num = b.pop()
        if a_num > b_num:
            print('A')
            break
        elif a_num < b_num:
            print('B')
            break
        elif len(a) == 0 and len(b) != 0:
            print('B')
            break
        elif len(b) == 0 and len(a) != 0:
            print('A')
            break
    else:
        print('D')