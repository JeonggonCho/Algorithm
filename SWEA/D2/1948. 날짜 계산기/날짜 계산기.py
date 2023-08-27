T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # (인덱스)월의 일 수

for i in range(1, T + 1):
    month_1, day_1, month_2, day_2 = map(int, input().split()) # 시작월일 마지막월일 입력받기
    if month_1 == month_2: #시작월과 마지막월이 같을 경우
        print(f'#{i} {day_2 - day_1 + 1}')
    else: # 다를 경우
        day_count = days[month_1] - day_1 + 1
        for j in range(month_1 + 1, month_2):
            day_count += days[j]
        day_count += day_2
        print(f'#{i} {day_count}')