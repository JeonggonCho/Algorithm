def solution(polynomial):
    answer = ''
    num = []
    x = 0
    for i in list(polynomial.split(' ')):
        if 'x' in i:
            if i[:-1] == '':
                x += 1
            else:
                x_num = int(i[:-1])
                x += x_num
        elif i == '+':
            pass
        else:
            num.append(int(i))
    if x:
        if x == 1:
            answer += 'x'
        else:
            answer += str(x)
            answer += 'x'
    if x and num:
        answer += ' + '
    if num:
        answer += str(sum(num))
        
    return answer