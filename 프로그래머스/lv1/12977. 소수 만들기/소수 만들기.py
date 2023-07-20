from itertools import combinations
import math

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        a = sum(i)
        for j in range(2, math.ceil(math.sqrt(a)) + 1):
            if a % j == 0:
                break
        else:
            answer += 1
    return answer