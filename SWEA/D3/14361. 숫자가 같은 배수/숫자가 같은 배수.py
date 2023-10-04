from itertools import permutations

T = int(input())

for i in range(1, T+1):
    N = input()
    length = len(N)
    num = int(N)

    li = list(permutations(N, length))[1::]

    for j in li:
        new_num = int(''.join(j))
        if new_num > num and new_num % num == 0:
            print(f'#{i} possible')
            break
    else:
        print(f'#{i} impossible')