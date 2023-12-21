from itertools import combinations

def set_mean_value(li):
    mean_value = 0
    for k in li:
        mean_value += sum(k) / len(k)
    return mean_value / len(li)

T = int(input())

for i in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    li = []
    for j in range(1, n+1):
        li.extend(list(combinations(nums, j)))
    result = set_mean_value(li)
    
    print(f'#{i} {result}')