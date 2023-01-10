N = int(input())
numbers = list(map(int, input().split()))
M = max(numbers)
score = []

for i in numbers:
    score.append(i / M * 100)
print(sum(score) / len(score))