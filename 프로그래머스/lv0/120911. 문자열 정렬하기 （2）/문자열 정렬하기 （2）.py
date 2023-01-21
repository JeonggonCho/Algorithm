def solution(my_string):
    answer = ''
    list1 = sorted(my_string.lower())
    for i in list1:
        answer += i
    return answer