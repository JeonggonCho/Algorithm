import sys

char = sys.stdin.readline().strip()

result = 0
temp = 0
for i in range(len(char) - 1):
    if char[i] == "(":
        if char[i + 1] == ")":
            result += temp
        elif char[i + 1] == "(":
            temp += 1
    elif char[i] == ")":
        if char[i + 1] == ")":
            temp -= 1
            result += 1

print(result)