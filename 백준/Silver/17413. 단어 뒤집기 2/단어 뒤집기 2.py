import sys

S = sys.stdin.readline().strip()

result = '' # 최종 문자열
char = '' # 단어 저장
tag = False # 현재 태그인지 아닌지 판별

for i in S: # 문자열의 문자 순회
    if i == '<': # 문자가 '<'이면, 태그는 참
        tag = True
        if char: # 단어 저장에 문자가 있으면, 뒤집어서 최종 문자열에 더하고 ''빈 단어로 초기화
            result += char[::-1]
            char = ''
        result += i # 최종 문자열에 '<' 더하기

    elif i == '>': # 문자가 '>'이면, 태그는 거짓이고 최종문자열에 '>' 더하기
        tag = False
        result += i

    elif i == ' ': # 문자가 공백일 경우,
        if tag: # 태그가 참일 경우,
            result += i # 최종 문자열에 공백 더하기
        else: # 태그가 거짓일 경우,
            if char: # 단어 저장에 문자가 있으면, 뒤집어서 최종 문자열에 더하고 ''빈 단어로 초기화
                result += char[::-1]
                char = ''
            result += i # 최종 문자열에 공백 더하기

    else: # 문자가 그 외의 알파벳 혹은 숫자일 경우,
        if tag: # 태그가 참이면, 문자를 최종 문자열에 더하기
            result += i
        else: # 태그가 거짓이면, 문자를 단어 저장에 더하기
            char += i
if char: # 모두 순회 후, 단어 저장에 문자가 남아있을 경우,
    result += char[::-1] # 뒤집어서 최종 문자열에 더한다.

print(result) # 최종 문자열 출력