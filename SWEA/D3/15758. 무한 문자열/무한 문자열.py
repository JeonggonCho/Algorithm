T = int(input())

for i in range(1, T+1):
    char1, char2 = input().split()
    a = ''
    b = ''
    for j in char1:
        a += j
        check1 = char1.replace(a, '')
        if len(check1) == 0:
            break
    for k in char2:
        b += k
        check2 = char2.replace(b, '')
        if len(check2) == 0:
            break
    if a == b:
        print(f'#{i} yes')
    else:
        print(f'#{i} no')