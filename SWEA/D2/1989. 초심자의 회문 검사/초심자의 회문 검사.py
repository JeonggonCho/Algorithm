T = int(input())

for i in range(1, T+1):
    reverse = []
    char = list(input())
    for j in char[::-1]:
        reverse.append(j)
    if char == reverse:
        result = 1
    else:
        result = 0
    print(f'#{i} {result}')