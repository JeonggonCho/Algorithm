T = int(input())

for i in range(1, T+1):
    N = int(input()) # 노선 개수
    stations = {} # 정류장 번호(키)-정류장 지나는 버스의 개수(값) 딕셔너리

    for j in range(1, 5001): # 딕셔너리 초기화
        stations[j] = 0

    for j in range(N):
        A, B = map(int, input().split()) # 각 j번째 노선은 A 이상, B 이하인 정류장만 다닌다.
        for k in range(A, B+1): # A 이상 B 이하인 정류장에 더하기 1
            stations[k] += 1

    P = int(input()) # P개의 정류장
    selected_stations = [] # P개 정류장의 버스개수를 담을 리스트

    for l in range(P):
        station = int(input())
        selected_stations.append(stations[station])

    print(f'#{i}', *selected_stations)