T = int(input())

for i in range(1, T+1):
    length = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for j in range(1, length-1):
        li = [nums[j-1], nums[j], nums[j+1]]
        max_num = max(li)
        min_num = min(li)
        if nums[j] != max_num and nums[j] != min_num:
            cnt += 1
    print(f'#{i} {cnt}')