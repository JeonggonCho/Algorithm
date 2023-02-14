import sys

char = sys.stdin.readline()
x_list = ''
result = ''

for i in char:
    if i == 'X':
        x_list += i
    elif i == '.':
        if len(x_list) % 2 != 0:
            print(-1)
            break
        elif len(x_list) % 2 == 0:
            A = len(x_list) // 4
            B = (len(x_list) % 4) // 2
            result += ('AAAA' * A + 'BB' * B + '.')
            x_list = ''
        else:
            result += '.'
            x_list = ''
else:
    if len(x_list) % 2 != 0:
        print(-1)
    elif len(x_list) % 2 == 0:
        A = len(x_list) // 4
        B = (len(x_list) % 4) // 2
        result += ('AAAA' * A + 'BB' * B)
        print(result)