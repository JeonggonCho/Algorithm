import math
T = int(input()) # 테스트케이스 수 T 입력받기

for i in range(1, T+1): # 테스트케이스 수만큼 실행
    num = int(input()) # 카드 개수 입력받기
    card_deck = list(input().split()) # 카드 종류 리스트로 받기
    result_deck = [] # 빈리스트 형성

    cut = math.ceil(num / 2) # 카드개수를 이등분하고 반올림하여 리스트 슬라이싱 포인트 구하기
    a = card_deck[:cut] # 카드 종류 리스트에서 슬라이싱 포인트로 구분하여 a 리스트, b 리스트로 나누기
    b = card_deck[cut:]

    for j in range(len(a)): # 카드개수가 짝수일 경우, a와 b의 개수가 같지만, 홀수일 경우, a가 1개 더 크기에 a의 길이 만큼 실행
        try:
            result_deck.append(a[j]) # a 리스트의 카드와 b 리스트의 카드를 하나씩 번갈아가며 빈리스트에 추가하기
            result_deck.append(b[j])
        except: # a리스트와 b리스트의 카드개수가 맞지 않아 오류가 생길 경우,
            pass # 패스하기
    
    print(f'#{i}', *result_deck) # 최종적으로 셔플된 리스트 언패킹으로 출력