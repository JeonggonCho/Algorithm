# 조합을 이용하여, budget에 맞는 부서들의 조합을 찾고,
# 이 중 부서들의 개수가 최대일 때, 부서 개수를 출력
# 조합 이용 시, 시간초과 발생

def solution(d, budget):
    d.sort()
    li = []
    sum_value = 0
    for i in d:
        if sum_value < budget:
            if i <= budget:
                sum_value += i
                li.append(i)
        elif sum_value > budget:
            li.pop()
            return len(li)
        else:
            return len(li)
    return len(li)