def solution(my_string, num1, num2):
    answer = ''
    num = 0
    for i in my_string:
        if num == num1:
            answer += my_string[num2]
        elif num == num2:
            answer += my_string[num1]
        else:
            answer += i
        num += 1
    return answer