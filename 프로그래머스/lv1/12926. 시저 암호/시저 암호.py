def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif 65 <= ord(i) <= 90 and (ord(i) + n) > 90:
            answer += chr((ord(i) + n) % 91 + 65)
        elif 97 <= ord(i) <= 122 and (ord(i) + n) > 122:
            answer += chr((ord(i) + n) % 123 + 97)
        else:
            answer += chr(ord(i) + n)
    return answer