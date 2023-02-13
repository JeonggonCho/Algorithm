def solution(numlist, n):
    answer = []
    abs_list = []
    for i in numlist:
        abs_list.append((i, abs(n - i)))
    abs_list.sort(key = lambda x :(x[1], -x[0]))
    for a, b in abs_list:
        answer.append(a)
    return answer