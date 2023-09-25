T = int(input())

for i in range(1, T+1):
    li = []
    result = ''
    max_length = 0
    for j in range(5):
        char = list(input())
        if len(char) >= max_length:
            max_length = len(char)
        li.append(char)

    for k in range(max_length):
        for l in li:
            if len(l) >= k + 1:
                result += l[k]

    print(f'#{i} {result}')