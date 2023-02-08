def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num += i
        else:
            if num:
                answer += int(num)
                num = ''
    if num:
        answer += int(num)
    return answer