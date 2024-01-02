T = int(input())


for i in range(1, T+1):
    dict= {}
    N = int(input())
    for j in range(N):
        num = int(input())
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    answer = 0
    for k in list(dict.keys()):
        if dict[k] % 2 == 1:
            answer += 1

    print(f'#{i} {answer}')