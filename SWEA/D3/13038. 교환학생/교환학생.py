T = int(input())

for i in range(1, T+1):
    n = int(input()) #들어야하는 수업 일 수
    schedule = list(map(int, input().split())) #시간표 리스트
    class_days = []

    #시간표 순회하며 수업있는 날의 인덱스들만 리스트로 저장
    for j in range(7):
        if schedule[j] == 1:
            class_days.append(j)

    periods = [] #각 시작일에 따라서 걸리는 일 수들을 저장할 리스트

    #수업있는 날들부터 수업 시작
    for k in class_days:
        start = k
        days = 0
        goal = 0

        while goal != n:
            days += 1
            start += 1
            goal += schedule[start % 7 - 1]

        #걸린 모든 일 수를 periods 리스트에 담기
        periods.append(days)

    #periods 중 가장 적게 걸린 날을 출력
    print(f'#{i} {min(periods)}')