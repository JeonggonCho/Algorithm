for i in range(1, 11):
    N = int(input())
    cal = list(input())
    for j in range(1, N-1, 2):
        cal[j], cal[j+1] = cal[j+1], cal[j]
    new_cal = ''.join(cal)
    result = int(new_cal[0])
    for k in range(1, len(new_cal)):
        if new_cal[k] == '+':
            result += int(new_cal[k-1])
    print(f'#{i} {result}')