import sys

total = 0
num_len = 0
numbers = {}
frequent_value = []

for i in range(10):
    num = int(sys.stdin.readline().strip())
    if num not in numbers:
        numbers[num] = 1
    else:
        numbers[num] += 1


for j in numbers:
    total += j * numbers[j]
    num_len += numbers[j]
    if numbers[j] == max(numbers.values()):
        frequent_value.append(j)
mean_value = total // num_len

print(mean_value)
print(frequent_value[0])