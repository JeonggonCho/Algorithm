import sys

N = int(sys.stdin.readline())
cnt = 0 # 한수의 개수

for i in range(1, N+1): # 1부터 N까지 순회
    if i < 100: # 1부터 99까지는 모두 한수이다.
        cnt += 1
    else: # 100 이상은 판별이 필요하다.
        nums = list(map(int, str(i))) # 숫자를 각 자리마다 분리하기
        if nums[1] - nums[0] == nums[2] - nums[1]: # 공차가 동일할 경우, 한수이다.
            cnt += 1

print(cnt)