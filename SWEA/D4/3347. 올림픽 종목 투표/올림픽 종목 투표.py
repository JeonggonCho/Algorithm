T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split()) # N:종목 수, M:위원회 수
    values = list(map(int, input().split())) # 재미있는 종목 순으로 정렬된 각 종목 당 개최 비용
    organization_max_value = list(map(int, input().split())) # 위원회 별 최대 개최 허용 비용
    rank = {} # 위원회 기준에 부합하는 종목 투표수
    length = len(values) # 종목 수

    for j in range(length):
        rank[j] = 0

    for k in organization_max_value: # 위원회 개최 허용 비용 순회
        for l in range(length): # 각 종목 인덱스 순회
            if k >= values[l]: # 위원회 비용보다 해당 인덱스의 종목 개최 비용이 작거나 같다면, 투표 수에 1을 더하고 순회를 마친다.
                rank[l] += 1
                break
    selected_sport = sorted(rank.items(), key = lambda x:-x[1])[0][0] + 1 # 투표 수를 많이 받은 값 순서로 정렬한 후, 1등 종목 인덱스에 더하기 1
    print(f'#{i} {selected_sport}')