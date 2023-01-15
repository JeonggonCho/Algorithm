def solution(num_list):
    answer = []
    num_even = 0
    num_odd = 0
    for i in num_list:
        if i % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
    answer.append(num_even)
    answer.append(num_odd)
    return answer