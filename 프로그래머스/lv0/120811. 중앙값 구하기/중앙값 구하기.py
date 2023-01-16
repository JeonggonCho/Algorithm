import math
def solution(array):
    answer = sorted(array)[math.floor(len(array)/2)]
    return answer