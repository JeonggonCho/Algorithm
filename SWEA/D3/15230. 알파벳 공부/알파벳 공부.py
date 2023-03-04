alpha = ''

for i in range(97, 123):
    alpha += chr(i)

T = int(input())

for j in range(1, T+1):
    cnt = 0
    char = input()
    for k in range(min(len(alpha), len(char))):
        if alpha[k] == char[k]:
            cnt += 1
        else:
            break
    print(f'#{j} {cnt}')