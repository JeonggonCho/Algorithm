T = int(input()) # 테스트케이스 수 T 입력받기
vowel = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트 형성

for i in range(1, T+1): # 테스트케이스 수만큼 실행
    char = input() # 문자열 입력받기
    result = '' # 빈문자열 형성
    for j in char: # 문자열을 순회
        if j not in vowel: # 해당문자가 모음 리스트에 없을 경우,
            result += j # 빈문자열에 누적
    print(f'#{i} {result}') # 최종 누적된 문자열 출력