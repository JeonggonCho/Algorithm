char = input() # 단어입력받기

while True: # 계속 실행하기
    print(char[0:10]) # 앞부분 10개 출력
    char = char.replace(char[0:10], '') # 앞부분 10개 삭제
    
    if len(char) == 0: # 출력할 문자가 없으면 멈춤
        break