def solution(my_string):
    answer = ''
    list1 = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in list1:
            answer += i
    return answer