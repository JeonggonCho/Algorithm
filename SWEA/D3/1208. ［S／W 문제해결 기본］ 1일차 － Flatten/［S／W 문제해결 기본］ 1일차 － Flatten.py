for i in range(1, 11): # 테스트케이스 10번 실행
    cnt = int(input()) # 평탄화 작업횟수 입력받기
    height = list(map(int, input().split())) # 각각의 높이값을 리스트로 받기

    for j in range(cnt): # 작업횟수만큼 실행
        height = sorted(height) # 높이에 따라 정렬하기
        height.append(height.pop() - 1) # 제일 큰 높이값을 pop하여 1빼고 다시 넣기
        height[0] += 1 # 제일 작은 높이값에 1더해주기
    print(f'#{i} {max(height) - min(height)}') # 최종적으로 최대높이값에서 최소높이값을 뺀 값 출력