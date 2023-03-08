week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

T = int(input())

for i in range(1, T+1):
    day = input()
    print(f'#{i} {7 - week.index(day)}')