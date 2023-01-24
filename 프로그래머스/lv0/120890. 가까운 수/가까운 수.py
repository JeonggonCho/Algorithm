def solution(array, n):
    a = array[0]
    for i in array:
        if abs(n - i) < abs(n - a):
            a = i
        elif abs(n - i) == abs(n - a):
            if i < a:
                a = i
    answer = a
    return answer