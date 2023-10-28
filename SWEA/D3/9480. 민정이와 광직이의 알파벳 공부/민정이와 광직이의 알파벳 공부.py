from itertools import combinations

results = [] # 결과값 담을 리스트

T = int(input()) # 테스트케이스 수

for i in range(1, T+1):
    N = int(input()) # 입력받을 단어 개수
    cnt = 0 # 모든 소문자를 포함하는 단어 세트 수
    words = [] # 입력받은 단어를 저장할 리스트
    for j in range(N): # 단어 개수만큼 순회하여 리스트에 단어 담기
        word = input()
        words.append(word)

    for k in range(1, len(words)+1): # 각각의 길이별 단어 조합 만들기
        set_words = list(combinations(words, k))

        for l in set_words:
            char = list(set(list(''.join(l)))) # 단어들의 알파벳을 각각 분리하여 set으로 중복없애기
            set_alpha = [] # 소문자만 담을 리스트
            length = len(char)
            if length >= 26: # 알파벳 수가 26개 이상일 경우, 순회를 통해 소문자만 거르기
                for m in range(length):
                    if char[m].islower():
                        set_alpha.append(char[m])
                if len(set_alpha) == 26: # 걸러진 알파벳의 개수가 26개일 경우, 단어 세트 수에 1 더하기
                    cnt += 1

    results.append(f'#{i} {cnt}') # 결과값 리스트에 담기

for n in results: # 모든 결과값 출력
    print(n)