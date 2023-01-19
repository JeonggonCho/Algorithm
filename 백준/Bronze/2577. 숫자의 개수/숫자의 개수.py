num = 1
num_cnt = {}
for i in range(10):
    num_cnt[i] = 0

for j in range(3):
    num *= int(input())

for k in str(num):
    num_cnt[int(k)] += 1

for l in num_cnt:
    print(num_cnt.get(l))