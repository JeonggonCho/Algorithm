T = int(input())
results = []
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for i in range(1, T+1):
    t, length = input().split()
    li = list(input().split())
    num_list = []

    for j in li:
        num_list.append(nums.index(j))

    num_list.sort()
    convert = []

    for k in num_list:
        convert.append(nums[k])

    result = ' '.join(convert)

    results.append(f'#{i}\n{result}')

for l in results:
    print(l)