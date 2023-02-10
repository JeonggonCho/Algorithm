T = int(input())

for i in range(1, T+1):
    char = input()
    a = ''

    for j in char:
        a += j
        check = char.replace(a, '')
        if len(check) == 0 or check in a:
            break

    print(f'#{i} {len(a)}')