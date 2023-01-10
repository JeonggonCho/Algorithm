N = int(input())
numbers = list(map(int, input().split()))

numbers = sorted(numbers)
print(numbers[round(len(numbers) // 2)])