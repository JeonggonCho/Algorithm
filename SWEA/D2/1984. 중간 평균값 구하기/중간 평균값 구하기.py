T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    mean_value = int(round((sum(numbers) - min(numbers) - max(numbers)) / 8, 0))
    print(f'#{i} {mean_value}')