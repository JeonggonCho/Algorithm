def solution(numbers, k):
    cnt = (k-1) * 2
    order = cnt % len(numbers)
    answer = numbers[order]
    return answer