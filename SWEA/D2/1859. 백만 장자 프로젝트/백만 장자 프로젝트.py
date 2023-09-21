T = int(input())

for i in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    benefit = 0
    max_price = nums[-1]

    for j in range(N-2, -1, -1):  # 뒤에서부터 순회
        if nums[j] <= max_price:   # 현재 가격이 최대 가격보다 작거나 같으면
            benefit += max_price - nums[j]  # 이익 계산
        else:                     # 현재 가격이 최대 가격보다 크면 
            max_price = nums[j]   # 최대 가격 업데이트

    print(f'#{i} {benefit}')
