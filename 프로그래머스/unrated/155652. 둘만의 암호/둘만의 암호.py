def solution(s, skip, index):
    answer = ''
    for i in s:
        arr = []
        num = ord(i) + 1
        while len(arr) != index:
            if num > 122:
                num -= 26
            char = chr((num))
            if char not in skip:
                arr.append(char)
            num += 1
        answer += arr[-1]
    return answer