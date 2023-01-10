T = int(input())

month_31 = ['01', '03', '07', '08', '10', '12']
month_30 = ['04', '06', '09', '11']

for i in range(1, T+1):
    numbers = input()
    year = numbers[0:4]
    month = numbers[4:6]
    day = numbers[6:8]
    
    if month in month_31:
        if int(day) >= 1 and int(day) <= 31:
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')
    elif month in month_30:
        if int(day) >= 1 and int(day) <= 30:
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')
    elif month == '02':
        if int(day) >=1 and int(day) <= 28:
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')
    else:
        print(f'#{i} -1')