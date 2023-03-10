T = int(input())

num_list = [2, 3, 5, 7, 11]

for i in range(1, T+1):
    answer = []
    n = int(input())
    for j in num_list:
        cnt = 0
        while n % j == 0:
            n /= j
            cnt += 1
        answer.append(cnt)
    print(f'#{i}', *answer)