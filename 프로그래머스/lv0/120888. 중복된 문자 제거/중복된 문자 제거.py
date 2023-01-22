def solution(my_string):
    answer = ''
    list1 = []
    for i in my_string:
        if i not in list1:
            list1.append(i)
    for j in list1:
        answer += j
    return answer