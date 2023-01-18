char = input()
list_alpha = []

for i in range(97, 123):
    list_alpha.append(chr(i)) # 아스키코드 함수를 이용하여 알파벳 담긴 리스트 형성

for j in list_alpha:
    if j not in char:
        print('-1', end=' ')
    else:
        print(char.index(j), end=' ')