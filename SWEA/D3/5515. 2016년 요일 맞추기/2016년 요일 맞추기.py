import datetime

T = int(input())

for i in range(1, T + 1):
    m, d = map(int, input().split())
    day = datetime.date(2016, m, d)
    print(f'#{i} {day.weekday()}')