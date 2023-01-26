T = int(input())

for i in range(T):
    PS = list(input())
    cnt = 0
    if PS[0] == ')' or PS[-1] == '(':
        print('NO')
    else:
        while len(PS) > 0:
            a = PS.pop()
            if a == ')':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                print('NO')
                break
        if cnt == 0:
            print('YES')
        elif cnt > 0:
            print('NO')