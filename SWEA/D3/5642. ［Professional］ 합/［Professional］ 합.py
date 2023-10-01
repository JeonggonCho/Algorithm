# 카데인 알고리즘을 적용한 방법

T = int(input()) # 테스트 케이스 개수 입력

for i in range(1, T+1):
    N = int(input()) # 입력받을 숫자의 개수
    nums = list(map(int, input().split())) # 수열 입력받기

    max_so_far = nums[0] # 초기값 설정
    max_ending_here = nums[0]

    for j in range(1, N):
        max_ending_here = max(nums[j], max_ending_here + nums[j])
        max_so_far = max(max_so_far, max_ending_here)

    print(f'#{i} {max_so_far}')