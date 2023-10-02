end_points = ['.', '?', '!'] # 문장을 구별할 식별표(마침표, 물음표, 느낌표)

def cnt_end_points(str): # 문장 개수 세는 함수
    cnt = 0
    for _ in str:
        if _ in end_points:
            cnt += 1
    return cnt


def is_name(name): # 숫자가 없고 첫글자는 대문자이고 나머지는 소문자인지 확인하여 이름인지 아닌지 boolean값 반환하는 함수
    length = len(name)
    if length == 1:
        if name[0].isupper():
            return True
        else:
            return False
    elif length >= 2:
        if name.isalpha() and name[0].isupper() and name[1::].islower():
            return True
        else:
            return False


T = int(input())

for i in range(1, T+1):
    N = int(input())
    text = ''

    while(cnt_end_points(text) != N): # 입력받은 문자열에서 문자의 개수가 N과 같을 때까지 문자열 입력받기
        input_words = input()
        text += (input_words + ' ')

    sentences = []
    sentence = ''

    for j in text: # 묹자열 순회하면서 문장 단위로 끊기
        if j in end_points:
            sentences.append(sentence)
            sentence = ''
        else:
            sentence += j

    cnt_name_li = [] # 문장 별로 이름의 개수를 담을 빈리스트 cnt_name_li

    for k in sentences: # 문장 순회
        cnt_name = 0 # 문장별 이름 개수세기
        words = k.split() # 띄어쓰기 단위로 문장 쪼갠 리스트 words
        for l in words: # 단어들 순회
            if is_name(l): # 이름인지 판별하고 이름이면 카운트
                cnt_name += 1
        cnt_name_li.append(cnt_name) # 문장의 이름 개수 리스트에 담기

    print(f'#{i}', *cnt_name_li)