T = int(input())

for i in range(1, T+1):
    char = input()
    num = input()
    index_list = list(map(int, input().split()))
    dict = {}
    result = ''

    for j in index_list:
        if j not in dict:
            dict[j] = 1
        else:
            dict[j] += 1

    for k in range(len(char)):
        if k in dict:
            for l in range(dict[k]):
                result += '-'
            result += char[k]
        else:
            result += char[k]
    if len(char) in dict:
        for m in range(dict[len(char)]):
            result += '-'

    print(f'#{i} {result}')