def solution(numbers):
    list1 = []
    for i in numbers:
        del numbers[numbers.index(i)]
        for j in numbers:
            list1.append(i * j)
    answer = max(list1)
    return answer