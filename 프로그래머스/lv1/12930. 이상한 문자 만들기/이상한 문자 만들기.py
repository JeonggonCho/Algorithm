def solution(s):
    word = ''
    word_list = []
    for i in list(s.split(' ')):
        cnt = 0
        for j in i:
            if cnt == 0 or cnt % 2 == 0:
                word += j.upper()
            else:
                word += j.lower()
            cnt += 1
        word_list.append(word)
        word = ''
    answer = ' '.join(word_list)
    return answer