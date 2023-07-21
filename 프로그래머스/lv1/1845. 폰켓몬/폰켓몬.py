def solution(nums):
    cnt = {}
    for i in nums:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    if len(cnt) > int(len(nums) / 2):
        return int(len(nums) / 2)
    else:
        return len(cnt)