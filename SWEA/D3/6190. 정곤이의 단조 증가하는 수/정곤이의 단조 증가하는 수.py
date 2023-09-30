def is_mono(num): # 단조 증가하는 수 판별 함수
    str_num = str(num) # 파라미터로 받은 숫자를 문자열로 변환
    length = len(str_num) # 문자열 길이 length
    check = True

    for _ in range(length - 1): # 문자열 길이-1 만큼 인덱스 순회
        if str_num[_] > str_num[_+1]: # 앞의 숫자가 뒤의 숫자보다 크면, false를 리턴, 아니면 true 리턴 후 break
            check = False
            break
    return check


T = int(input()) # 테스트케이스 수 T

for i in range(1, T+1):
    N = int(input()) # 테스트 케이스 별 숫자 리스트 개수
    nums = list(map(int, input().split())) # 숫자 리스트
    li = [] # 두 수의 곱들을 담을 빈 리스트

    for j in range(N-1): # 두 수의 곱을 li 리스트에 담는다.
        for k in range(j+1, N):
            A = nums[j] * nums[k]
            li.append(A)

    mono_li = [] # 단조 증가하는 수를 담을 빈 리스트

    for l in li: # li 리스트를 순회하여 단조 증가하는 수이면, mono_li 리스트에 담는다.
        result = is_mono(l)
        if result == True:
            mono_li.append(l)

    if mono_li: # 단조 증가하는 수가 있으면, 정렬 후, 가장 큰 수를 출력한다.
        answer = sorted(mono_li)[-1]
        print(f'#{i} {answer}')
    else: # 없으면, -1을 출력한다.
        print(f'#{i} -1')