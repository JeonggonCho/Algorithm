T = int(input())

for i in range(1, T+1):
    N = int(input()) # 옷의 벌 수
    nums = sorted(list(map(int, input().split())), reverse = True) # N개의 옷의 가격 높은 순으로 정렬
    result = 0

    for j in range(N): # 옷의 가격 순회
        if (j + 1) % 3 != 0: # 3의 배수 번째 옷의 가격 제외 후, 나머지 가격 누적
            result += nums[j]

    print(f'#{i} {result}')