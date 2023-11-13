import sys
import math

N = int(sys.stdin.readline())

num_dict = {}
num_li = []

for i in range(N):
    num = int(sys.stdin.readline())
    # 딕셔너리에 넣기
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

    # 리스트에 넣기
    num_li.append(num)

# 산술평균
sum_num = 0
for j in num_dict:
    sum_num += j * num_dict[j]
avg = round(sum_num / N)
print(avg)

# 중앙값
num_li.sort()
print(num_li[math.ceil(N / 2) - 1])

# 최빈값
mode_value = max(num_dict.values())
mode_keys = []
for k in num_dict:
    if num_dict[k] == mode_value:
        mode_keys.append(k)
if len(mode_keys) == 1:
    print(mode_keys[0])
else:
    mode_keys.sort()
    print(mode_keys[1])

# 범위
num_key = num_dict.keys()
min_num = min(num_key)
max_num = max(num_key)
print(max_num - min_num)