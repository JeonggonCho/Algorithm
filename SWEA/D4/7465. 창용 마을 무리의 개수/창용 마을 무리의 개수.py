T = int(input()) # 테스트케이스 수 T 입력받기

for i in range(1, T+1): # 테스트케이스 수 만큼 실행
    N, M = map(int, input().split()) # 사람 수 N과 관계 수 M 입력받기
    people = [[j] for j in range(1, N+1)] # 사람들 번호로 이차원리스트 만들기

    for k in range(M): # 관계 수 M 만큼 실행 
        n1, n2 = map(int, input().split()) # 관계 입력받기

        for l in people: # 사람들 이차원리스트 순회
            if n1 in l: # 관계에 속하는 사람이 있는 모임이 나올 경우,
                a = l # a에 모임리스트를 할당
                people.remove(l) # 사람들 리스트에서 해당 모임리스트 삭제

        for m in people: # 사람들 이차원리스트 순회
            if n2 in m: # 관계에 속하는 사람이 있는 모임이 나올 경우,
                b = m # b에 모임리스트를 할당
                people.remove(m) # 사람들 리스트에서 해당 모임리스트 삭제

        if a != b: # a, b에 할당된 모임이 다른 경우,
            people.append(a + b) # 두 개의 모임을 합쳐서 사람들 이차원리스트에 넣기
            a = [] # a와 b 다시 빈 리스트로 초기화
            b = []

    print(f'#{i} {len(people)}') # 최종적으로 사람들 이차원리스트의 길이 출력