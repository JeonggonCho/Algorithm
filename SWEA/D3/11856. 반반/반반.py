T = int(input()) # 테스트케이스 수 T입력받기

for i in range(1, T+1): # 테스트케이스 수만큼 실행
    char = input() # 길이 4의 문자열 입력받기
    dic = {} # 문자(키)와 개수(값)를 담을 딕셔너리 형성

    for j in char: # 입력받은 문자열에서 문자 하나씩 순회
        if j not in dic: # 딕셔너리 키에 해당 문자가 없을 경우,
            dic[j] = 1 # 해당 문자를 키로 할당하고 개수를 1로 값에 담기
        else: # 딕셔너리에 이미 있다면,
            dic[j] += 1 # 개수(값)에 1 더하기

    if list(dic.values()) == [2, 2]: # 딕셔너리의 값을 리스트로 출력시 [2개, 2개]일 경우,
        print(f'#{i} Yes') # 'Yes' 출력
    else: # 그렇지 않을 경우,
        print(f'#{i} No') # 'No'출력