import sys
from itertools import combinations

def make_str(a):
    result = int(''.join(map(str, a)))
    return result

nums = [9, 8,7, 6, 5, 4, 3, 2, 1, 0]

n = int(sys.stdin.readline())

set_li = set()
for i in range(1, 11):
    nums_combinations = set(map(make_str, list(combinations(nums, i))))
    set_li.update(nums_combinations)
if n > len(set_li) - 1:
    print(-1)
else:
    print(sorted(set_li)[n])