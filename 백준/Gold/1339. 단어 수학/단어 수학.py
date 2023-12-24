import sys

n = int(sys.stdin.readline())

chars = []
for i in range(n):
    char = sys.stdin.readline().strip()
    chars.append(char)

dict = {}
for j in chars:
    for k in range(len(j)):
        if j[k] not in dict:
            dict[j[k]] = 10 ** (len(j) - k)
        else:
            dict[j[k]] += 10 ** (len(j) - k)

li = sorted(dict.items(), key=lambda x: x[1], reverse=True)

numbers = {}
num = 9

for m in li:
    numbers[m[0]] = num
    num -= 1

result = 0
for n in chars:
    combination_number = ''
    for o in n:
        combination_number += str(numbers[o])
    result += int(combination_number)

print(result)