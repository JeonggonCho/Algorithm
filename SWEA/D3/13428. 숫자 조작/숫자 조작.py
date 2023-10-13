from itertools import combinations

T = int(input())
results = [] # 결과 담을 리스트

for i in range(1, T+1):
    N = input() # 정수 N이 주어짐
    length = len(N) # 정수 N의 길이 length
    indexes = range(length) # 인덱스를 담은 리스트 indexes
    max_num = int(N) # 최댓값 초기화
    min_num = int(N) # 최솟값 초기화

    if N == 0: # N이 0이면 최댓값, 최솟값 모두 0으로 results에 담기
        results.append(f'{i} 0 0')
    else: # N이 0이 아닐 경우,
        matches = list(combinations(indexes,2)) # 각각의 인덱스 쌍을 짝지은 조합 리스트 생성
        for j in matches:
            temp_list= list(N)
            temp_list[j[0]], temp_list[j[1]] = temp_list[j[1]], temp_list[j[0]] # 각 인덱스 자리쌍의 값 바꾸기
            temp = "".join(temp_list)
            if temp.startswith('0'): # 0부터 시작하면 제외
                continue

            temp_num=int(temp)

            if max_num < temp_num: # 최댓값보다 크면 최댓값 갱신하기
                max_num = temp_num

            if min_num >temp_num: # 최솟값보다 작으면 최솟값 갱신하기
                min_num = temp_num

        results.append(f'#{i} {min_num} {max_num}') # 최솟값, 최댓값 results에 담기

for k in results: # 결과값들 출력
    print(k)