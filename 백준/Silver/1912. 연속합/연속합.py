import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sum = [numbers[0]]

for i in range(len(numbers) - 1):
    sum.append(max(sum[i] + numbers[i + 1], numbers[i + 1]))
    
print(max(sum))