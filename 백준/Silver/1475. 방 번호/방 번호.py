import sys
import math

nums = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
}

N = list(sys.stdin.readline().rstrip())

for i in N:
    if i == '6' or i == '9':
        nums['6'] += 1
    else:
        nums[i] += 1

nums['6'] = math.ceil(nums['6'] / 2)

cnt = nums.values()

print(max(cnt))