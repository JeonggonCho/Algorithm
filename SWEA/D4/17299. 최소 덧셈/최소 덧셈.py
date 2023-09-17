T = int(input())

for i in range(1, T+1):
    num = input()
    li = []
    for j in range(1, len(num)):
        value = int(num[:j]) + int(num[j:])
        li.append(value)
    min_value = min(li)
    print(f'#{i} {min_value}')